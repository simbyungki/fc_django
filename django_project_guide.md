# django project

## Django 

### project 폴더 생성
 - github

### 가상환경 설정

 - [Terminal] pip install virtualenv
 - 생성한 폴더로 이동, 
   [Terminal] virtualenv {{ venv name }}

### 가상환경 시작
 - windows > {{ venv name }}/Scripts/activate
 - Mac > source {{ venv name }}/bin/activate
 - (가상환경 종료)
   [Terminal] deactivate

### django 설치, project, app 생성
 - [Terminal] pip install django
 - [Terminal] django-admin startproject {{ project name }}
 - [Terminal] django-admin startapp {{ app name }}

### settings.py 파일에 APP 등록
 - 'INSTALLED_APPS에 생성한 APP을 추가 후 저장한다.

### models.py 작성 후,
 - [Terminal] python manage.py makemigrations
 - [Terminal] python manage.py migrate

### table 확인 
 - [Terminal] sqlite3 db.sqlite3
 - [Terminal] >>> .Tables
 - [Terminal] >>> .schema {{ table name }}

### django admin
 - [Terminal] python manage.py runserver
 - [Terminal] python manage.py createsuperuser

### form > token
 - {% csrf_token %}