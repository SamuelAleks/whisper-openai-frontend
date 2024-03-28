# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library


# import filedialog module
import os
import sys
import xdg
import glob
import tqdm
import whisper
import pathlib
import threading
import subprocess
import configparser
import customtkinter
from customtkinter import filedialog
from whisper.utils import get_writer
import tkinter as tk
from tkinter import filedialog as fd


# Function for opening the
# file explorer window
global AUDIO_INPUT_FOLDER
global AUDIO_FILENAME
global TRANSCRIPTION_OUTPUT_FOLDER
#AUDIO_INPUT_FOLDER = ""
#TRANSCRIPTION_OUTPUT_FOLDER = ""
CONFIG = "TranscriptionApplicationConfig.conf"

def loadVariables():
    file = CONFIG
    if (os.path.exists(file) == False):
        f = open(file, "w")
        AUDIO_INPUT_FOLDER = "C:/"
        TRANSCRIPTION_OUTPUT_FOLDER = "C:/"
        f.writelines(["C:/\n", "C:/"])
        f.close()
        return AUDIO_INPUT_FOLDER, TRANSCRIPTION_OUTPUT_FOLDER
    else:
        with open(file) as f:
            data = f.readlines()
            AUDIO_INPUT_FOLDER = data[0]
            TRANSCRIPTION_OUTPUT_FOLDER = data[1]
            f.close()
            return AUDIO_INPUT_FOLDER, TRANSCRIPTION_OUTPUT_FOLDER

def get_default_file_explorer():
    # Get the default file explorer's .desktop file
    try:
        output = subprocess.check_output("xdg-mime query default inode/directory", shell=True)
        # Decode the output from bytes to string and strip newlines
        file_explorer_desktop = output.decode('utf-8').strip()
        # Extract the actual name of the file explorer (before the .desktop extension)
        file_explorer = file_explorer_desktop.split('.')[0]
        return file_explorer
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return None

def open_file_explorer():
    file_explorer = get_default_file_explorer()
    if file_explorer:
        try:
            # Open the default file explorer
            subprocess.run([file_explorer])
        except Exception as e:
            print(f"Failed to open file explorer: {e}")

# Example usage


def chooseAudioDirectory(m):
    AUDIO_INPUT_FOLDER, TRANSCRIPTION_OUTPUT_FOLDER = loadVariables()
    root.withdraw()
    directory = filedialog.askdirectory(initialdir = AUDIO_INPUT_FOLDER, title = "Select a Folder") # Change label contents
    root.deiconify()


    list_of_files = glob.glob(directory + '/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getmtime)

    AUDIO_INPUT_FOLDER = latest_file.strip().replace("\\", "/")
    m.configure(text=AUDIO_INPUT_FOLDER)
    #AUDIO_INPUT_FOLDER = AUDIO_INPUT_FOLDER.replace("\\", "/")


    file = CONFIG
    with open(file, 'r') as f:
        data = f.readlines()
        data[0] = AUDIO_INPUT_FOLDER + '\n'
        f.close()
    with open(file, 'w') as f:
        f.writelines(data)
        f.close()


def chooseTranscriptionDirectory(m):
    AUDIO_INPUT_FOLDER, TRANSCRIPTION_OUTPUT_FOLDER = loadVariables()
    root.withdraw()
    directory = filedialog.askdirectory(initialdir=TRANSCRIPTION_OUTPUT_FOLDER, title="Select a Folder")

    root.deiconify()
    # Change label contents
    #label3.configure(text=directory)
    TRANSCRIPTION_OUTPUT_FOLDER = directory.strip().replace("\\", "/")
    m.configure(text=TRANSCRIPTION_OUTPUT_FOLDER)

    #TRANSCRIPTION_OUTPUT_FOLDER = TRANSCRIPTION_OUTPUT_FOLDER.replace("\\", "/")
    file = CONFIG
    with open(file, 'r') as f:
        data = f.readlines()
        data[1] = TRANSCRIPTION_OUTPUT_FOLDER + '\n'
        f.close()
    with open(file, 'w') as f:
        f.writelines(data)
        f.close()

def test1():
    print("hi")

class _CustomProgressBar(tqdm.tqdm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._current = self.n  # Set the initial value

    def update(self, n):
        super().update(n)
        self._current += n

        # Handle progress here
        progress = str(self._current) + "/" + str(self.total)
        print("Progress: " + progress)
        ratio = str(float(self._current)/float(self.total))
        print("ratio: " + ratio)
        progressBarValue = ratio*100
        lambda:progressBarUpdate(progressBarValue)
        progressbar.set((float(self._current)/float(self.total)))

def progressBarUpdate(m):
    progressbar['value']=4

def transcribe():
    import whisper.transcribe
    transcribe_module = sys.modules['whisper.transcribe']
    transcribe_module.tqdm.tqdm = _CustomProgressBar

    # testString = AUDIO_INPUT_FOLDER.strip().replace("/", "\\")
    testString = AUDIO_INPUT_FOLDER.strip()
    
    model = whisper.load_model("medium")
    result = model.transcribe(testString, language = "en", verbose = None, fp16=False)

    writer = get_writer("all", "")
    writer(result, TRANSCRIPTION_OUTPUT_FOLDER)
    #print(result["text"])
    progress = Label(window, justify="left", anchor="w", text = "Transcription Complete", height = 4)

def thread():
    threading.Thread(target=transcribe).start()

def toggle_subframe(var, subframe_1):
    if var.get() == 0:
        subframe_1.grid_forget()  # Hide subframe_1
    else:
        subframe_1.grid()  # Show subframe_1
        #frame.update()

def change_scaling_event(new_scaling: str, frame):
    # Store the current window position
    x_pos = root.winfo_x()
    y_pos = root.winfo_y()

    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)
    
    change_window_size(frame)


def change_window_size(frame):
    root.update_idletasks()  # Update window geometry

    # Get the new window size based on frame size
    new_width = frame.winfo_reqwidth()
    new_height = frame.winfo_reqheight()
    
    print("new_width: " + str(new_width))
    print("new_height: " + str(new_height))
    
    # Calculate the change in size
    delta_width = new_width - root.winfo_width()
    delta_height = new_height - root.winfo_height()
    
    print("delta_width: " + str(delta_width))
    print("delta_height: " + str(delta_height))
    
    root.after(0, lambda: adjust_window_position(new_width, new_height, delta_width, delta_height))


def adjust_window_position(new_width, new_height, delta_width, delta_height):

    root.update_idletasks() 

    # Get the current window position
    x = root.winfo_x()
    y = root.winfo_y()
    
    print("x: " + str(x))
    print("y: " + str(y))

    # Calculate the new position relative to the previous position
    new_x = x - delta_width // 2
    new_y = y - delta_height // 2

#    new_x = x - delta_width ^ 2
#    new_y = y
    
    print("new_x: " + str(new_x))
    print("new_y: " + str(new_y))
    # Adjust the window position to keep it in the same location
    root.geometry("{}x{}+{}+{}".format(new_width, new_height, new_x, new_y))

def main():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")

    global root
    root = customtkinter.CTk()
    root.geometry("1000x750")

    var = customtkinter.IntVar()

    frame = customtkinter.CTkFrame(master=root)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Use grid instead of pack
    frame.rowconfigure((0, 1), weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=12)
    frame.grid(pady=0, padx=0)

    subframe_1 = customtkinter.CTkFrame(master=frame)
    subframe_1.rowconfigure((0,1), weight=1)
    subframe_1.columnconfigure((0,1,2), weight=1)
    #subframe_1.grid(padx=(20, 0), pady=(20, 0))
    subframe_1.grid(pady=10, padx=10, columnspan=2, sticky="nsew")



    button_choose_input_directory = customtkinter.CTkButton(master=subframe_1, text = "Choose Input Directory", command=lambda: chooseAudioDirectory(input_folder_display_variable))
    button_choose_input_directory.grid(row=0, column=0, pady=12, padx=10, sticky="ew" )
    #button_choose_input_directory.pack(pady=12, padx = 10)

    input_folder_display_variable = customtkinter.CTkLabel(master=subframe_1, text=AUDIO_INPUT_FOLDER)
    input_folder_display_variable.grid(row=0, column=1, pady=12, padx=10, sticky="w")
    #input_folder_display_variable.pack(pady=12, padx=10)

    button_choose_input_file = customtkinter.CTkButton(master=subframe_1, text="Choose Input File")
    button_choose_input_file.grid(row=1, column=0, pady=12, padx=10, sticky="ew")

    input_file_display_variable = customtkinter.CTkLabel(master=subframe_1, text=AUDIO_FILENAME)
    input_file_display_variable.grid(row=1, column=1, pady=12, padx=10, sticky="w")
    #input_file_display_variable.pack(pady=12, padx=10)

    button_choose_output_directory = customtkinter.CTkButton(master=subframe_1, text = "Choose Output Directory", command=lambda: chooseTranscriptionDirectory(output_folder_label))
    button_choose_output_directory.grid(row=2, column=0, pady=12, padx=10, sticky="ew")
    #button_choose_output_directory.pack(pady=12, padx = 10)

    output_folder_label = customtkinter.CTkLabel(master=subframe_1, text=TRANSCRIPTION_OUTPUT_FOLDER)
    output_folder_label.grid(row=2, column=1, pady=12, padx=10, sticky="w")

    auto_file_checkbox = customtkinter.CTkCheckBox(subframe_1, text="Choose File Automatically")
    auto_file_checkbox.grid(row=3, column=0, pady=12, padx=10)

    create_output_dir_checkbox = customtkinter.CTkCheckBox(subframe_1, text="Choose File Automatically")
    create_output_dir_checkbox.grid(row=3, column=1, pady=12, padx=10, sticky = "w")



    button_transcribe = customtkinter.CTkButton(master=frame, text="Transcribe", command=thread)
    button_transcribe.grid(row=10, column=0, pady=12, padx = 10)
    
    global progressbar
    progressbar = customtkinter.CTkProgressBar(master=frame, mode='determinate')
    progressbar.grid(row=10, column=1, pady=10, padx=12, sticky="ew")
    #progressbar.set(0)

    view_output_files = customtkinter.CTkButton(master=frame, text="View Output Files")
    view_output_files.grid(row=11, column=0, pady=12, padx = 10)
    
    view_output_label = customtkinter.CTkLabel(master=frame, text="Transcription Complete")
    view_output_label.grid(row=11, column=1, pady=12, padx = 10, sticky="w")
    
    open_subtitle_edit = customtkinter.CTkButton(master=frame, text="Open Subtitle Edit")
    open_subtitle_edit.grid(row=12, column=0, pady=12, padx = 10)
    
    open_se_label = customtkinter.CTkLabel(master=frame, text="Subtitle Edit Not Installed")
    open_se_label.grid(row=12, column=1, pady=12, padx = 10, sticky="w")
    
    reset_status = customtkinter.CTkButton(master=frame, text="Reset Status")
    reset_status.grid(row=12, column=0, pady=12, padx = 10)
    
    checkbox = customtkinter.CTkCheckBox(frame, text="Hide Label", variable=var, command=lambda: toggle_subframe(var, subframe_1))
    checkbox.grid(row=13, column=0, pady=(10, 20))
    
    scaling_label = customtkinter.CTkLabel(frame, text="UI Scaling:", anchor="w")
    scaling_label.grid(row=13, column=1, padx=200, pady=(10, 20), sticky="e")

    scaling_optionmenu = customtkinter.CTkOptionMenu(frame, values=["80%", "90%", "100%", "110%", "120%"], command=lambda value: change_scaling_event(value, frame))
    scaling_optionmenu.grid(row=13, column=1, padx=20, pady=(10, 20), sticky="e")
    
    frame.grid_rowconfigure(14, minsize=15)
    
    change_window_size(frame)

    # Enter the main event loop
    root.mainloop()

if __name__ == "__main__":
    AUDIO_INPUT_FOLDER, TRANSCRIPTION_OUTPUT_FOLDER = loadVariables()
    fullAudioString = AUDIO_INPUT_FOLDER
    AUDIO_FILENAME = fullAudioString.rsplit('/', 1)[1]
    main()
