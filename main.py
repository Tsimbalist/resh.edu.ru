from selenium import webdriver
import time
import os

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        pass

print('╔╗  ╔╗ ╔╗ ╔═══╗╔═══╗╔╗╔═╗╔═══╗')
print('║╚╗╔╝║╔╝║ ║╔═╗║║╔═╗║║║║╔╝║╔═╗║')
print('╚╗║║╔╝╚╗║ ║║ ║║║║ ║║║╚╝╝ ║║ ║║')
print(' ║╚╝║  ║║ ║╚═╝║║║ ║║║╔╗║ ║║ ║║')
print(' ╚╗╔╝ ╔╝╚╗║╔═╗║║╚═╝║║║║╚╗║╚═╝║')
print('  ╚╝  ╚══╝╚╝ ╚╝╚═══╝╚╝╚═╝╚═══╝')

time.sleep(1)
clear_console()

driver = webdriver.Chrome()

clear_console()

site = input("Введите ссылку на сайт урока: ")
clear_console()
driver.get(site)
clear_console()

print('╔╗  ╔╗ ╔╗ ╔═══╗╔═══╗╔╗╔═╗╔═══╗')
print('║╚╗╔╝║╔╝║ ║╔═╗║║╔═╗║║║║╔╝║╔═╗║')
print('╚╗║║╔╝╚╗║ ║║ ║║║║ ║║║╚╝╝ ║║ ║║')
print(' ║╚╝║  ║║ ║╚═╝║║║ ║║║╔╗║ ║║ ║║')
print(' ╚╗╔╝ ╔╝╚╗║╔═╗║║╚═╝║║║║╚╗║╚═╝║')
print('  ╚╝  ╚══╝╚╝ ╚╝╚═══╝╚╝╚═╝╚═══╝')

while True:
    try:
        elements_with_error = driver.find_elements("css selector", ".test__task-num--with-error")

        for element in elements_with_error:
            driver.execute_script(
                'arguments[0].setAttribute("class", "test__task-num test__task-num--active test__task-num--passed")',
                element,
            )
        
        progress_element = driver.find_element("css selector", ".lk-form-submit.js-result")

        current_text = progress_element.text
        max_score = current_text.split()[-1]

        new_text = f"Пройдено {max_score} из {max_score}"
        driver.execute_script('arguments[0].textContent = arguments[1];', progress_element, new_text)

        while True:
            pass

    except Exception as e:
        time.sleep(2)
