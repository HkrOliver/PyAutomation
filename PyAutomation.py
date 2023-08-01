import io # Reading and Writing to text files
import os # Checking if paths exists
import subprocess # run the automation script.
import tkinter as tk, tkinter # Making the GUI
from tkinter import filedialog # For the user to select the source and destination and source folders

window = tk.Tk(); window.title("PyAutomation"); window.geometry("400x400")

source_folder=""; destination_folder=""

def Get_Path(button_pressed):
    if button_pressed == "source_folder_Button":
        source_folder=filedialog.askdirectory()
    
    if button_pressed=="destination_folder_Button":
        destination_folder=filedialog.askdirectory()

def save_folders():
    source_folder = source_folder_Textbox.get("1.0", "end-io")
    destination_folder = destination_folder_Textbox.get("1.0", "end-io")
    window.destroy()

source_folder_Label = tk.Label(window, text="Source Folder:")
source_folder_Label.grid(row=0, column=0, padx=10, pady=10)

source_folder_Textbox = tk.Text(window, width=20, height=2)
source_folder_Textbox.grid(row=0, column=1, padx=10, pady=10)

source_folder_Browse = tk.Button(window, text="Browse", width=20, height=2)
source_folder_Browse.grid(row=1, column=1, padx=50, pady=5)  # Adjust the 'pady' value

destination_folder_Label = tk.Label(window, text="Destination Folder:")
destination_folder_Label.grid(row=2, column=0, padx=10, pady=10)  # Move to the next row

destination_folder_Textbox = tk.Text(window, width=20, height=2)
destination_folder_Textbox.grid(row=2, column=1, padx=10, pady=10)

destination_folder_Browse = tk.Button(window, text="Browse", width=20, height=2)
destination_folder_Browse.grid(row=3, column=1, padx=50, pady=5)  # Adjust the 'pady' value

save_button = tk.Button(window, text="Save Folders", command=save_folders)
save_button.grid(row=4, columnspan=2, padx=10, pady=10)



window.mainloop()
