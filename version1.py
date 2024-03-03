import time
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

file_name = "Мой дом ужасов.txt"
options = Options()
options.add_extension("/home/yuri/PycharmProjects/bookparser/Files/AdBlock.crx")
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 0})
driver = webdriver.Chrome(options)


# Open the specified URL
def page_reader():
    try:
        assert "Мой дом ужасов" in driver.title
        time.sleep(3)
        search = driver.find_elements(By.TAG_NAME, "p")
        title = driver.find_element(By.CLASS_NAME, "ui.header").text + "\n"
        ls = ""
        for i in search:
            ls += i.text + "\n"
        return title + ls
    except Exception as e:
        print(f"Ошибка при обработке страницы {driver.page_source}: {e}")


def button_click():
    button = driver.find_element(By.XPATH, "//a/span[text()='Вперед']")
    button.click()


def main():
    url = "https://ranobehub.org/ranobe/535/1/1"
    driver.get(url)
    with open(file_name, 'a+') as file:
        for i in range(1, 1034):
            file.write(page_reader())
            button_click()
    print("Программа успешно завершила выполнение.")
    driver.quit()


if __name__ == "__main__":
    main()
