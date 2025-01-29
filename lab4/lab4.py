if __name__ == "__main__":
    # Write your solution here
    pass

import random


class SoftToys:
    """
    Базовый класс мягкие игрушки.
    name: название
    length: длина тела
    colour: окрас
    colorlist: список цветов
    """
    def __init__(self, name: str, length: int, colour: str):
        self.name = None
        self.length = None
        self.colour = None

    def set_params(self, name: str, length: int, colour: str):
        if not isinstance(length, int):
            raise TypeError("Длина должна быть типа int")
        self.name = name
        self.length = length
        self.colour = colour

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, length={self.length!r}, colour={self.colour!r})"

    def __str__(self):
        return f"Игрушка {self.name}. Длина {self.length}. Цвет {self.colour}"

    def changecolour(self):
        colorlist = ['red', 'orange', 'yellow', 'green', 'blue','indigo', 'violet'] #список цветов
        newcolour = random.choice(colorlist)
        self.colour = newcolour


class Amigurumi(SoftToys):
    """
        Дочерний класс Амигуруми(мягкие игрушки).
        name: название
        length: длина тела
        colour: окрас
        colorlist: список цветов
        yarn: толщина нити для вязания
        """

    def __init__(self, name: str, length: int, colour: str):
        self.name = None
        self.length = None
        self.colour = None
        self.yarn = None

    def selectyarn(self):
        self.yarn = random.choice(['1', '2', '3', '4', '5']) #толщина нити для вязания

    def __str__(self):
        return f"Амигуруми {self.name}. Длина {self.length}. Толщина нити {self.yarn}"


first_one = SoftToys("Seal", 23, "White")
first_one.set_params("Seal", 23, "White")
first_one.changecolour()
print(first_one)

second_one = Amigurumi("Snake", 72, "Green")
second_one.set_params("Snake", 72, "Green")
second_one.selectyarn()

print(second_one)