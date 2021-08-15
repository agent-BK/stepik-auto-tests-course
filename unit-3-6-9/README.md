
# Task: launching autotests for different interface languages

### Condition: ###
>- Create a GitHub repository where the files will be stored **conftest.py** and **test_items.py.**</br>
>- Add to the file **conftest.py** a handler that reads the language parameter from the command line.</br>
>- Implement in the file **conftest.py** the logic of launching the browser with the specified user language. The browser must be declared in the browser fixture and passed to the test as a parameter.</br>
>- To the **test_items.py** write a test that verifies that the product page on the site contains an add to cart button. For example, you can check the product available at [http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/](http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/).</br>
>- The test should be run with the language parameter with the following command: `pytest --language=es test_items.py` and pass successfully. It is enough that the code works only for the Chome browser. Send a link to this repository as a response to this task.</br>
>- Send a link to this repository as a response to this task.</br>
>- Send the solution for review to other students. Do not forget that the decision can be submitted for review only once.</br>
>- Check the solutions of at least three other students to get points for the task.</br>

***

# Задание: запуск автотестов для разных языков интерфейса 

### Условие: ###
>- Создайте GitHub-репозиторий, в котором будут лежать файлы **conftest.py** и **test_items.py**.</br>
>- Добавьте в файл **conftest.py** обработчик, который считывает из командной строки параметр language.</br>
>- Реализуйте в файле **conftest.py** логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.</br>
>- В файл **test_items.py** напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по [http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/](http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/).</br>
>- Тест должен запускаться с параметром language следующей командой: `pytest --language=es test_items.py` и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.</br>
>- Отправить ссылку на данный репозиторий в качестве ответа на данное задание.</br>
>- Отправить решение на рецензирование другим учащимся. Не забудьте, что решение на рецензирование можно отправить только один раз.</br>
>- Проверьте решения минимум трех других учащихся, чтобы получить баллы за задание.</br>