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

### Linux
```bash
DEBUG=False python manage.py test authapp.tests --verbosity=0
```

### Windows

```bash
$env:DEBUG="False"; python manage.py test ninjadjangoapp.tests --verbosity=0
```

## Usage Guide


### Params
在 [app views](./ninjadjangoapp/views.py) 中，將參數設置於 view 函數的第二個參數之後。設定完成後，只需在 `urls` 中對應，便可直接透過變數名稱獲取參數值。

### Request Body
在 [app schemas](./ninjadjangoapp/schemas.py) 中定義請求體結構，包括：資料型態、是否必填、範例資料。定義完成後，Swagger 會自動生成相關文件。  
將 Schema 放入 [app views](./ninjadjangoapp/views.py) 中作為 view 函數的第二個參數，自動驗證參數並解析為 Schema。在 view 函數中可以透過 `body.` 的方式存取請求參數。

### Response
在 [app schemas](./ninjadjangoapp/schemas.py) 中定義回應結構，並在 `urls` 中將回應 Schema 與 API 端點綁定，Swagger 將自動顯示回應格式。

### App Urls
在 [app urls](./ninjadjangoapp/urls.py) 中創建 `Router` 物件，使用 `api_operation` 方法設定：
- method：HTTP 方法（GET、POST 等）。
- path：API 路徑。
- summary：簡短描述。
- tags：分類標籤。
- response：指定回應 Schema。
- 指定要呼叫的 view function。

### Project Urls
在 [project urls](./ninjadjangoproject/urls.py) 中創建 `NinjaAPI` 物件，使用 `add_router` 方法將各個 app 的 `Router` 添加進來。可將所有 app 的 API 集中管理，並在 Swagger 中統一顯示。


