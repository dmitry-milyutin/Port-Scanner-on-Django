import socket

# target_ip = "127.0.0.1"
target_ip ="8.8.8.8"
ports_to_check = [22, 80, 443, 8000, 53]
# SSH, HTTP, HTTPS, Django, DNS

for port in ports_to_check:
    # if port != 53
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    # 
    
    result = sock.connect_ex((target_ip, port))
    # Takes ONE argument: a tuple (target_ip, port) — note the double parentheses,
    #   the outer ones call the function, the inner ones form the tuple itself
    # Attempts the real TCP handshake (SYN -> SYN-ACK -> ACK) to that address+port
    # Returns an integer error code:
    #   0        = open
    #   nonzero  = close/filtered

    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed or filtered")

    sock.close()

# These two arguments together define what socket this is before any connection happens
# socket.AF_INET   -> address family: use IPv4 (there's also AF_INET6 for IPv6)
# socket.SOCK_STREAM -> socket type: use TCP (SOCK_DGRAM would mean UDP instead)