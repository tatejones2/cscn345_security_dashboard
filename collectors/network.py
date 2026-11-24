import psutil


def collect_listening_ports():
    ports = []

    for connection in psutil.net_connections(kind="inet"):
        if connection.status == psutil.CONN_LISTEN:
            ports.append({
                "ip": connection.laddr.ip,
                "port": connection.laddr.port,
                "protocol": "TCP",
            })

    return sorted(ports, key=lambda item: item["port"])
