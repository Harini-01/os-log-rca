import re
import pandas as pd
from datetime import datetime

LOG_PATTERN = re.compile(
    r"(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+"
    r"(?P<host>\S+)\s+"
    r"(?P<program>[^\[]+)"
    r"(?:\[(?P<pid>\d+)\])?:\s+"
    r"(?P<message>.*)"
)

def parse_syslog(log_path, year=2024):
    rows = []

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = LOG_PATTERN.match(line)
            if not match:
                continue

            data = match.groupdict()

            ts_str = f"{data['timestamp']} {year}"
            timestamp = datetime.strptime(ts_str, "%b %d %H:%M:%S %Y")

            rows.append({
                "timestamp": timestamp,
                "host": data["host"],
                "program": data["program"].strip(),
                "pid": data["pid"],
                "message": data["message"]
            })

    return pd.DataFrame(rows)
