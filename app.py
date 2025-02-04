import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class MediaTranscriberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Transcriber")
        
        self.label = tk.Label(root, text="Select a folder containing media files")
        self.label.pack(pady=10)
        
        self.select_btn = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_btn.pack(pady=5)
        
        self.transcribe_btn = tk.Button(root, text="Start Transcription", command=self.start_transcription)
        self.transcribe_btn.pack(pady=5)
        
        self.folder_path = None

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            messagebox.showinfo("Folder Selected", f"Selected folder: {self.folder_path}")

    def start_transcription(self):
        if not self.folder_path:
            messagebox.showwarning("No Folder", "Please select a folder first!")
            return
        
        media_files = [f for f in os.listdir(self.folder_path) if f.endswith(('.mp3', '.wav', '.mp4'))]

        if not media_files:
            messagebox.showwarning("No Media Files", "No media files found in the selected folder.")
            return

        for file in media_files:
            file_path = os.path.join(self.folder_path, file)
            subprocess.run(["python", "transcribe.py", file_path])

        messagebox.showinfo("Transcription Complete", "Transcription has been saved in the output folder.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MediaTranscriberApp(root)
    root.mainloop()