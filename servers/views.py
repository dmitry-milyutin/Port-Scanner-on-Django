from django.shortcuts import render
from django.conf import settings
import socket


def home_page(request):
    return render(request, "home.html", {})

def scan_page(request):
    target_ip = request.GET.get("target_ip", "")
    open_ports = []
    closed_ports = []

    ports_to_check = [22, 80, 443, 8000, 53, 59871, 3000]
    # SSH, HTTP, HTTPS, Django, DNS, private django, local host

    for port in ports_to_check:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)

        sock.close()

    print(f"Open: {open_ports}\nClosed: {closed_ports}")

    return render(request, "scan.html", {"target_ip" : target_ip, "open_ports" : open_ports, "closed_ports" : closed_ports})