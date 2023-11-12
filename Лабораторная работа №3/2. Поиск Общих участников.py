# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, coma=","):
    group1 = group1.split(coma)
    group2 = group2.split(coma)
    general = list(set(group1).intersection(group2))
    general.sort()

    return general

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print("Общие участники:", find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
