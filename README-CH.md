# Ninja

展示如何使用 Ninja 管理 Django URL 並自動生成 Swagger 文件。

## Overview

- Language: Python v3.12
- Web FrameWork: Django v5.1.4

## ENV


將 `.env.example` 複製為 `.env`  

```yaml
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY="django-insecure-"
DEBUG=True
```

## Run

### Migration

```bash
python manage.py migrate
```

### Install Module

```bash
poetry install
```


### Run Server

```bash
python manage.py runserver
```

伺服器運行在 `http://localhost:8000`  
swagger 文件在 `http://localhost:8000/docs`  

## Test

### In windows

```bash
$env:DEBUG="False"; python manage.py test ninjadjangoapp.tests --verbosity=0
```