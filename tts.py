import pyttsx3


def get_voices():
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    voice_list = []

    for index, voice in enumerate(voices):
        voice_list.append({
            "id": index,
            "name": voice.name
        })

    engine.stop()

    return voice_list


def speak_text(text, voice_id=0, speed=200, volume=100):
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    if 0 <= voice_id < len(voices):
        engine.setProperty("voice", voices[voice_id].id)

    engine.setProperty("rate", speed)

    engine.setProperty("volume", volume / 100)

    engine.say(text)

    engine.runAndWait()

    engine.stop()