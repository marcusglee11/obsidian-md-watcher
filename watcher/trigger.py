import os
import time
import subprocess
from .config import WATCH_FOLDER
from .utils import log

WATCHER_SCRIPT = "python -m watcher.vault_committer"
LOG_FILE = os.path.join(WATCH_FOLDER, "trigger.log")

def main():
    log("🟢 File trigger started", LOG_FILE)
    seen = set(os.listdir(WATCH_FOLDER))

    while True:
        time.sleep(3)
        current = set(os.listdir(WATCH_FOLDER))
        new_md = [f for f in current - seen if f.endswith(".md")]

        if new_md:
            log(f"📄 New .md file(s) detected: {new_md}", LOG_FILE)
            try:
                subprocess.Popen(WATCHER_SCRIPT, shell=True)
                log("🚀 Triggered vault_committer", LOG_FILE)
            except Exception as e:
                log(f"❌ Failed to launch watcher: {e}", LOG_FILE)
            time.sleep(30)
        seen = current

if __name__ == "__main__":
    main()
