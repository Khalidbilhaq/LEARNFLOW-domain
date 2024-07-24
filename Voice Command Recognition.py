

import os
import speech_recognition as sr
import webbrowser

# Function to recognize speech from microphone input
def recognize_speech_from_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing...")
        audio_data = r.listen(source)
    
    try:
        print("Recognized...")
        command = r.recognize_google(audio_data)
        print(f"Command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

# Main function
def cr():
    # Recognize speech from microphone input
    command = recognize_speech_from_microphone()
    
    # Perform actions based on recognized command
    if command:
        # Your logic to perform actionable tasks based on the recognized command
        print("Performing action based on command:", command)

        if 'hey google' in command:
            webbrowser.open("https://google.com/")
            print("Hello how can i assist you")

        elif 'open github' in command:
            webbrowser.open("https://youtube.com/")

        elif 'open calculator'in command:
            os.system("calc.exe")
            print("Calculator opened")
        
        else:
            print("Command not recognized.")
    else:
        print("Please try again.")

# Run the main function
cr()
