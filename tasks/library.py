"""
Завдання_3.
З використанням технології hash-table створити електронний каталог бібліотеки.
Не погано, якщо це буде каталог домашньої бібліотеки.
Передбачити взаємозв’язок ключ-значення на рівні автор-бібліографія.
Інший сценарій ключ-значення також приймається.
Електронний каталог має надавати можливість його наповнення, модифікації, видалення записів, пошуку.
Мінімальний сценарій пошуку – за ключем – автором.

--------------------------------------------------------------------------------------------------------------------
Приклад реалізація хеш-таблиці в Python за допомогою ланцюжка дій:
Визначте розмір хеш-таблиці (кількість індексів у базовому масиві).
Створіть хеш-функцію, яка приймає ключ як вхідні дані та повертає індекс у масиві.
Створіть масив із вказаним розміром та ініціалізуйте його порожніми значеннями.
Реалізуйте функції для додавання, пошуку, видалення та отримання значень на основі ключів.
https://www.geeksforgeeks.org/implementation-of-hash-table-in-python-using-separate-chaining/

--------------------------------------------------------------------------------------------------------------------

"""
from tasks.Model.book import Book


class Node:                                 # Клас Node - вузол у зв’язаному списку, який міститиме пару ключ-значення + покажчик на наступний вузол у списку
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):                   # хеш функція
        return hash(key) % self.capacity

    def insert(self, book : Book):           # додавання елемента
        key = book.get_autor()
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, book)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = book
                    return
                current = current.next
            new_node = Node(key, book)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):                  # пошук елемента
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def remove(self, key):                  # видалення елемента
        index = self._hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __len__(self):                  # __len__ використовується для повернення довжини об’єкта.
        return self.size

    def __contains__(self, key):        # __contains__ перевіряє, чи існує певний елемент у колекції чи ні.
        try:
            self.search(key)
            return True
        except KeyError:
            return False

def init_library(library : HashTable) -> HashTable:
    book1 = Book(1, "Mark Twain", "The Adventures of Tom Sawyer",
                  "Видавничий дім `Школа`", "Adventures", 1876)
    book2 = Book(2, "Mark Twain", "Adventures of Huckleberry Finn",
                 "Видавництво Старого Лева", "Adventures", 1884)
    book3 = Book(3, "Mark Twain", "Tom Sawyer Abroad",
                 "А-ба-ба-га-ла-ма-га", "Adventures", 1894)
    book4 = Book(4, "Mark Twain", "Tom Sawyer, Detective",
                 "Видавництво Старого Лева", "Детектив", 1896)
    book5 = Book(5, "Arthur Conan Doyle", "Этюд в багрових тонах",
                 "Видавництво \"Освіта\"", "Детектив", 1887)
    book6 = Book(6, "Arthur Conan Doyle", "Знак чотирьох",
                 "Видавництво Старого Лева", "Детектив", 1890)
    book7 = Book(7, "Arthur Conan Doyle", "Пригоди Шерлока Холмса",
                 "А-ба-ба-га-ла-ма-га", "Детектив", 1892)
    for book in (book1, book2, book3, book4, book5, book6, book7):
        library.insert(book)                # додавання книги
    return library

if __name__ == '__main__':

    home_library = init_library(HashTable(8))              # розмір таблиці 5
    # перевірка значень в таблиці за ключем
    print("Arthur Conan Doyle" in home_library)    # = True
    print("apricot" in home_library)  # = False

    print('home_library.search("Mark Twain") = ')
    home_library.search("Mark Twain").draw()  # отримання значення за ключем = 2

    # Оновлення значення за ключем
    home_library.insert(Book(8, 'autor', 'title', 'publisher', 'genre', 'year'))
    print('home_library.insert("Mark Twain", 4) = ')
    home_library.search("Mark Twain").draw()

    # Розмір таблиці
    print('len(home_library) = ', len(home_library))  # 3