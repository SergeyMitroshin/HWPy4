# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [1, 2, 223, 2, 3, 3, 7, 4, 5, 15]

def get_unnumbers(numbers):
    list_of_unique_numbers = []
    unumbers = set(numbers)

    for number in unumbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(get_unnumbers(numbers))