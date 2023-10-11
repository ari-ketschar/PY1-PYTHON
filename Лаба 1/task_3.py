list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

count = len(list_players)
team_1 = list_players[:int(count/2)]
team_2 = list_players[int(count/2):]

print(f"{team_1}\n{team_2}")
