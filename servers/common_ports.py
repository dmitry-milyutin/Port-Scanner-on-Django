SERVICE_PORTS = {
    # Web
    "http": 80,
    "https": 443,
    "http-alt": 8080,
    "https-alt": 8443,

    # File transfer
    "ftp": 21,
    "ftp-data": 20,
    "sftp": 22,      # runs over SSH
    "tftp": 69,

    # Remote access
    "ssh": 22,
    "telnet": 23,
    "rdp": 3389,
    "vnc": 5900,

    # Email
    "smtp": 25,
    "smtps": 465,
    "pop3": 110,
    "pop3s": 995,
    "imap": 143,
    "imaps": 993,

    # Naming / network services
    "dns": 53,
    "dhcp": 67,
    "ntp": 123,
    "snmp": 161,
    "ldap": 389,

    # Databases
    "mysql": 3306,
    "postgres": 5432,
    "mssql": 1433,
    "oracle": 1521,
    "mongodb": 27017,
    "redis": 6379,

    # Dev servers / frameworks
    "django": 8000,
    "flask": 5000,
    "node": 3000,
    "react": 3000,

    # File sharing
    "smb": 445,
    "nfs": 2049,

    # Messaging / other
    "irc": 6667,
    "mqtt": 1883,
}