# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participant(str1, str2, razd='|'):
    first = str1.split(razd)
    second = str2.split(razd)
    first_set = set(first)
    comm = first_set.intersection(second)
    comm = list(comm)
    comm.sort()
    return comm
r = find_common_participant(participants_first_group, participants_second_group)
print(r)
# TODO Проверьте работу функции с разделителем отличным от запятой
