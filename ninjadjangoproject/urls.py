"""
URL configuration for ninjadjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import JsonResponse
from django.urls import path
from ninja import NinjaAPI, Router
from ninjadjangoapp.urls import router as api_router
from ninja.errors import ValidationError
from django.http import HttpRequest, JsonResponse


ninja_api = NinjaAPI(
    title="Ninja Django System",
    version="1.0",
    description="Ninja API 文件",
)

# 客製化驗證錯誤
@ninja_api.exception_handler(ValidationError)
def custom_validation_error_handler(request: HttpRequest, exc: ValidationError):

    # 缺少資料
    for error in exc.errors:
        if error["type"] == "missing":
            return JsonResponse({
                "error": "Invalid Parameter Error",
                "message": f"Should provide {error['loc'][-1]} in request {error['loc'][-2]}."
            }, status=400)

    # 其他類型的錯誤
    error_details = [
        {
            "loc": error["loc"][-1],  # 錯誤發生的位置
            "msg": error["msg"],      # 錯誤訊息
            "type": error["type"],    # 錯誤類型
        }
        for error in exc.errors
    ]

    return JsonResponse({
        "error": "Invalid Parameter Error",
        "message": f"Validation failed: {', '.join([d['msg'] for d in error_details])}"
    }, status=400)



# 檢驗 Service 是否健康路由
health_router = Router()
@health_router.get("/", tags=["Health Check"])
def health_check(request):
    return JsonResponse({}, status=200)


# 使用 ninja api 來管理路由, swagger 文件自動掛載在 /docs 下面
ninja_api.add_router("/health", health_router)
ninja_api.add_router("/api", api_router) 


urlpatterns = [
    path("", ninja_api.urls),
]
