from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    """
    Модель таблицы users в базе данных
    """
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        """
        Для удобного вывода представления объекта user в консоли
        """
        return f'<User(id={self.id}, name={self.name}, email={self.email})>'

    def __init__(self, name, email):
        """
        Конструктор для создания нового экземпляра User
        """
        super().__init__()
        self.name = name
        self.email = email
