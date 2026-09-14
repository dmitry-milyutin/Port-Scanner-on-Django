from django.shortcuts import render
from django.conf import settings
from .common_ports import SERVICE_PORTS
import socket
from django.core.paginator import Paginator


def home_page(request):
    return render(request, "home.html", {})


def scan_page(request):
    target_ip = request.GET.get("target_ip", "")
    scan_all = request.GET.get("scan_all", "")

    checked_ports = []
    if scan_all:
        for port in SERVICE_PORTS.items():
            checked_ports.append(port)
    else:
        checked_ports_raw = request.GET.getlist("ports")
        for p in checked_ports_raw:
            checked_ports.append(int(p))

    open_ports = []
    closed_ports = []
    if target_ip and checked_ports:
        for port in checked_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                open_ports.append(port)
            else:
                closed_ports.append(port)

            sock.close()

    return render(request, "scan.html", {"target_ip": target_ip, "checked_ports": checked_ports, "service_ports": SERVICE_PORTS, "open_ports": open_ports, "closed_ports": closed_ports})

def get_port_name(port):
    for name, p in SERVICE_PORTS.items():
        if p == port:
            return name
        
    return f"Port {port}"


def search_ports(query):
    query = query.strip().lower()

    if not query:
        return []
    
    if query.isdigit():
        port = int(query)
        if 0 <= port <= 65535:
            return [(port, get_port_name(port))]
        
        return []
    
    results = []

    for name, port in SERVICE_PORTS.items():
        if query in name.lower():
            results.append((port, name))

    return results

def all_ports_page(request):
    paginator = Paginator(range(0, 65536), 100)
    page_obj = paginator.get_page(request.GET.get("page", 1))
    ports = []
    for port in page_obj:
        ports.append((port, get_port_name(port)))
    return render(request, "all_ports.html", {"ports": ports, "page_obj": page_obj})

def port_search_page(request):
    query = request.GET.get("q", "")
    results = search_ports(query) if query else []
    return render(request, "port_search.html", {"query": query, "results": results})