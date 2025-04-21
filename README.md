# 🗂️ Obsidian Markdown Watcher

**Obsidian Markdown Watcher** is a lightweight automation tool that monitors your Downloads folder for new `.md` files — such as those exported from ChatGPT — and automatically commits them into your Obsidian vault with Git tracking, folder-based categorization, and an indexed summary note.

---

## ✅ Purpose

This tool helps researchers, writers, and AI power users streamline the export and archival of ChatGPT conversations into a personal knowledge base using Obsidian.

It turns exported markdown files into:
- Version-controlled Git commits
- Indexed entries by topic (e.g., #belief, #identity)
- Appended summary links inside an `Index.md` file
- Archival backup copies in a designated subfolder

---

## 🔍 Scope

This tool is designed for:
- Local use on Windows (Python 3.10+)
- Markdown files exported from ChatGPT or other apps
- Obsidian vaults stored on your local filesystem

---

## 🚀 Features

- ✅ Watches your Downloads folder for `.md` files
- ✅ Automatically moves them to your Obsidian vault
- ✅ Commits changes with Git
- ✅ Updates a structured index note with wiki links + tags
- ✅ Categorizes entries by folder label (e.g., `Self-Continuity`, `Belief Shifts`)
- ✅ Archives a backup copy in a separate folder

---

## 🧰 Installation

```bash
git clone https://github.com/YOUR_USERNAME/obsidian-md-watcher.git
cd obsidian-md-watcher
pip install -e .
```

Make sure `python` is in your PATH and `git` is installed.

---

## ⚙️ Configuration

Edit your paths in `obsidian_md_watcher/watcher/config.py`:

```python
WATCH_FOLDER = "C:/Users/YOUR_USERNAME/Downloads"
VAULT_FOLDER = "C:/Users/YOUR_USERNAME/Obsidian/YourVault"
```

The script will also create:
- `processed/` folder inside `Downloads` (for archive copies)
- `ChatGPT Summary Index.md` inside your vault

---

## 💻 Usage

### Manual Run:
```bash
python -m obsidian_md_watcher.watcher.trigger
```

This will watch for new `.md` files in your Downloads folder. When one is detected:
- It triggers the vault processor
- Moves the file to your vault
- Commits it
- Updates the index

---

## 🔄 Automation (Optional)

To start on boot:
1. Create a `.bat` file:
   ```bat
   start "" python C:\Users\YOUR_USERNAME\obsidian-md-watcher\obsidian_md_watcher\watcher\trigger.py
   ```
2. Add it to Windows Task Scheduler → "At logon"

---

## 📚 Output Format

Every committed `.md` file includes:
```markdown
🔗 Source: https://chat.openai.com/share/abc123xyz
```

Index entries look like:
```markdown
## Self-Continuity
- 2025-04-21 16:44:01 — [[Grief Reflection Note]] (folder: Self-Continuity) #self-continuity #identity
```

---

## 🤝 Contributions

PRs welcome! Please open an issue or suggestion to expand categorization, support `.env` config, or multi-platform compatibility.

---

## 📜 License

MIT License — free to use, fork, and extend.
