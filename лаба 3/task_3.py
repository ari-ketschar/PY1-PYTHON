def count_letters(str_):
    letters = []
    letters_dict = {}
    for sym in str_.lower():
        if sym.isalpha():
            if letters_dict.get(sym) != None:
                letters_dict[sym] += 1
            else:
                letters_dict[sym] = 1

    return letters_dict


def calculate_frequency(letters_):
    letters_frequency = {}
    total = sum(letters_.values())
    for letter, count in letters_.items():
        letters_frequency[letter] = round((count / total), 2)

    return letters_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letters_dict = count_letters(main_str)
frequency = calculate_frequency(letters_dict)
for letter, freq in frequency.items():
    print(f"{letter}: {freq:.2f}")
