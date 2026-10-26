SERVICE_PORTS = {
    # Web
    "http": 80,
    "https": 443,
    "http-alt": 8080,
    "https-alt": 8443,
    "http-proxy": 3128,          # Squid
    "haproxy-stats": 8404,

    # File transfer
    "ftp": 21,
    "ftp-data": 20,
    "sftp": 22,                  # runs over SSH
    "tftp": 69,
    "rsync": 873,

    # Remote access / admin panels
    "ssh": 22,
    "telnet": 23,
    "rdp": 3389,
    "vnc": 5900,
    "webmin": 10000,
    "cockpit": 9090,
    "portainer": 9443,

    # Email
    "smtp": 25,
    "submission": 587,           # SMTP with STARTTLS (client mail)
    "smtps": 465,
    "pop3": 110,
    "pop3s": 995,
    "imap": 143,
    "imaps": 993,
    "mailhog-smtp": 1025,        # dev mail catcher
    "mailhog-web": 8025,

    # Naming / network services
    "dns": 53,
    "dhcp": 67,
    "kerberos": 88,
    "rpcbind": 111,
    "ntp": 123,
    "netbios-ns": 137,
    "netbios-ssn": 139,
    "snmp": 161,
    "snmp-trap": 162,
    "ldap": 389,
    "ldaps": 636,
    "syslog": 514,               # UDP
    "syslog-tls": 6514,

    # VPN
    "ipsec-ike": 500,
    "ipsec-nat-t": 4500,
    "openvpn": 1194,
    "wireguard": 51820,

    # Databases
    "mysql": 3306,
    "postgres": 5432,
    "pgbouncer": 6432,
    "mssql": 1433,
    "oracle": 1521,
    "mongodb": 27017,
    "mongodb-shard": 27018,
    "mongodb-config": 27019,
    "redis": 6379,
    "redis-sentinel": 26379,
    "memcached": 11211,
    "elasticsearch": 9200,
    "elasticsearch-transport": 9300,
    "cassandra": 9042,
    "couchdb": 5984,
    "influxdb": 8086,
    "clickhouse-http": 8123,
    "neo4j-http": 7474,
    "neo4j-bolt": 7687,

    # Python app servers (behind nginx)
    "gunicorn": 8000,
    "uwsgi": 3031,               # common uwsgi-protocol socket
    "daphne": 8000,              # Django Channels / ASGI
    "uvicorn": 8000,

    # Dev servers / frameworks
    "django": 8000,
    "flask": 5000,
    "node": 3000,
    "react": 3000,
    "nextjs": 3000,
    "vite": 5173,
    "angular": 4200,
    "webpack-dev": 8080,
    "jupyter": 8888,
    "php-fpm": 9000,

    # Task queues / message brokers
    "rabbitmq": 5672,
    "rabbitmq-tls": 5671,
    "rabbitmq-mgmt": 15672,
    "epmd": 4369,                # Erlang port mapper (RabbitMQ)
    "celery-flower": 5555,
    "kafka": 9092,
    "zookeeper": 2181,
    "nats": 4222,
    "mqtt": 1883,
    "mqtts": 8883,
    "irc": 6667,

    # Monitoring / logging
    "prometheus": 9090,
    "alertmanager": 9093,
    "node-exporter": 9100,
    "nginx-exporter": 9113,
    "redis-exporter": 9121,
    "postgres-exporter": 9187,
    "grafana": 3000,
    "kibana": 5601,
    "logstash-beats": 5044,
    "sentry": 9000,

    # Containers / orchestration / infra
    "docker": 2375,              # unencrypted, should never be exposed
    "docker-tls": 2376,
    "docker-registry": 5000,
    "kubernetes-api": 6443,
    "kubelet": 10250,
    "etcd-client": 2379,
    "etcd-peer": 2380,
    "consul": 8500,
    "vault": 8200,
    "minio": 9000,
    "minio-console": 9001,

    # File sharing
    "smb": 445,
    "nfs": 2049,
}