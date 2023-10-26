def find_common_participants(first_group, second_group, sep=","):
    common = list(set(first_group.split(sep)).intersection((second_group.split(sep))))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие участники: ", find_common_participants(participants_first_group, participants_second_group, sep="|"))
