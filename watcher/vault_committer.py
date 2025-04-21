import os
import shutil
import time
import subprocess
from datetime import datetime
from .config import WATCH_FOLDER, VAULT_FOLDER, ARCHIVE_FOLDER, INDEX_NOTE, LOG_FILE
from .utils import log

def append_to_index(filename, folder_label):
    relative_link = f"[[{filename}]]"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tag_map = {
        "Self-Continuity": "#self-continuity #identity #reflection",
        "Belief Shifts": "#belief #update #thought",
        "Opportunity Mapper": "#opportunity #strategy",
        "Insight Synthesizer": "#insight #synthesis",
        "Philosophical Stances": "#philosophy #perspective",
        "Emotional Logs": "#emotion #pattern",
        "Tool Design": "#tool #ai #architecture"
    }
    tags = tag_map.get(folder_label, "")
    entry = f"- {timestamp} — {relative_link} (folder: {folder_label}) {tags}\n"

    section_header = f"## {folder_label}"
    try:
        if not os.path.exists(INDEX_NOTE):
            with open(INDEX_NOTE, "w", encoding="utf-8") as f:
                f.write("# ChatGPT Summary Index\n\n## 🔥 Recent or Important\n\n")

        with open(INDEX_NOTE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        found_section = False
        for line in lines:
            new_lines.append(line)
            if line.strip() == section_header:
                found_section = True
                new_lines.append(entry)

        if not found_section:
            new_lines.append(f"\n{section_header}\n\n")
            new_lines.append(entry)

        with open(INDEX_NOTE, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

        log(f"✅ Index updated under section: {folder_label}", LOG_FILE)
    except Exception as e:
        log(f"❌ ERROR updating summary index: {e}", LOG_FILE)

def process_file(file_path):
    filename = os.path.basename(file_path)
    target_path = os.path.join(VAULT_FOLDER, filename)
    archive_path = os.path.join(ARCHIVE_FOLDER, filename)

    log(f"📦 Processing: {filename}", LOG_FILE)

    if not os.path.exists(file_path):
        log(f"⚠️ File not found: {file_path}", LOG_FILE)
        return

    try:
        shutil.move(file_path, target_path)
        log(f"✅ File moved to vault: {target_path}", LOG_FILE)
    except Exception as e:
        log(f"❌ Move failed: {e}", LOG_FILE)
        return

    try:
        subprocess.run(["git", "-C", VAULT_FOLDER, "add", filename], check=True)
        subprocess.run(["git", "-C", VAULT_FOLDER, "commit", "-m",
                        f"[Auto] Committed ChatGPT summary: {filename} at {datetime.now().isoformat()}"], check=True)
        log(f"✅ Git commit: {filename}", LOG_FILE)
    except subprocess.CalledProcessError as e:
        log(f"❌ Git commit error: {e}", LOG_FILE)
        return

    try:
        shutil.copy(target_path, archive_path)
        log(f"📁 Archived to: {archive_path}", LOG_FILE)
    except Exception as e:
        log(f"⚠️ Archive copy failed: {e}", LOG_FILE)

    folder_label = "General"
    if "belief" in filename.lower(): folder_label = "Belief Shifts"
    elif "continuity" in filename.lower(): folder_label = "Self-Continuity"
    elif "opportunity" in filename.lower(): folder_label = "Opportunity Mapper"
    elif "emotion" in filename.lower(): folder_label = "Emotional Logs"
    elif "philosophy" in filename.lower(): folder_label = "Philosophical Stances"
    elif "insight" in filename.lower(): folder_label = "Insight Synthesizer"
    elif "tool" in filename.lower(): folder_label = "Tool Design"

    append_to_index(filename, folder_label)

def main():
    try:
        files = [f for f in os.listdir(WATCH_FOLDER) if f.endswith(".md")]
        for file in files:
            full_path = os.path.join(WATCH_FOLDER, file)
            process_file(full_path)
    except Exception as e:
        log(f"❌ Loop error: {e}", LOG_FILE)

if __name__ == "__main__":
    main()
