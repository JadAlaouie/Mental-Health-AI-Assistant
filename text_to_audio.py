import pyttsx3

class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self, voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_available_voices(self):
        voices = self.engine.getProperty('voices')
        
        for i, voice in enumerate(voices):
            
            language = voice.languages[0] if voice.languages else 'Unknown language'
            
            print(f'{i + 1} {voice.name} {voice.age}: {language} ({voice.gender}) [{voice.id}]')

    def text_to_speech(self, text: str, save: bool = False, file_name = 'output.mp3'):
        self.engine.say(text)
        print("I am speaking...")
        if save:
            self.engine.save_to_file(text, file_name)
        self.engine.runAndWait()
    
if __name__ == '__main__':
    tts = TextToSpeech(None, 200, 1.0)
    tts.text_to_speech("I'm so sorry to hear that you're feeling that way. Please know that you are not alone, and there are people who care about you deeply. It takes a lot of courage to admit when we're struggling, and I want you to know that I'm here to support you. First and foremost, please know that you are not a burden, and your life is valuable. If you're feeling suicidal, please reach out to a crisis helpline or a trusted adult for support. You can call the Lebanon National Suicide Prevention Lifeline at pace to talk about your feelings. You can find a list of mental health professionals in Lebanon through the Lebanese Psychological Association or the Lebanese Psychiatric Society.Remember, you are not alone, and there is help available. You are strong, capable, and deserving of love and support.")