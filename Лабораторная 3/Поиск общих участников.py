# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, razd = ','):
    group1 = set(str1.split(razd))
    group2 = set(str2.split(razd))
    result = group1.intersection(group2)
    result = list(result)
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, ' '))