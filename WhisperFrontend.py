import tkinter
import os
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image
import sys

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Transcription Automator")
        self.geometry(f"{1100}x{760}")
        
        self.logo = ImageTk.PhotoImage(file="img/icon_4.png", master=self)
        self.iconphoto(False, self.logo)
        #self.iconbitmap('@/home/admin/Whisper Frontend/logo_3.xpm')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=0)

        # ----- ----- -----Selection Frame for Choosing the Directories and Files for Execution ----- ----- -----
        self.selection_frame = customtkinter.CTkFrame(self)
        self.selection_frame.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.selection_frame_group = customtkinter.CTkLabel(master=self.selection_frame, text="Choose Your Files/Folders")
        self.selection_frame_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="n")
        # ----- Input Directory Button and Label Group -----
        self.inputDirectoryButton = customtkinter.CTkButton(master=self.selection_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Choose Input Directory')
        self.inputDirectoryButton.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.inputDirectoryLabel = customtkinter.CTkLabel(master=self.selection_frame, fg_color="transparent", text_color=("gray10", "#DCE4EE"), text='Really')
        self.inputDirectoryLabel.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="w")
        # ----- Input File Button and Label Group -----
        self.inputFileButton = customtkinter.CTkButton(master=self.selection_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Choose Input File')
        self.inputFileButton.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.inputFileLabel = customtkinter.CTkLabel(master=self.selection_frame, fg_color="transparent", text_color=("gray10", "#DCE4EE"), text='Test')
        self.inputFileLabel.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="w")
        # ----- Output Directory Button and Label Group -----
        self.outputDirectoryButton = customtkinter.CTkButton(master=self.selection_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Choose Output Directory')
        self.outputDirectoryButton.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.outputDirectoryLabel = customtkinter.CTkLabel(master=self.selection_frame, fg_color="transparent", text_color=("gray10", "#DCE4EE"), text='Test')
        self.outputDirectoryLabel.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="w")
        # ----- Checkbox Options for the Selection Frame
        self.checkbox_0 = customtkinter.CTkCheckBox(master=self.selection_frame, text='Choose File Automatically')
        self.checkbox_0.grid(row=4, column=0, pady=20, padx=20, sticky="n")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.selection_frame, text='Create Output Directory Automatically')
        self.checkbox_1.grid(row=4, column=1, pady=20, padx=20, sticky="w")



        # ----- ----- ----- ----- Main frame with execution buttons and labels, no options except for a button to reset the program status ----- ----- ----- -----
        self.transcribeButton = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Transcribe')
        self.transcribeButton.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.transcribeLabel = customtkinter.CTkLabel(master=self, fg_color="transparent", text_color=("gray10", "#DCE4EE"), text='Ready to Transcribe')
        self.transcribeLabel.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="w")

        self.viewOutputButton = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='View Output Files')
        self.viewOutputButton.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.viewOutputLabel = customtkinter.CTkLabel(master=self, fg_color="transparent", text_color=("gray10", "#DCE4EE"), text='Transcription Complete')
        self.viewOutputLabel.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="w")

        self.openSEButton = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Open Subtitle Edit')
        self.openSEButton.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.openSELabel = customtkinter.CTkLabel(master=self, fg_color="transparent", text_color=("gray10", "#DCE4EE"), text='Subtitle Edit Not Installed')
        self.openSELabel.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="w")

        self.resetStatusButton = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Reset Status')
        self.resetStatusButton.grid(row=4, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.resetStatusLabel = customtkinter.CTkLabel(master=self, fg_color="transparent", text_color=("gray10", "#DCE4EE"), text='Reset File Locations')
        self.resetStatusLabel.grid(row=4, column=1, padx=(20, 20), pady=(20, 20), sticky="w")


if __name__ == "__main__":
    print(os.getcwd())
    app = App()
    app.mainloop()
    
