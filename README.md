## WEDDEV is an collection of Django apps for learning purposes 

```sh
Django apps : 

1) ftl - simle api endpoint to fetch user

```

### Getting started open a terminal follow the instructions below

```sh
 > git clone https://github.com/NishantGhanate/webdev

 > cd webdev

 > virtualenv venv

 > venv\Scripts\activate

 > pip install -r requirements.txt

```

### Generate Django secret key :
```sh
from django.core.management.utils import get_random_secret_key

get_random_secret_key()

'[GENERATED SECRET KEY]'
```

### Env file
Simply create a .env text file on your repository’s root directory where manage.py exists , then paste GENERATED SECRET KEY :

```sh
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
SECRET_KEY=+jfvhj1(r@................
DB_HOST = 127.0.0.1
DB_NAME = test
DB_USER = root
DB_PASSWORD = root
DB_PORT = 3306
```

### Run :

```sh

> python manage.py runserver 

```

### Deploy project on heroku

```sh
 > Create app in Heroku 

 > Connect via Github add git repo & branch

 > Deploy Brach 
```

### Hosted  :-

| Platform       | URL                  |
| ------------- | ------------------------------ |
|    Heroku     | https://webdevdjango.herokuapp.com/ |

# Debug Heroku
> Check project has ( runtime.txt , procfile ) and correct content
[runtime.txt](https://github.com/NishantGhanate/webdev/blob/main/runtime.txt)
[procfile](https://github.com/NishantGhanate/webdev/blob/main/Procfile)

heroku config:set DISABLE_COLLECTSTATIC=1


