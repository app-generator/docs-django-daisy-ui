# [Django Core](https://github.com/app-generator/core-django)

Minimal **Django** project with `Docker` support - actively supported by [App Generator](https://app-generator.dev/) via `Email` and **[Discord](https://discord.gg/fZC6hup)**. 


## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/core-django.git
$ cd core-django
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

---
**[Django Core](https://github.com/app-generator/core-django)** - Minimal **Django** core provided by **[AppSeed](https://appseed.us/)**
