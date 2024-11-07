numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим


typ_ = {
    f'{type(numbers[0])}': 0,
    f'{type(numbers[1])}': 1,
    f'{type(numbers[2])}': 2,
    f'{type(numbers[3])}': 3,
    f'{type(numbers[4])}': 4,
    f'{type(numbers[5])}': 5,
    f'{type(numbers[6])}': 6,
    f'{type(numbers[7])}': 7,
    f'{type(numbers[8])}': 8,
    f'{type(numbers[9])}': 9,
    f'{type(numbers[10])}': 10,
    f'{type(numbers[11])}': 11,
    f'{type(numbers[12])}': 12,
    f'{type(numbers[13])}': 13,
    f'{type(numbers[14])}': 14,
    f'{type(numbers[15])}': 15,
    f'{type(numbers[16])}': 16,
    f'{type(numbers[17])}': 17,
    f'{type(numbers[18])}': 18,
    f'{type(numbers[19])}': 19
}
x = typ_["<class 'NoneType'>"]
# print(typ_)
# print(x)

average_ = (sum(numbers[0:x]) + sum(numbers[x+1:])) / len(numbers)
numbers[x] = average_
print("Измененный список:", numbers)

# Я сначала решила для конкретно 4го элемента списка. потом хотела для любого элемента
# но без использования циклов и условий т.к. их не проходили.
# в итоге для списка любой длины ничего не вышло. только для 20зн.списка и только при одном символе None.