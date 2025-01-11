# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Bird:
    def __init__(self, body_length: (int, float), main_colour: str, specie: str):
        """
        Создание и подготовка к работе объекта "Птица"

        :param body_length: Длина туловища
        :param main_colour: Основной цвет птицы
        :param specie: Название вида
        Примеры:
        >>>hawk = Bird(61, "серый", "Accipiter gentilis")  # инициализация экземпляра класса
        """
        if not isinstance(body_length, (int, float)):
            raise TypeError("Длина туловища должна быть типа int или float")
        self.body_length = body_length

        if not isinstance(main_colour, str):
            raise TypeError("Основной цвет должен быть string")
        self.main_colour = main_colour
        if not isinstance(specie, str):
            raise TypeError("Вид должен быть string")
        self.specie = specie

    def type_by_size(self, body_length: (int, float)) -> str:
        """
        Функция которая определяет категорию по размеру,
        например
        if body_length < 10:
            return "small"
        if 10 < body_length < 30:
            return "middle"
        if 30 < body_length:
            return "big"

        :param body_length: Длина туловища
        :return: Категория

        Примеры:
        >>> hawk = Bird(61, "серый", "Accipiter gentilis")
        >>> hawk.type_by_size()
        """

    def rename_the_bird(self, new_specie: str) -> None:
        """
        Переименование птицы.
        :param new_specie: Новое имя вида

        :raise TypeError: Если введенное имя не является строкой то вызываем ошибку

        print("Input new specie(name) if you want")
        new_specie = input()
        self.specie = new_specie
        Примеры:
        >>> hawk = Bird(61, "серый", "Accipiter gentilis")
        >>> hawk.rename_the_bird("northern goshawk")
        """


class Subjects:
    def __init__(self, subject_name: str, number_of_course: int,
                 teacher_name: str, code_of_department: int):
        """
        Создание и подготовка к работе объекта "Предмет"

        :param subject_name: Название предмета
        :param number_of_course: Номер курса
        :param teacher_name: Фамилия преподавателя
        :param code_of_department: Условный код кафедры
        Примеры:
        >>> subj1 = Subjects('mechanics', 2, 'Ivanov', 301)  # инициализация экземпляра класса
        """
        if not isinstance(subject_name, str):
            raise TypeError('Название предмета должно быть str')
        if not isinstance(number_of_course, int):
            raise TypeError('Номер курса должен быть числом')
        if not isinstance(teacher_name, str):
            raise TypeError('Фамилия преподавателя должна быть str')
        if not isinstance(code_of_department, int):
            raise TypeError('Условный код кафедры должен быть числом')
        self.subject_name = subject_name
        self.number_of_course = number_of_course
        self.teacher_name = teacher_name
        self.code_of_department = code_of_department

    def next_course(self) -> None:
        """
                Перевод на следующий курс, увеличиваем номер курса на 1
                Примеры:
        >>> subj1 = Subjects('mechanics', 2, 'Ivanov', 301)
        >>> subj1.next_course()
        """
        self.number_of_course += 1

    def new_teacher(self, new_teacher_name: str) -> None:
        """
                Изменить преподавателя, меняем атрибут teacher name
                Примеры:
        >>> subj1 = Subjects('mechanics', 2, 'Ivanov', 301)
        >>> subj1.new_teacher('Petrov')
        """
        if not isinstance(new_teacher_name, str):
            raise TypeError('Фамилия учителя должна быть str')
        self.teacher_name = new_teacher_name


class Candies:
    def __init__(self, candy_name: str, ingredients: list):
        """
               Создание и подготовка к работе объекта "Сладость"

               :param candy_name: Название сладости
               :param ingredients: Список ингредиентов в составе

               Примеры:
               >>>maffin = Candies("маффин", ['eggs', 'flour', 'butter', 'raisin'])
               """
        if not isinstance(candy_name, str):
            raise TypeError('Имя должно быть строкой')
        if not isinstance(ingredients, list):
            raise TypeError("Ожидается список ингредиентов")
        self.candy_name = candy_name
        self.ingredients = ingredients

    def add_ingred(self, new_ingred: str) -> None:
        """
                Добавить что-то в состав сладости, меняем атрибут ingredients
                Примеры:
        >>> maffin = Candies("маффин", ['eggs', 'flour', 'butter', 'raisin'])
        >>> maffin.add_ingred('sugar')
        """
        if not isinstance(new_ingred, str):
            raise TypeError('Ингредиент должен быть str')
        self.ingredients.append(new_ingred)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
