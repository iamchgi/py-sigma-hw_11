"""
Завдання_1.
З використанням технології стека – stack та рекурсивних викликів розробити програмний скрипт алгоритму «Ханойська вежа»
(https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/)
Алгоритм «Ханойська вежа»:
Для піраміди із 3 веж - стрижнів необхідно перемістити всі диски на сусідній стрижень з урахуванням наступних правил:
1. За один крок переміщається тільки один диск;
2. Диск більшого розміру не можна розташовувати над диском меншого розміру.

------------------------------------------------------------------------------------------------------------------------------------
Приклад організації стеку з використанням метода deque з модуля collections -
реалізує спеціалізовані типи даних контейнерів
По суті - здійснено трансформація правил черги до рівня стека.
https://docs.python.org/uk/3/library/collections.html#module-collections

Створити стек - означає встановити взаємодію елементів та операцій над ними
push(a) – Вставляє елемент «a» у верхній частині стека
pop() – видаляє найвищий елемент стеку
empty() – Повертає, чи стек порожній
full() : перевірити, чи заповнений стек
peek() – повертає посилання на найвищий елемент стека

Package Version
------- -------
pip 24.3.1

"""

from collections import deque

global tower_1, tower_2, tower_3


def create_stack(n) -> deque:
    stack = deque(maxlen=n)
    return stack


def push(stack, item) -> None:
    if full(stack):
        raise "steck full"
    stack.append(item)


def pop(stack) -> int:
    if empty(stack):
        raise "Stack is empty"
    return stack.pop()


def peek(stack) -> int:
    return stack[-1]


def empty(stack) -> bool:
    return len(stack) == 0


def full(stack) -> bool:
    return len(stack) == stack.maxlen


def init_data(tower, n) -> None:
    while n > 0:
        push(tower, n)
        n -= 1
    return None


def towers_draw() -> None:
    for tower in [tower_1, tower_2, tower_3]:
        print(list(tower))
    print("--------------------------------")
    return


def disks_moving(tower_s, tower_a, tower_d, n) -> None:
    """
    Рекурсивний метод для руху дисків 'Ханойської башти'
    :param tower_s: Source rod, з якого плануємо брати диск(и)
    :param tower_a: Допоміжний стержень
    :param tower_d: Стержень, на який переміщуються диск(и)
    :param n: кількість дисків які треба перемістити
    :return: None
    """
    if n == 1:
        push(tower_d, pop(tower_s))
        towers_draw()
        return
    disks_moving(tower_s, tower_d, tower_a, n - 1)
    disks_moving(tower_s, tower_a, tower_d, 1)
    disks_moving(tower_a, tower_s, tower_d, n - 1)


def tower_of_hanoi_main() -> None:
    global tower_1, tower_2, tower_3
    n = int(input("Кількість дисків ->"))
    tower_1 = create_stack(n)
    tower_2 = create_stack(n)
    tower_3 = create_stack(n)
    init_data(tower_1, n)
    towers_draw()
    disks_moving(tower_1, tower_2, tower_3, n)
    return None