# # -*- coding: utf-8 -*-
# #  1. Напишіть програму, яка приймає два цілих числа від
# # користувача і виводить суму діапазону чисел між ними.
# num1 = int(input("Перше ціле число"))
# num2 = int(input("Друге ціле число"))
#
# start = min(num1, num2)
# end = max(num1, num2)
#
# total = 0
# for x in range(start, end + 1):
#     total += x
#
# print("Сума діапазону:", total)
#
# #  2. Напишіть програму, для знаходження суми всіх парних
# # чисел від 1 до 100.
# sum_even = 0
# for n in range(2, 101, 2):
#     sum_even += n
# print("Сума парних від 1 до 100:", sum_even)
#
# #  3. Напишіть програму, яка приймає рядок від користувача і
# # виводить кожну літеру рядка на окремому рядку.
# text = input("Введіть рядок: ")
# for letter in text:
#     print(letter)
#
# #  4. Напишіть програму, яка створює список цілих чисел та
# # виводить новий список, який містить лише парні числа з
# # вихідного списку.
# numbers_input = input("Введіть цілі числа через пробіл: ")
# numbers = [int(x) for x in numbers_input.split()]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print("Парні числа:", even_numbers)
#
# # 5.Напишіть функцію, яка приймає список рядків від
# # # користувача і повертає новий список, що містить лише
# # # рядки, що починаються з великої літери.
#
# # Згенерований вхідний рядок (імітує ввід користувача)
# input_string = "Apple banana Cherry dog Енот єнот Python java Ruby 123start _hidden"
#
# def only_capitalized(strings: list[str]) -> list[str]:
#     """
#     функція, яка приймає список рядків від
#     користувача і повертає новий список, що містить лише
#     рядки, що починаються з великої літери.
#     """
#
#     return [s for s in strings if s and s[0].isalpha() and s[0].isupper()]
#
# # Перетворюємо на список рядків (за пробілами або іншим роздільником)
# strings = input_string.split()
#
# result = only_capitalized(strings)
# print("Вхідні рядки:", strings)
# print("З великої літери:", result)
#
#
# #  6. Напишіть функцію, яка приймає список рядків від
# # користувача і повертає новий список, що містить лише
# # рядки, які містять слово "Python".
# def contains_python(strings: list[str]) -> list[str]:
#     # Враховуємо точне слово "Python" (регістрочутливо)
#     return [s for s in strings if "Python" in s]
#
# result = contains_python(strings)
# print("Вхідні рядки:", strings)
# print("Містить слово Python:", result)

##################################################################################
#  7. (додаткове на кристалики) Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.

WORDS = {
    "Python": "Мова програмування високого рівня з акцентом на читабельність.",
    "Function": "Блок коду, який виконує певне завдання і може повертати значення.",
    "Variable": "Ім’я, що посилається на значення, збережене в пам’яті.",
    "Algorithm": "Скінченна послідовність кроків для розв’язання задачі.",
    "List": "Упорядкована змінювана колекція елементів у Python.",
    "Dictionary": "Невпорядкована колекція пар ключ-значення.",
    "Loop": "Конструкція, що дозволяє багаторазово виконувати блок коду.",
    "Class": "Шаблон (тип) для створення об’єктів з полями та методами.",
    "Module": "Файл з кодом Python, який можна імпортувати та використовувати.",
    "Exception": "Механізм обробки помилок під час виконання програми."
}


def add_word():
    word = input("Введіть слово: ").strip()
    if not word:
        print("Порожнє слово не допускається.")
        return

    if word in WORDS:
        print("Слово вже існує. Поточне визначення:", WORDS[word])
        overwrite = input("Перезаписати? (y/n): ").strip().lower()
        if overwrite != "y":
            return

    definition = input("Введіть визначення: ").strip()
    WORDS[word] = definition
    print(f'Додано/оновлено: "{word}"')


def delete_word():
    word = input("Введіть слово для видалення: ").strip()
    if word in WORDS:
        del WORDS[word]
        print(f'Видалено: "{word}"')
    else:
        print("Слова не знайдено.")


def search_word():
    word = input("Введіть слово для пошуку: ").strip()
    if word in WORDS:
        print(f'{word}: {WORDS[word]}')
    else:
        print("Не знайдено.")


def list_words():
    if not WORDS:
        print("Словник порожній.")
        return
    print("Слова у словнику:")
    for w, d in WORDS.items():
        print(f"- {w}: {d}")


ACTIONS = {
        "1": add_word,
        "2": delete_word,
        "3": search_word,
        "4": list_words,
        "0": None,
    }


def run_words_menu():

    while True:
        print("\nМеню словника:")
        print("1 — Додати/оновити слово")
        print("2 — Видалити слово")
        print("3 — Знайти слово")
        print("4 — Показати всі слова")
        print("0 — Вихід")
        choice = input("Ваш вибір: ").strip()
        if choice == "0":
            print("Вихід із меню.")
            break
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Невірний вибір. Спробуйте ще.")

if __name__ == "__main__":
    run_words_menu()
# ... existing code ...