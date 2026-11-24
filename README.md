# Linux Security Dashboard

**CSCN 345 | Liberty University**  
**Author: Tate Jones**

## Overview

The Linux Security Dashboard is a Python-based command-line application designed to monitor the health and security of a Linux server. The project was developed using an Ubuntu server hosted on DigitalOcean.

The dashboard combines system resource monitoring, SSH authentication log analysis, Fail2ban activity, and network port monitoring into a single terminal interface.

## Features

- **System Health:** Monitors CPU usage, memory usage, disk usage, and system uptime.
- **SSH Monitoring:** Tracks successful logins, failed authentications, and invalid user attempts.
- **Fail2ban Monitoring:** Tracks detected events, IP address bans, and unbans.
- **Network Monitoring:** Displays listening TCP ports and their associated IP addresses.
- **Terminal Dashboard:** Presents collected information in organized, color-coded tables.

## Technologies Used

- Python 3
- Ubuntu Linux
- DigitalOcean
- psutil
- Rich
- Fail2ban
- OpenSSH
- Regular expressions

## Project Structure

```
cscn345_security_dashboard/
├── collectors/
│   ├── fail2ban.py
│   ├── network.py
│   └── ssh.py
├── security_monitor.py
├── .gitignore
└── README.md
```

| File | Description |
|---|---|
| `security_monitor.py` | Main program responsible for displaying the dashboard and system health information. |
| `collectors/ssh.py` | Collects and summarizes SSH authentication events. |
| `collectors/fail2ban.py` | Collects and summarizes Fail2ban security events. |
| `collectors/network.py` | Identifies listening TCP ports on the server. |
| `.gitignore` | Excludes unnecessary files from version control. |

## Installation

Clone the repository:

```bash
git clone https://github.com/tatejones2/cscn345_security_dashboard.git
cd cscn345_security_dashboard
```

Install Python and virtual environment support if needed:

```bash
sudo apt install python3 python3-venv
```

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required Python libraries:

```bash
pip install psutil rich
```

## Usage

Activate the virtual environment and run the program:

```bash
source .venv/bin/activate
python3 security_monitor.py
```

The dashboard displays four sections directly in the terminal:

1. Linux Server Health
2. SSH Security Activity
3. Fail2ban Security Activity
4. Listening Network Ports

## Log Sources

The program collects security information from the following Linux log files:

| Log File | Purpose |
|---|---|
| `/var/log/auth.log` | SSH authentication activity |
| `/var/log/fail2ban.log` | Fail2ban security events |

The user running the program must have the appropriate permissions to read these files. Fail2ban and SSH logging must also be configured on the server.

## Limitations

The program analyzes the most recent 1,000 lines of each log file by default. The dashboard provides a snapshot of the server's current state and must be run again to refresh the displayed information.

The network monitoring feature identifies listening TCP ports but does not determine whether those ports are accessible externally.

The dashboard is a monitoring tool and does not directly modify server security configurations.

## Future Improvements

- Automatic dashboard refreshing
- Security event timeline
- Firewall rule monitoring
- Docker container monitoring
- Lynis security audit integration
- Automated security alerts

## Project Purpose

The purpose of this project is to demonstrate how Python programming can be combined with Linux system administration and cybersecurity. By collecting and displaying information from multiple sources, the dashboard makes it easier for a system administrator to monitor server activity, identify potential security concerns, and evaluate overall system health.
