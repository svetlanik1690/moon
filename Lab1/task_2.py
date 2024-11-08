# TODO Найдите количество книг, которое можно разместить на дискете

voluMB = 1.44
m = 1024
pages = 100
strings = 50
symbols = 25
bytes = 4
bytes_in_book = pages * strings * symbols * bytes
voluB = voluMB * m * m
n = voluB // float(bytes_in_book)
print("Количество книг, помещающихся на дискету:", round(n))