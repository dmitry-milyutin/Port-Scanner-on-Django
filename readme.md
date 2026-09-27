# Port Scanner (Django)

A web-based TCP port scanner built with Django. Enter a target host, pick which ports to check, and see which ones are open, all from the browser instead of the command line.(Example images in Demo folder)


## Features

- **Common port scan:** check all standard service ports at once (HTTP, SSH, FTP, etc.), defined in `common_ports.py`
- **Custom port lists:** search for any port and add it to your own list to scan
- **Session-based:** your port list is saved per browser session using cookies, so no account is needed
- **Standalone demo:** `scanner.py` shows the core scanning logic on its own, outside of Django

## How it works

<!-- Fill in 2–3 sentences in your own words: e.g. how scanner.py checks a port
(does it open a TCP connection with a timeout?), and how the Django view uses it. -->

## Setup

1. Clone the repo and create a virtual environment:
```bash
   git clone https://github.com/dmitry-milyutin/Port-Scanner-on-Django.git
   cd Port-Scanner-on-Django
   python3 -m venv venv
   source venv/bin/activate
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Django secret key:
```
   SECRET_KEY=your_secret_key_here
```

## Running

**Locally:**
```bash
python3 manage.py runserver
```
Then open http://127.0.0.1:8000

**On another machine or your local network:**
1. Add the server's IP to `ALLOWED_HOSTS` in `settings.py`
2. Run:
```bash
   python3 manage.py runserver 0.0.0.0:8000
```

> `runserver` is Django's development server and isn't meant for production. For a real deployment, use a production server like Gunicorn behind Nginx.

## Responsible use

Only scan hosts you own or have explicit permission to test. Unauthorized port scanning can violate network policies and, in some jurisdictions, the law.

## Built with

Python, Django, HTML/CSS
