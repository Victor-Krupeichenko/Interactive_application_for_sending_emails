import speech_recognition as sr
from text_to_speech.speech import TextToSpeech


class SpeechRecognition:
    """
    Класс для распознавания речи
    """

    def __init__(self, microphone_id=0, language='ru-Ru', rate=180, volume=0.8, voice_id=1):
        """
        Конструктор класса
        :param microphone_id: id-микрофона
        :param language: зык распознавания речи
        :param rate: Скорость голоса
        :param volume: громкость голоса
        :param voice_id: id-голосового пакета из ОС
        """
        self.r = sr.Recognizer()
        self.microphone = sr.Microphone(device_index=microphone_id)
        self.language = language
        self.text_to_speech = TextToSpeech(rate, volume, voice_id)

    def speech_processing(self, text):
        """
        Метод для распознавания речи с микрофона
        :param text: Текст который нужно преобразить в речь
        :return: Строка с распознанной речью
        """
        with self.microphone as source:
            while True:
                self.text_to_speech.talk(text)
                try:
                    audio = self.r.listen(source)
                    recognized_text = self.r.recognize_google(audio, self.language)
                    if not recognized_text:
                        continue
                except sr.UnknownValueError:
                    self.text_to_speech.talk('Не могу распознать речь')
                    continue
                except sr.RequestError:
                    self.text_to_speech.talk('Ошибка: при отправки запроса на распознания речи')
                    continue
                return recognized_text
