### Read Me

## Setup

Make your .env file and add your secret key:

secret_key=type_your_key

Install the needed libraries from req.txt:

pip install -r req.txt


To run locally:

python3 manage.py runserver

On server:

Add IP to ALLOWED_HOSTS in settings

python3 manage.py runserver [IP]:port

## Info

The port scanner runs cookie sessions

You can add a custom port you would like to scan by searching for it and adding it to your list

You can also scan all the common ports at once which are listed in common_ports.py

There is a demo file explaining how the scanner works in scanner.py