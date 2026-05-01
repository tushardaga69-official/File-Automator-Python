# Automated File Organizer (Image Mover)

A Python utility designed to automate the tedious task of sorting files. This script specifically identifies `.jpg` images in a cluttered source directory and moves them to a clean destination folder, creating the destination automatically if it doesn't already exist.

## 🚀 Features
*   **Path Validation:** Prompts the user for source and destination paths, handling extra spaces with `.strip()`.
*   **Auto-Folder Creation:** Checks if the destination folder exists and creates it if necessary using `os.makedirs`.
*   **Efficient Moving:** Uses the `shutil` library to move files safely across the file system.
*   **Real-time Feedback:** Prints a confirmation message for every file successfully moved.

## 🛠️ How It Works
1. The user inputs the directory path for the "Source" (where files are) and the "Destination" (where files should go).
2. The script iterates through every file in the source directory.
3. A logical check filters files ending in `.jpg`.
4. The script joins the file name with the directory paths to create a full system path.
5. Files are transferred, and a final success message is displayed.

## 💻 Tech Stack
*   **Language:** Python 3.x
*   **Libraries:** `os` (File system navigation), `shutil` (High-level file operations)

## 📂 Example Usage
```text
Enter the Source Folder Location: C:/Users/Downloads
Enter the Destination Folder Location: C:/Users/Pictures/Holiday_Photos
Moved: photo1.jpg
Moved: sunset.jpg
All .jpg files moved successfully...
