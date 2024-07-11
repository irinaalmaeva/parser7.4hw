# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
#  1. Спрашивать у пользователя первоначальный запрос.
#  2. Переходить по первоначальному запросу в Википедии.
#  3. Предлагать пользователю три варианта действий:
#  листать параграфы текущей статьи;
#  перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# выйти из программы.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
time.sleep(3)

search = browser.find_element(By.ID, "searchInput")
# Спрашиваем у пользователя запрос

request = input("Введите запрос для поиска на Википедии: ")

search.send_keys(request)

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()


def get_related_pages():
    related_pages = browser.find_elements(By.CLASS_NAME, "mbox-text")
    for index, page in enumerate(related_pages):
        print(f"{index + 1}. {page.text}")


def get_internal_links():
    internal_links = browser.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    for index, link in enumerate(internal_links):
        print(f"{index + 1}. {link.text}")


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == "1":
            list_paragraphs()
        elif choice == "2":
            get_related_pages()
            selected_page = int(input("Выберите страницу для перехода: "))
            related_pages[selected_page - 1].click()
            time.sleep(3)
            print("\nВыберите действие:")
            print("1. Листать параграфы статьи")
            print("2. Перейти на одну из внутренних статей")
            inner_choice = input("Введите номер действия: ")
            if inner_choice == "1":
                list_paragraphs()
            elif inner_choice == "2":
                get_internal_links()
                selected_link = int(input("Выберите ссылку для перехода: "))
                internal_links[selected_link - 1].click()

                time.sleep(3)
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()





