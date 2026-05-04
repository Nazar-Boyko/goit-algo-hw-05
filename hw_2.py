
from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]:
    '''
    Генерує всі дійсні числа, що зустрічаються в тексті.

    :param text: Відний рядок
    :return: Генератор числе типу float
    '''
    words = text.split()
    for word in words[1:-1]:
        try:
            yield float(word)
        except ValueError:
            continue
    

def sum_profit(text: str, func: Callable) -> float:
    """
    Обчислює суму всіх чисел, отриманих із тексту через передану функцію.

    :param text: Вхідний рядок
    :param func: Функція-генератор чисел
    :return: Сума чисел
    """
    total = 0.0
    for i in func(text):
        total += i 

    return total

text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів.")

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
