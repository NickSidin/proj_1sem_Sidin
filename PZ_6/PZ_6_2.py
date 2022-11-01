# Дан целочисленный список размера N. Найти максимальное количество его одинаковых элементов.
from collections import Counter
def get_max_count_of_ident_elem(lis): #создание функции
    elem, count = Counter(lis).most_common()[0]
    return f'elem {elem}, count = {count}'
lis = [1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,4,5,6,7,7,7,7,7,7,7,7,7,7,7,7,7]
print(get_max_count_of_ident_elem(lis))