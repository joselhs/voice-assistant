import os
import speech_recognition as sr
from elevenlabs import play
from elevenlabs.client import ElevenLabs


# set_api_key(os.environ['ELEVEN_API_KEY'])

class AudioInterface:

    def listen(self) -> str:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Di algo!")
            audio = recognizer.listen(source)

        
        
        text = recognizer.recognize_whisper_api(
            audio,
            api_key=os.environ['OPENAI_API_KEY']
        )

        return text


    def speak(self, text):
        client = ElevenLabs(
            api_key=os.environ['ELEVEN_API_KEY'], # Defaults to ELEVEN_API_KEY
        )

        audio = client.generate(
            text=text,
            voice='Sara',
            model="eleven_multilingual_v2",
        )

        play(audio)

