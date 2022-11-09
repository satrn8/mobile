# <h1>Mobile тесты</h1>

Mobile тесты интернет-магазина Лабиринт выполнены на языке Python с использованием Selene/Selenium, Pytest. Локальный запуск тестов проводится в Android Studio, удаленный запуск тестов проводится в Browserstack. 
Для просмотра результатов прохождения тестов используется Allure Report.
_____________________________________________________________________________________________________
Установка

```
git clone https://github.com/satrn8/mobile.git
```
Запуск локально
```
pytest .\tests\android\test_labirint_for_local.py --alluredir reports\
```
Генерация отсчета локально
```
allure serve .\reports\ 
```
________________________________________________________________________________________________________________
* <h2>Тест добавления в корзину книг по ID и заполнение формы заказа</h2> 
 
![image](https://user-images.githubusercontent.com/107774229/200141349-30d71247-6d0a-4664-9188-f4fee173eebe.png)
 
https://user-images.githubusercontent.com/107774229/200194190-c19a197b-1d29-4afc-9300-93d094a96619.mp4

 
* <h2>Тест поиска на странице</h2> 

![image](https://user-images.githubusercontent.com/107774229/200197573-0af5e6d9-e15c-431e-81ef-f4b3ca4dd22c.png)

https://user-images.githubusercontent.com/107774229/200170997-d3b0a7c5-c3c1-44d4-8d7c-0d5967b4427a.mp4

* <h2>Тест открытия раздела</h2> 

![image](https://user-images.githubusercontent.com/107774229/200141399-83488b87-3971-4ae3-ab08-e94be3a41e6e.png)

https://user-images.githubusercontent.com/107774229/200171999-119a500a-b24f-4844-9678-e9bd85a8a7cd.mp4

* <h2>Тест фильтрации</h2> 

![image](https://user-images.githubusercontent.com/107774229/200141420-a516fdd3-9db0-45a7-811d-d70fcf219e89.png)

https://user-images.githubusercontent.com/107774229/200172179-62eb459e-42a2-47c0-af59-c121f5adfd05.mp4

* <h2>Тест раздела помощи</h2> 

![image](https://user-images.githubusercontent.com/107774229/200141439-4d833d5f-574f-418b-b8c4-0c9cb145a49f.png)
