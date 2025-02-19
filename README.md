# [Django & DaisyUI/Tailwind](https://app-generator.dev/docs/technologies/django/integrate-daisyui.html) `Starter`

Minimal [Django starter that uses DaisyUI/Tailwind](https://app-generator.dev/docs/technologies/django/integrate-daisyui.html) for styling and Vite as builder tool.

- Support: https://app-generator.dev/
- [Django & DaisyUI/Tailwind](https://app-generator.dev/docs/technologies/django/integrate-daisyui.html) - Integration Guide

<br /> 

![Django & DaisyUI/Tailwind - Thumb Image](https://github.com/user-attachments/assets/ea55908f-8b1e-4abd-9e88-0443bbeb67ba)

<br />

## Deploy on `Render` (free plan)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

<br /> 

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/docs-django-daisy-ui.git
$ cd docs-django-daisy-ui
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

> 👉 Compile DaisyUI/Tailwind

```bash
$ yarn 
$ yarn dev     # development
$ yarn build   # production
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

---
[Django & DaisyUI/Tailwind](https://app-generator.dev/docs/technologies/django/integrate-daisyui.html)- Minimal **Django** core provided by **[App-Generaror](https://app-generator.dev/)**
