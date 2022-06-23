# mediasoft
 
Карасев Степан

[ТЗ.Python.docx](https://github.com/YxTiBlya/mediasoft/files/8968581/Python.docx)

В папке tz есть файл req.txt со всеми нужными библиотеками. Нужно создать виртуальную среду и установить в нее библиотеки командой pip install -r req.txt

Админка по адрессу localhost/admin. Пароль и логин админки: admin

По пути TZ/tz/settings.py в DATABASES установить свою бд. В случае с postresql создать бд, указать в настройках название бд, логин и пароль. После провести миграцию командой python manage.py migrate. И для запуска использовать python manage.py runserver
