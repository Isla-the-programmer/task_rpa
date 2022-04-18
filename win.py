from pywinauto import Application


def pywinauto_task(file_f, text):
    app = Application().start('notepad.exe')
    app['Безымянный – Блокнот'].MenuSelect('Файл-> Сохранить как ...')
    txt = '.txt'
    app["Сохранить как"]['edit'].TypeKeys(file_f + txt)
    app["Сохранить как"]["Сохранить"].click()
    app[file_f + ' – Блокнот'].edit.TypeKeys(text + '\n', with_newlines=True)
    app.Notepad.MenuSelect("Файл-> Выход")
    app['Блокнот']["Сохранить"].click()


if __name__ == '__main__':   # Выполнить эту функцию
    file_f = str(input("Введите название нового файла\n"))
    text = str(input("Введите текст\n"))
    pywinauto_task(file_f= file_f, text= text)
