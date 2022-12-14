"""
Домашнее задание №1
Функции и структуры данных
"""


def is_prime(nmbr: int) -> bool:
    """
    Функция проверяет является ли число простым и
    возвращает True если число простое
    """
    if nmbr == 2 or nmbr == 3:
        return True
    if nmbr % 2 == 0 or nmbr < 2:
        return False
    for i in range(3, int(nmbr ** 0.5) + 1, 2):
        if nmbr % i == 0:
            return False
    return True


def power_numbers(*args) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    #>>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    power_numbers = []
    for item in args:
        power_numbers.append(item ** 2)
    return  power_numbers


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers: list, param: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    #>>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    #>>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    even_numbers = [item for item in numbers if not item % 2]
    odd_numbers = [item for item in numbers if item % 2]
    prime_numbers = list(filter(is_prime, numbers))
    if param == "odd":
        return odd_numbers
    elif param == "even":
        return even_numbers
    elif param == "prime":
        return prime_numbers
