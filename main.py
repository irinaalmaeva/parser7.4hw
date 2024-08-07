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
browser.get('https://ru.wikipedia.org/w/index.php?search=&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&go=%D0%9F%D0%B5%D1%80%D0%B5%D0%B9%D1%82%D0%B8')

search = browser.find_element(By.ID, "searchInput")
# Спрашиваем у пользователя запрос

request = input("Введите запрос для поиска на Википедии: ")

search.send_keys(request)
search.send_keys(Keys.ENTER)

time.sleep(2)


def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()


def get_related_pages():
    global related_pages
    related_pages = browser.find_elements(By.CLASS_NAME, "mbox-text")
    for index, page in enumerate(related_pages):
        print(f"{index + 1}. {page.text}")
    return related_pages


def get_internal_links():
    global internal_links
    internal_links = browser.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    for index, link in enumerate(internal_links):
        print(f"{index + 1}. {link.text}")
    return internal_links


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
            related_pages = get_related_pages()
            if not related_pages:
                print("Нет связанных страниц. Попробуйте снова.")
                continue
            selected_page = int(input("Выберите ссылку для перехода: "))
            related_pages[selected_page - 1].click()
            time.sleep(3)
            print("\nВыберите действие:")
            print("1. Листать параграфы статьи")
            print("2. Перейти на одну из внутренних статей")
            inner_choice = input("Введите номер действия: ")
            if inner_choice == "1":
                list_paragraphs()
            elif inner_choice == "2":
                internal_links = get_internal_links()
                if not internal_links:
                    print("Нет внутренних ссылок.")
                    continue
                selected_link = int(input("Выберите ссылку для перехода: "))
                if 1 <= selected_link <= len(internal_links):
                   internal_links[selected_link - 1].click()
                   time.sleep(3)
                else:
                 print("Неверный номер ссылки. Попробуйте снова.")
            else:
                print("Неверный номер страницы. Попробуйте снова.")

        elif choice == "3":
            break
        else:
         print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()



