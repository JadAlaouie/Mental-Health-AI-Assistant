import speech_recognition as sr 
import pyttsx3

r = sr.Recognizer() 

def record_text():

    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration = 0.1)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText
            
        except sr.RequestError as error:
            print("Could not request results!")

        except sr.UnknownValueError:
            print("Unknown Error Occured!")
    return 

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return 

while(1):
    text = record_text()
    output_text(text)
    print("wrote text")