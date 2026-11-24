import re
from collections import Counter
from pathlib import Path

LOG_FILE = Path("/var/log/fail2ban.log")

EVENT_PATTERN = re.compile(
    r"\[([^\]]+)\]\s+(Found|Ban|Unban)\s+([0-9a-fA-F:.]+)"
)


def collect_fail2ban_events(limit=1000):
    events = []

    try:
        with LOG_FILE.open("r", encoding="utf-8", errors="replace") as log:
            lines = log.readlines()[-limit:]

        for line in lines:
            match = EVENT_PATTERN.search(line)

            if match:
                events.append({
                    "jail": match.group(1),
                    "action": match.group(2),
                    "ip": match.group(3),
                    "message": line.strip(),
                })

    except (PermissionError, FileNotFoundError) as error:
        print(f"Unable to read Fail2ban logs: {error}")

    return events


def summarize_fail2ban_events(events):
    counts = Counter(event["action"] for event in events)
    jails = Counter(event["jail"] for event in events)

    return {
        "found": counts["Found"],
        "bans": counts["Ban"],
        "unbans": counts["Unban"],
        "total": len(events),
        "jails": dict(jails),
    }
