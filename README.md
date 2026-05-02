# 📂 File Automator (Python)

A practical automation utility built to streamline directory management. This script scans a source folder for specific file types and migrates them to a designated destination, ensuring a clean and organized workspace.

## 🚀 Features
* **Targeted Migration:** Automatically identifies and moves .jpg files (easily extensible to other formats).
* **Dynamic Directory Handling:** Uses os.path.join to ensure compatibility across Windows, macOS, and Linux.
* **Smart Folder Creation:** Automatically detects if the destination folder exists; if not, it creates it on the fly.
* **Real-time Feedback:** Provides console output for every file moved.

## 🛠️ How It Works
1. **User Input:** Prompts for the absolute paths of the Source and Destination folders.
2. **Safety Check:** Verifies and creates the destination directory if missing.
3. **Execution:** Moves matching files using shutil.move for a fast and safe transfer.

## 📝 Future Roadmap
[ ] Multi-format Support: Modify the script to move .png, .pdf, or .docx files simultaneously.

[ ] File Renaming: Add a timestamp to files during the move to avoid overwriting files with the same name.

[ ] Logging: Generate a session log file (move_log.txt) of all moved items for audit purposes.

[ ] GUI Implementation: Build a simple interface using Tkinter for easier folder selection.

## ⚙️ Installation & Usage
1. Clone the repository:
git clone https://github.com/tushardaga69-official/CodeAlpha_File-Automator-Python

2. Run the script:
python file_mover.py
