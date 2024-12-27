from django.db import models
from enum import Enum


# 狀態枚舉類別
class StatusType(Enum):
    PENDING = "Pending"
    DONE = "Done"


# 任務表格
class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # 創建時間，自動填充
    updated_at = models.DateTimeField(auto_now=True)  # 更新時間，自動填充
    title = models.CharField(max_length=100)  # 任務標題
    description = models.TextField(blank=True, null=True)  # 任務描述
    status = models.CharField(
        max_length=20,
        choices=[(st.name, st.value) for st in StatusType],  # 狀態選項
        default=StatusType.PENDING.value,
    )
    due_date = models.DateField(blank=True, null=True)  # 截止日期


    class Meta:
        db_table = 'task'

