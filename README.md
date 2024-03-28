# Whisper Transcription Front-end

<img title="" src="file:///home/admin/projects/active/Whisper%20Frontend/README/first_start.png" alt="Alt text" data-align="inline" width="525">

---

## Program Functions

#### Configuration File

- Stores latest program global variables to a configuration file
  
  - Config variables are retrieved at program start up
  
  - Config variables are changed after every global variable update

- Contents
  
  - **AUDIO_INPUT_FOLDER:** Most recent input directory
  
  - **TRANSCRIPTION_OUTPUT_FOLDER:** Most recent output directory

#### Choose Input Directory

- Button: opens file picker dialog when clicked
  
  - Saves selected directory as a global variable
  
  - ![file picker](/home/admin/projects/active/Whisper%20Frontend/README/file_picker.png)

- Label: Prints the input folder variable, in addition to the input file is the automatic file selection flag is checked

#### Choose Input File

- Allows the user to select the desired input file when button is pressed

- When "Choose File Automatically" is checked, this option is not available
  
  - Automatic file selection is based on which file was most recently modified in the input directory

- Label states what the currently selected input file is

#### Choose Output Directory

- Allows the user to select their desired output directory

- "Create Output Directory Automatically" creates an output directory based off of the name of the input file within the input directory

- Label lists the current output directory label

#### Transcribe

- Utilizes the openai-whisper package to process and transcribe the desired input file

- Transcription results are saved to .json, .srt, .tsv, .txt, and .vtt file formats

#### Transcription Progress Bar

- Progress bar is based on the transcription progress

- The transcription progress information is piped from openai-whisper into a progress bar method

#### View Output Files

- When transcription is complete, the button allows the user to open the output directory of the latest transcription task

#### Open Subtitle Edit

- Opens the Subtitle Edit program if installed

- Opens the Subtitle Edit download page if the program is not installed

#### UI Scaling

- UI scaling options of 80-120

- Program window is automatically resized based on UI scaling

- <img src="file:///home/admin/projects/active/Whisper%20Frontend/README/120_Scaling.png" title="" alt="120% UI Scaling" width="590">



   
