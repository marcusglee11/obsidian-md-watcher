# 🗂️ Obsidian Markdown Watcher

**Obsidian Markdown Watcher** is a lightweight automation tool that monitors your Downloads folder for new `.md` files — such as those exported from ChatGPT — and automatically commits them into your Obsidian vault with Git tracking, folder-based categorization, and an indexed summary note.

---

## ✅ Purpose

This tool helps researchers, writers, and AI power users streamline the export and archival of ChatGPT conversations into a personal knowledge base using [Obsidian](https://obsidian.md).

It turns exported markdown files into:
- Git-tracked vault entries
- Categorized notes with wiki-style links
- Summary-indexed entries grouped by topic
- Archived backups in a processed folder

---

## 🔍 Scope

This tool is designed for:
- **Personal use** on a local Windows system
- **Markdown files exported from ChatGPT**
- **Integration with Obsidian vaults** stored locally
- No internet dependencies or API calls

> ✅ Works fully offline  
> ✅ Safe for private/local note workflows  
> ✅ Designed for long-term archival and self-curation

---

## 🚀 Features

- ✅ Watches your Downloads folder for `.md` files
- ✅ Automatically moves them to your Obsidian vault
- ✅ Commits changes with Git (local only)
- ✅ Updates a structured index note with wiki links and tags
- ✅ Categorizes entries by folder label (e.g., `Self-Continuity`, `Belief Shifts`)
- ✅ Archives a backup copy in a processed folder
- ✅ Logs every action for audit and debugging

---

## 🧰 Installation

### Step 1: Unzip
Unzip this project to a clean directory, e.g.:
```
C:/Users/YOUR_USERNAME/Projects/obsidian-md-watcher
```

### Step 2: Install the Python Package
In the terminal (PowerShell or CMD):
```bash
cd C:/Users/YOUR_USERNAME/Projects/obsidian-md-watcher
pip install -e .
```

### Step 3: Configure Your Paths
Edit `watcher/config.py` and replace the default placeholders:
```python
WATCH_FOLDER = "C:/Users/YOUR_USERNAME/Downloads"
VAULT_FOLDER = "C:/Users/YOUR_USERNAME/Obsidian/YourVault"
```

---

## 💻 Manual Usage

Run this to start watching for exported `.md` files:
```bash
python -m watcher.trigger
```

Whenever a markdown file is dropped into your Downloads folder:
- The script will trigger
- Move the file to your Obsidian vault
- Commit it via Git
- Append an index entry to your vault’s summary

---

## ⚙️ Automate on Startup (Optional)

1. Open Task Scheduler
2. Create a new **Basic Task**
3. Set Trigger: **When I log on**
4. Set Action:  
   Program/script:
   ```bash
   python
   ```
   Add arguments:
   ```
   -m watcher.trigger
   ```
   Start in:
   ```
   C:/Users/YOUR_USERNAME/Projects/obsidian-md-watcher
   ```

---

## 🧠 How to Instruct ChatGPT to Generate Obsidian-Ready Summaries

When using ChatGPT, type:

### 🔹 Generic Save Command
```
*obsidian
```

ChatGPT will:
- Choose folder + title automatically
- Export a full conversation summary
- Format it for Obsidian
- Include a shareable link to the original chat

### 🔹 Custom Save Command
```
*obsidian:self-continuity note:Why I Resist Vulnerability
```

This lets you specify:
- Folder (for categorization)
- Note title (for the filename and index entry)

---

## 📚 Output Format

### Top of Every `.md` Note
```markdown
🔗 Source: https://chat.openai.com/share/abc123xyz
```

### In the Summary Index
```markdown
## Self-Continuity
- 2025-04-21 16:44:01 — [[Why I Resist Vulnerability]] (folder: Self-Continuity) #identity #reflection
```

---

## 🔐 Security Notice

This tool processes and indexes personal ChatGPT summaries **locally**.

- **Do NOT push your Obsidian vault** or any `*.md` files to GitHub unless redacted
- `config.py` contains your personal paths — keep it private
- Git is used for local versioning only
- You can optionally encrypt your vault with tools like [Cryptomator](https://cryptomator.org)

---

## 📄 License

MIT License – Free to use, fork, extend, and automate.

---

## 🤝 Contributions

Pull requests welcome! Help improve multi-platform support, tagging logic, or community vault examples.
