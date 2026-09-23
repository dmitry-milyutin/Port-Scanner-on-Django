import socket
from django.shortcuts import render
from .common_ports import SERVICE_PORTS

# 22 -- ["sftp", "ssh"]
PORT_NAMES = {}
for name, port in SERVICE_PORTS.items():
    PORT_NAMES.setdefault(port, [])
    PORT_NAMES[port].append(name)


def home_page(request):
    return render(request, "home.html")

def label(port):
    names = PORT_NAMES.get(port)
    if names:
        return f"{port} ({', '.join(names)})"
    return str(port)


def parse_port(raw):
    if raw.isdigit() and 0 <= int(raw) <= 65535:
        return int(raw)
    
    return None


def search_ports(query):
    query = query.strip().lower()
    if not query:
        return []
    if query.isdigit():
        port = parse_port(query)

        return [port] if port is not None else []
    
    return sorted({port for name, port in SERVICE_PORTS.items() if query in name})

def scan_ports(target_ip, ports):
    open_ports, closed_ports = [], []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        if sock.connect_ex((target_ip, port)) == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)

        sock.close()
    return open_ports, closed_ports


def scan_page(request):
    ports = request.session.get("ports", [])
    target_ip = request.session.get("target_ip", "")
    query = ""
    open_ports, closed_ports = [], []
    scanned = False
    error = ""

    if request.method == "POST":
        target_ip = request.POST.get("target_ip", "").strip()
        query = request.POST.get("q", "").strip()

        if "add" in request.POST:
            port = parse_port(request.POST["add"])
            if port is not None and port not in ports:
                ports.append(port)
        elif "remove" in request.POST:
            port = parse_port(request.POST["remove"])
            if port in ports:
                ports.remove(port)
        elif "clear" in request.POST:
            ports = []
        elif "scan_all" in request.POST:
            ports = sorted(set(SERVICE_PORTS.values()))

        if "scan" in request.POST or "scan_all" in request.POST:
            if not target_ip:
                error = "Enter a target IP first"
            elif not ports:
                error = "Add at least one port to scan"
            else:
                try:
                    open_ports, closed_ports = scan_ports(target_ip, sorted(ports))
                    scanned = True
                except socket.gaierror:
                    error = f"Couldn't resolve '{target_ip}'"

        request.session["ports"] = ports
        request.session["target_ip"] = target_ip

    return render(request, "scan.html", {
        "target_ip": target_ip,
        "query": query,
        "results": [(p, label(p)) for p in search_ports(query)],
        "ports": ports,
        "selected": [(p, label(p)) for p in ports],
        "scanned": scanned,
        "open_ports": [(p, label(p)) for p in open_ports],
        "closed_ports": [(p, label(p)) for p in closed_ports],
        "error": error,
    })