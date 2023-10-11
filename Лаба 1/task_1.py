

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

index_none = 4
numbers[index_none] = 0

sum_ = sum(numbers)
count = len(numbers)
average = round((sum_ / count), 3)

numbers[index_none] = average

print("Измененный список:", numbers)
