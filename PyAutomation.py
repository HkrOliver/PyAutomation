import io # Reading and Writing to text files
import os # Checking if paths exists
import subprocess # run the automation script.
import psutil
import platform
import tkinter as tk, tkinter # Making the GUI
from tkinter import filedialog 

window = tk.Tk(); window.title("PyAutomation"); window.geometry("400x400")

source_folder=""; destination_folder=""; folder_path=""

def Get_Path(button_pressed):
    if button_pressed == "source_folder_Browse":
        folder_path=filedialog.askdirectory()
        source_folder_Textbox.delete("1.0", "end")
        source_folder_Textbox.insert("1.0", folder_path)
    
    if button_pressed=="destination_folder_Browse":
        folder_path=filedialog.askdirectory()
        destination_folder_Textbox.delete("1.0", "end")
        destination_folder_Textbox.insert("1.0", folder_path)

def Load_Paths():
    if os.path.exists("Source_Folder.txt"):
        with io.open("Source_Folder.txt") as file:
            source_folder=file.read()
            source_folder_Textbox.delete("1.0", "end")
            source_folder_Textbox.insert("1.0", source_folder)
    
    if os.path.exists("Destination_Folder.txt"):
        with io.open("Destination_Folder.txt") as file:
            destination_folder=file.read()
            destination_folder_Textbox.delete("1.0", "end")
            destination_folder_Textbox.insert("1.0", destination_folder)

def Clear_Paths():
    source_folder_Textbox.delete("1.0", "end"); destination_folder_Textbox.delete("1.0", "end")

def Save_Folders():
    source_folder = source_folder_Textbox.get("1.0", "end-io")
    destination_folder = destination_folder_Textbox.get("1.0", "end-io")
    
    with io.open("Source_Folder.txt") as file:
        file.write(source_folder)

    with io.open("Destination_Folder") as file:
        file.write(destination_folder)

def Start_Automation():
    subprocess.run(["python", "FileAutomation.py"], shell=True)

def Stop_Automation():
    if platform.system() == "Windows":
        subprocess.run(["taskkill", "/F", "/IM", "FileAutomation.py"])
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        subprocess.run(["pkill", "-f", "FileAutomation.py"])

source_folder_Label = tk.Label(window, text="Source Folder:")
source_folder_Label.grid(row=0, column=0, padx=10, pady=10)

source_folder_Textbox = tk.Text(window, width=20, height=2)
source_folder_Textbox.grid(row=0, column=1, padx=10, pady=10)
 
source_folder_Browse = tk.Button(window, text="Browse", width=20, height=2, command=lambda: Get_Path("source_folder_Browse"))
source_folder_Browse.grid(row=1, column=1, padx=50, pady=5)  

destination_folder_Label = tk.Label(window, text="Destination Folder:")
destination_folder_Label.grid(row=2, column=0, padx=10, pady=10)  

destination_folder_Textbox = tk.Text(window, width=20, height=2)
destination_folder_Textbox.grid(row=2, column=1, padx=10, pady=10)

destination_folder_Browse = tk.Button(window, text="Browse", width=20, height=2, command=lambda: Get_Path("destination_folder_Browse"))
destination_folder_Browse.grid(row=3, column=1, padx=50, pady=5)

save_button = tk.Button(window, text="Save Folders", command=Save_Folders)
save_button.grid(row=4, columnspan=4, padx=10, pady=10)

clear_button = tk.Button(window, text="Clear", command=Clear_Paths)
clear_button.grid(row=4,columnspan=1, padx=10, pady=10)

automate_Button = tk.Button(window, text="Automate", command=Automation)
automate_Button.grid(row=4, columnspan=2, padx=10, pady=10)

window.mainloop()
