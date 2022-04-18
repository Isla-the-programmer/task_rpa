from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def open_query(query, num):
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.get('http://www.google.com')
    search = browser.find_element(By.NAME, 'q')
    search.send_keys(query)
    search.send_keys(Keys.RETURN)
    browser.implicitly_wait(15)
    links = browser.find_elements(By.CLASS_NAME, "yuRUbf")
    for k, link in enumerate(links):
        if k == num-1:
            url = link.find_element_by_tag_name('a').get_attribute("href")
            browser.execute_script('''window.open("{}","_blank");'''.format(url))
            return link.find_element_by_tag_name('a').get_attribute("href")


if __name__ == "__main__":
    query = str(input("Введите запрос:\n"))
    num = int(input("Номер ссылки\n"))
    print(open_query(query=query, num=num))
