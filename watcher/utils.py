from datetime import datetime

def log(msg, logfile):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
