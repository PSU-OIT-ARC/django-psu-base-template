# WDT Django project template

This template is used to start any Django project that will use the PSU Base Plugin

## How to use

```bash
$ django-admin.py startproject \
  --template=https://github.com/PSU-OIT-ARC/django-psu-base-template/archive/master.zip \
  --extension=py,md,txt \
  project_name
$ cd project_name
$ pip install -r requirements.txt
$ python manage.py migrate
```