from database.database_handler import DatabaseHandler
from mail_service.email_sender import EmailSender
from text_to_speech.speech import TextToSpeech
from voice_recognition.speech_processing import SpeechRecognition


class ProgramRunner:
    """
    Класс, реализующий основную логику работы программы.
    """

    def __init__(self):
        self.speech_processing = SpeechRecognition()
        self.database_handler = DatabaseHandler()
        self.text_to_speech = TextToSpeech()
        self.recipient = None
        self.subject = None
        self.text_message = None
        self.dict_action_selection = {
            1: ['Добавить пользователя', self.action_add_user],
            2: ['Отправить email', self.action_send_email],
            3: ['Выйти из программы'],
        }

    def get_email_info(self):
        """
        Запрашивает информацию о получателе письма, теме и тексте письма.
        """
        voice_texts = ['Кому отправить письмо?', 'Укажите тему письма', 'Укажите текст письма']
        attributes = ['recipient', 'subject', 'text_message']
        while True:
            for voice_text, attribute in zip(voice_texts, attributes):
                setattr(self, attribute, self.speech_processing.speech_processing(voice_text))
                if attribute == attributes[0]:
                    self.recipient = self.database_handler.get_data(self.recipient)
                if not self.recipient:
                    self.text_to_speech.talk('Пользователь не найден в базе данных')
                    break
            else:
                return

    def action_selection(self):
        """
        Выбирает действие пользователем.
        """
        while True:
            for key, value in self.dict_action_selection.items():
                print(f'{key}. {value[0]}')
            try:
                self.text_to_speech.talk('выберите действие')
                action = int(input('Ваш выбор:  '))
                self.text_to_speech.talk(f'Вы выбрали {self.dict_action_selection[action][0]}')
            except (ValueError, KeyError):
                self.text_to_speech.talk('Введено некорректное значение. Пожалуйста, повторите попытку.')
                continue
            return action

    def action_add_user(self):
        """
        Действие добавления нового пользователя в базу данных.
        """
        attributes = ['name', 'email']
        dict_user_data = {}
        for attribute in attributes:
            dict_user_data[attribute] = input(f'Введите {attribute} пользователя:   ')
        self.database_handler.set_data(**dict_user_data)
        self.text_to_speech.talk('Пользователь успешно добавлен в базу данных')

    def action_send_email(self):
        """
        Действие отправки email пользователю.
        """
        self.get_email_info()
        email = EmailSender(self.recipient, self.subject, self.text_message)
        email.send_message()
        self.text_to_speech.talk('Email отправлен')

    def run_program(self):
        """
        Основной метод, запускающий программу и вызывающий другие необходимые методы.
        """
        while True:
            action = self.action_selection()
            try:
                if self.dict_action_selection[action][0] == 'Выйти из программы':
                    self.text_to_speech.talk('До свидания!')
                    break
                self.dict_action_selection[action][1]()
            except (KeyError, IndexError):
                continue


if __name__ == '__main__':
    program_runner = ProgramRunner()
    program_runner.run_program()
