import os
from database.models import Base, User
from database.database_connect import engine, session
from sqlalchemy.exc import OperationalError
from settings_env import name_database


class DatabaseHandler:
    """
    Класс для управления операциями базы данных.
    """

    def __init__(self):
        """
        Инициализация подключения к базе данных.
        """
        self.session = session
        self.__check_database()

    @staticmethod
    def __check_database():
        """
        Проверяет существование базы данных (если нет то создаст базу данных)
        """
        if not os.path.exists(name_database):
            Base.metadata.create_all(engine)  # Создает таблицы в базе данных, если не существуют

    @staticmethod
    def data_handling_decorator(func):
        """
        Декоратор для обработки исключений во время работы с базой данных.
        :param func: Функция для обработки.
        """

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except OperationalError as exc:
                print(f'Ошибка при работе с базой данных: {exc}')
            except Exception as exc:
                print(f'Непредвиденная ошибка: {exc}')
            return None

        return wrapper

    @data_handling_decorator
    def get_data(self, name):
        """
        Получает конкретную запись из базы данных
        :param name: Имя пользователя.
        :return: Возвращает email пользователя или None
        """
        with self.session() as current_session:
            user = current_session.query(User).filter_by(name=name).first()
            if user:
                return user.email
            return None

    @data_handling_decorator
    def set_data(self, **kwargs):
        """
        Добавляет новую запись в базу данных.
        :param kwargs: Словарь с данными пользователя.
        """
        with self.session() as current_session:
            new_user = User(**kwargs)
            current_session.add(new_user)
            current_session.commit()
