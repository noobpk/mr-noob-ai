import speech_recognition
import pyttsx3
import datetime
import pyfiglet

#Define
ascii_banner = pyfiglet.figlet_format("Mr.Noob!!")
noob_listen = speech_recognition.Recognizer()
noob_speech = pyttsx3.init()

#Variable
version = "1.0"
owner = "Master Pk"
mr_noob_name = "Mr.Noob"
dt = datetime.datetime.now()
if dt.time() < datetime.time(6):
    noob_brain = f"Good Night {owner}!!"
elif dt.time() < datetime.time(12):
    noob_brain = f"Hello {owner}!! Have a good day."
elif dt.time() < datetime.time(18):
    noob_brain = f"Good Afternoon {owner}!!"
else:
    noob_brain = f"Good Evening {owner}!!"

def new_run():
    print(ascii_banner)
    print("Mr.Noob: " + noob_brain)
    noob_speech.say(noob_brain)
    noob_speech.runAndWait()

def main():
    #using voice
    while True:
        # with speech_recognition.Microphone() as mic:
        #         print("Mr.Noob: I'm Listening")
        #         voice = noob_listen.listen(mic)
        # print("Mr.Noob: ....")

    #using input form keyboard
        
        try:
            #you = noob_listen.recognize_google(voice)
            you = input('You: ')
            print("Mr.Noob: ....")  
        except:
            you = ""

        # print("You: " + you)

        #brain of Mr.Noob
        if you == "":
            noob_brain = "I can't hear you, try again"
        elif "hello" in you:
            noob_brain = "Hello Master"
        elif "name" in you:
            noob_brain = f"My name {mr_noob_name}"
        elif "bye" in you:
            noob_brain = "Bye Master"
            print("Mr.Noob: " + noob_brain)
            noob_speech.say(noob_brain)
            noob_speech.runAndWait()
            break
        else:
            noob_brain = f"Sorry, {owner}. I need learn more.!!"

        print("Mr.Noob: " + noob_brain)
        noob_speech.say(noob_brain)
        noob_speech.runAndWait()

if __name__ == "__main__":
    new_run()
    main()