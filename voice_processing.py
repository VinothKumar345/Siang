# services/voice_processing.py

import speech_recognition as sr


def convert_voice_to_text(audio_file):

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:

        audio = recognizer.record(source)

    try:

        text = recognizer.recognize_google(audio)

        return {
            "transcript": text,
            "status": "success"
        }

    except sr.UnknownValueError:

        return {
            "transcript": "",
            "status": "could not understand audio"
        }

    except sr.RequestError:

        return {
            "transcript": "",
            "status": "API unavailable"
        }