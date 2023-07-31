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




source_folder_Label=tk.Label(window, text="Source Folder: "); source_folder_Label.pack()
source_folder_Textbox=tk.Text(window); source_folder_Textbox.pack()

destination_folder_Label=tk.Label(window, text="Destination Folder: "); destination_folder_Label.pack()
destination_folder_Textbox=tk.Text(window); destination_folder_Textbox.pack()


window.mainloop()
