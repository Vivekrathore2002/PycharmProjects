# Text to Speech Command for windows is
import os
if name == '__main__':
    print("RoboSpeaker...")
    print("Write :q to exit")
    try:
        while True:
            txt = input("Enter anything to speak it:  ")
            if txt == ":q":
                cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye Bye')"
                os.system(cmd)
                break
            cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{txt}')"
            os.system(cmd)
    except Exception as e :
        print(f"Error is -> {e}")

