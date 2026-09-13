from django.shortcuts import render
from django.conf import settings
from .common_ports import SERVICE_PORTS
import socket


def home_page(request):
    return render(request, "home.html", {})


def scan_page(request):
    target_ip = request.GET.get("target_ip", "")
    checked_ports = request.GET.getlist("ports")

    open_ports = []
    closed_ports = []

    for port in checked_ports:
        port = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)

        sock.close()

    return render(request, "scan.html", {"target_ip": target_ip, "checked_ports": checked_ports, "service_ports": SERVICE_PORTS, "open_ports": open_ports, "closed_ports": closed_ports})