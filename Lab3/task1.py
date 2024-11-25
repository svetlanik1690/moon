# TODO Напишите функцию для поиска индекса товара


def poisk(item_list, item_name):
    ind = None
    for i in item_list:
        if i == item_name:
            ind = item_list.index(i)
            break
    return ind


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = poisk(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
