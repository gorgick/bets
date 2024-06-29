What i used for:
-OS: Windows 7, so here are python 3.8
-django, implemented CRUD, search(postgres-search), pagination, signals, bootstrap+css, mixins
-db: postgres

PSQL for people with Windows 7 - you can write commands in lower case:
>psql
>CREATE DATABASE your_base;
>CREATE USER base_user WITH PASSWORD 'password';
>ALTER ROLE base_user SET client_encoding TO 'utf-8';
>ALTER ROLE base_user SET default_transation_isolation TO 'read commited';
>ALTER ROLE base_user SET timezone TO 'UTC';
>GRANT ALL PRIVILEGES ON DATABASE your_base TO base_user;
>\q
After that create DATABASES in your project.settings

Little bit about project:
 -That's site to sell some your staff with bets from other restered people. If your anyone outbit you - you will get a message.
 ![static/images/Notification1.png](https://github.com/{gorgick}/{bets}/raw/{master}/{static/images/Notification1.png}/Notification1.png)
 
