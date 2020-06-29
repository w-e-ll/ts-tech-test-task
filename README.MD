Setup
=====

Clone the repo, create virtualenv if necessary.

Operate from base folder [../terminal].

To start the demo application you need running MySQL server.
In case you have it already - good.

Make next commands to create user, database, grant privileges::

    $ sudo mysql -u root -p -h localhost
    $ DROP USER 'well'@'localhost';
    $ CREATE USER 'well'@'localhost' IDENTIFIED BY '123';
    $ CREATE DATABASE terminal /*!40100 DEFAULT CHARACTER SET utf8 */;
    $ GRANT ALL PRIVILEGES ON terminal.* TO 'well'@'localhost';
    $ show databases;
    $ quit

Run db server::

    $ python app/main.py

Create table terminal with sample data::
 
    $ http://127.0.0.1:8080/post/
    $ add data to the post form 
    
Get sample data::
 
    $ http://127.0.0.1:8080

Testing
=======
Make next commands to create test user, test database, grant privileges::

    $ sudo mysql -u root -p -h localhost
    $ DROP USER 'test_user'@'localhost';
    $ CREATE USER 'test_user'@'localhost' IDENTIFIED BY '123';
    $ CREATE DATABASE test_app /*!40100 DEFAULT CHARACTER SET utf8 */;
    $ GRANT ALL PRIVILEGES ON test_app.* TO 'test_user'@'localhost';
    $ show databases;
    $ quit

Run tests::

    $ pytest tests/test_integration.py
    
TODO::
=======

    $ Dockerize App
    $ Fix init_db.py - missing dependency
    $ Make more tests
    $ Add type checking
    $ Fix some errors