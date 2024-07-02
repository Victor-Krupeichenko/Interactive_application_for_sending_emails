import pyttsx3


class TextToSpeech:
    """
    Класс для озвучки текста
    """

    def __init__(self, rate=180, volume=0.8, voice_id=1):
        """
        Конструктор класса
        :param rate: скорость голоса
        :param volume: громкость голоса
        :param voice_id: id - голосового пакета в ОС
        """
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        self.engine.setProperty(
            'voice', self.voices[voice_id].id if len(self.voices) >= voice_id else self.voices[0].id
        )

    def talk(self, text):
        """
        Метод для озвучки текста
        :param text: текст для озвучки
        """
        self.engine.say(text)
        self.engine.runAndWait()
