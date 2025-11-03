# -*- coding: utf-8 -*-
#  Симулятор роботи сайту
#  WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
#  Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
#  WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
#  Реалізація функціональності:
#  Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
#  Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.
#  Додаткові можливості (за бажанням на кристалики):
################################################################################################
# 1.Реалізуйте систему логіну/реєстрації для керування сайтом.
# 2.Додайте можливість редагування існуючих сторінок.
# 3.Створіть функціонал для пошуку сторінок за ключовими словами у заголовку або вмісті.


from datetime import datetime


class WebPage:
    def __init__(self, title: str, content: str = "", published_at: datetime | None = None):
        self.title = title
        self.content = content
        self.published_at = published_at or datetime.now()

    def show_details(self):
        # Заглушка: вивід деталей сторінки
        print(
            f"Деталі сторінки:\n- Заголовок: {self.title}\n- Дата: {self.published_at}\n- Вміст: {self.content[:50]}...")


class WebSite:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
        self.pages: list[WebPage] = []
        # Гарантуємо наявність index.html як стартової сторінки
        self._ensure_index_page()

    def __eq__(self, other) -> bool:
        if not isinstance(other, WebSite):
            return NotImplemented
        return self.url == other.url

    def __lt__(self, other) -> bool:
        if not isinstance(other, WebSite):
            return NotImplemented
        # Сортуємо за назвою, при рівності — за URL
        if self.name != other.name:
            return self.name < other.name
        return self.url < other.url

    def _ensure_index_page(self):
        if not any(p.title == "index.html" for p in self.pages):
            self.pages.append(WebPage(title="index.html", content="Головна сторінка"))

    def add_page(self, title: str, content: str):
        """додавання сторінки"""
        print(f"Додавання сторінки '{title}' до сайту '{self.name}'")

        title = (title or "").strip()
        if not title:
            print("Помилка: порожня назва сторінки.")
            return False
        if any(p.title == title for p in self.pages):
            print(f"Помилка: сторінка '{title}' вже існує.")
            return False
        page = WebPage(title=title, content=content or "")
        self.pages.append(page)
        print(f"Сторінку '{title}' додано до сайту '{self.name}'.")
        return True

    def remove_page(self, title: str):
        """Видалення сторінки за назвою. Повертає True, якщо сторінку видалено."""
        print(f"Видалення сторінки '{title}' із сайту '{self.name}'")
        title = (title or "").strip()
        if not title:
            print("Помилка: порожня назва сторінки.")
            return False
        if title == "index.html":
            print("Помилка: index.html не можна видалити.")
            return False

        probe = WebPage(title=title)  # рівність за title
        for i, page in enumerate(self.pages):
            if page == probe:
                removed = self.pages.pop(i)
                print(f"Сторінку '{removed.title}' видалено із сайту '{self.name}'.")
                return True

        print(f"Помилка: сторінку '{title}' не знайдено.")
        return False

    def show_info(self):
        print(f"Інформація про сайт '{self.name}' ({self.url})")
        print(f"К-сть сторінок: {len(self.pages)}")
        print("Список сторінок:", ", ".join(p.title for p in self.pages))


def print_menu():
    print("\nМеню:")
    print("1 — Створити сайт")
    print("2 — Додати сторінку")
    print("3 — Видалити сторінку")
    print("4 — Показати інформацію про сайт")
    print("0 — Вихід")


def create_site() -> WebSite:
    name = input("Введіть назву сайту: ").strip() or "Мій сайт"
    url = input("Введіть URL сайту: ").strip() or "https://example.com"
    site = WebSite(name=name, url=url)
    print(f"Сайт '{site.name}' створено. Додано сторінку index.html")
    return site


def add_page_flow(site: WebSite | None):
    if site is None:
        print("Спочатку створіть сайт (пункт 1 меню).")
        return
    title = input("Заголовок (наприклад, about.html): ").strip() or "page.html"
    content = input("Вміст сторінки: ").strip()
    site.add_page(title, content)


def remove_page_flow(site: WebSite | None):
    if site is None:
        print("Спочатку створіть сайт (пункт 1 меню).")
        return
    title = input("Введіть заголовок сторінки для видалення: ").strip()
    if not title:
        print("Порожній заголовок не допускається.")
        return
    if title == "index.html":
        print("index.html не можна видалити.")
        return
    site.remove_page(title)


def show_site_info_flow(site: WebSite | None):
    if site is None:
        print("Сайт ще не створено.")
        return
    site.show_info()


if __name__ == "__main__":
    site: WebSite | None = None

    while True:
        print_menu()
        choice = input("Ваш вибір: ").strip()
        if choice == "0":
            print("Вихід.")
            break
        elif choice == "1":
            site = create_site()
        elif choice == "2":
            add_page_flow(site)
        elif choice == "3":
            remove_page_flow(site)
        elif choice == "4":
            show_site_info_flow(site)
        else:
            print("Невірний вибір, спробуйте ще.")