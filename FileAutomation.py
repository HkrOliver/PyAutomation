import os  
import time
import shutil
import io
from watchdog.observers import Observer ; from watchdog.events import FileSystemEventHandler

def Get_Paths():
    global source_folder
    global destination_folder
    if os.path.exists("Source_Folder.txt"):
        with io.open("Source_Folder.txt", "r", encoding="utf-8") as file:
            source_folder=file.read()
    else:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        folder_name = "DownloadedFiles"
        source_folder = os.path.join(script_directory, folder_name)

    if os.path.exists("Destination_Folder.txt"):
        with io.open("Destination_Folder.txt", "r", encoding="utf-8") as file:
            destination_folder=file.read() 
    else:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        folder_name = "FolderToMoveTo"
        source_folder = os.path.join(script_directory, folder_name)

Get_Paths()

file_types = {
    ".txt": "Text File(s)",
    ".pdf": "PDF(s)",
    ".jpg": "Image(s)",
    ".gif": "Animated Image(s)",
    ".docx": "Word Document(s)",
    ".xlsx": "Excel Spreadsheet(s)",
    ".pptx": "PowerPoint Presentation(s)",
    ".psd": "Photoshop(s)",
    ".ps1": "Powershell Script(s)",
    ".bat": "Batch File(s)",
    ".py": "Python Script(s)",
    ".cs": "C# File(s)",
    ".json": "JSON File(s)",
    ".html": "HTML File(s)",
    ".css": "CSS FIle(s)",
    ".wav": "Audio File(s)",
}

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            file_extension = os.path.splitext(file_path)[1]
            destination = file_types.get(file_extension.lower(), "Other")
            destination_folder_path = os.path.join(destination_folder, destination)
            if not os.path.exists(destination_folder_path):
                os.makedirs(destination_folder_path)
            
            # Wait for 5 seconds to allow the file to be fully downloaded
            time.sleep(5)
            
            try:
                shutil.move(file_path, os.path.join(destination_folder_path, os.path.basename(file_path)))
            except FileNotFoundError:
                # If the file is still not available, ignore the event
                pass

if __name__ == "__main__":
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, source_folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
