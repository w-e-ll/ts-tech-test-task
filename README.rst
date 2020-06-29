# GitHub Terminal API

[Task]:
Написать простенький аппликейшн, который будет представлять упрощенную версию терминала для обработки внесенных пользователем данных.
На вход с клиента поступает некая последовательность данных от пользователя, напр.
{"name": "Bob";
"age": 27;
"city": "Oakland";
}
Сервер обязан последовательность получить, сохранить в бд и с задержкой в 10 сек вернуть ответ клиенту о том, что данные сохранены и обработаны.
Необходимо реализовать как серверную часть, так и интерфейс который будет находиться на клиенте- это можно сделать в упрощенной форме, достаточно несколько простых форм без сложных стилей.

Использовать python3, aiohttp, mysql, sqlalchemy.core (без ORM)
Код разместить на гит. репозитории

### How to run
```
$ git clone https://github.com/w-e-ll/ts-tech-test-task.git

$ cd ts-tech-test-task
```
Create a virtualenv to isolate our package dependencies locally
```
$ virtualenv -p python3.8 venv

$ source venv/bin/activate
```
Install requirements
```
$ pip install -r requirements.txt

```
Run script to fill the db
```
$ python init_db.py
# пока не работает - ошибка с зависимостью (не могу найти решение), по
этому и затянул - вчера еще все работало)
```
Run the server
```
$ python app/main.py
```
Открыть в браузере:
```
http://127.0.0.1:8080/post/ - добавить данные
http://127.0.0.1:8080/ - просмотреть данные после добавления