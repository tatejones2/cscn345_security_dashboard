import re
from collections import Counter
from pathlib import Path

LOG_FILE = Path("/var/log/auth.log")

PATTERNS = {
    "successful": re.compile(
        r"Accepted (?:publickey|password) for (\S+) from ([0-9a-fA-F:.]+)"
    ),
    "failed": re.compile(
        r"Failed (?:password|publickey) for (?:invalid user )?(\S+) from ([0-9a-fA-F:.]+)"
    ),
    "invalid_user": re.compile(
        r"Invalid user (\S+) from ([0-9a-fA-F:.]+)",
        re.IGNORECASE
    ),
}


def collect_ssh_events(limit=1000):
    events = []

    try:
        with LOG_FILE.open("r", encoding="utf-8", errors="replace") as log:
            lines = log.readlines()[-limit:]

        for line in lines:
            for event_type, pattern in PATTERNS.items():
                match = pattern.search(line)

                if match:
                    events.append({
                        "type": event_type,
                        "username": match.group(1),
                        "ip": match.group(2),
                        "message": line.strip(),
                    })
                    break

    except (PermissionError, FileNotFoundError) as error:
        print(f"Unable to read SSH logs: {error}")

    return events


def summarize_ssh_events(events):
    counts = Counter(event["type"] for event in events)

    return {
        "successful": counts["successful"],
        "failed": counts["failed"],
        "invalid_user": counts["invalid_user"],
        "total": len(events),
    }
