import time
import psutil

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from collectors.ssh import collect_ssh_events, summarize_ssh_events
from collectors.fail2ban import collect_fail2ban_events, summarize_fail2ban_events
from collectors.network import collect_listening_ports

console = Console()


def show_system_health():
    table = Table(title="Linux Server Health")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    uptime = int((time.time() - psutil.boot_time()) / 3600)

    table.add_row("CPU Usage", f"{cpu}%")
    table.add_row("Memory Usage", f"{memory}%")
    table.add_row("Disk Usage", f"{disk}%")
    table.add_row("System Uptime", f"{uptime} hours")

    console.print(table)


def show_ssh_activity():
    events = collect_ssh_events()
    summary = summarize_ssh_events(events)

    table = Table(title="SSH Security Activity")

    table.add_column("Event Type", style="cyan")
    table.add_column("Count", justify="right")

    table.add_row("Successful Logins", str(summary["successful"]))
    table.add_row("Failed Authentications", str(summary["failed"]))
    table.add_row("Invalid User Events", str(summary["invalid_user"]))
    table.add_row("Total Recognized Events", str(summary["total"]))

    console.print(table)


def show_fail2ban_activity():
    events = collect_fail2ban_events()
    summary = summarize_fail2ban_events(events)

    table = Table(title="Fail2ban Security Activity")

    table.add_column("Event Type", style="cyan")
    table.add_column("Count", justify="right")

    table.add_row("Detected Events (Found)", str(summary["found"]))
    table.add_row("Ban Events", str(summary["bans"]))
    table.add_row("Unban Events", str(summary["unbans"]))
    table.add_row("Total Recognized Events", str(summary["total"]))

    console.print(table)


def show_listening_ports():
    ports = collect_listening_ports()

    table = Table(title="Listening Network Ports")

    table.add_column("IP Address", style="cyan")
    table.add_column("Port", justify="right")
    table.add_column("Protocol")

    for port in ports:
        table.add_row(
            port["ip"],
            str(port["port"]),
            port["protocol"]
        )

    console.print(table)


def main():
    console.print(Panel.fit(
        "[bold cyan]Linux Security Monitor[/bold cyan]\n"
        "DigitalOcean Ubuntu Server",
        border_style="cyan"
    ))

    show_system_health()
    show_ssh_activity()
    show_fail2ban_activity()
    show_listening_ports()


if __name__ == "__main__":
    main()
