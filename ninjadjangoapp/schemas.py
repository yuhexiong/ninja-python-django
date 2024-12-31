from typing import Optional
from pydantic import BaseModel, Field
from ninjadjangoapp.models import StatusType
from ninja import Schema


# 基礎任務模型
class BaseTaskSchema(BaseModel):
    id: int = Field(..., example=1)
    title: str = Field(..., example="Sample Task Title")
    description: Optional[str] | None = Field(None, example="This is a description of the task.")
    status: StatusType = Field(..., example="Pending")
    due_date: Optional[str] | None = Field(None, example="2024-12-25")
    created_at: str = Field(..., example="2024-12-25T00:00:00.366272Z")
    updated_at: str = Field(..., example="2024-12-25T00:00:00.366272Z")


# 請求
class CreateTaskRequest(Schema):
    title: str = Field(..., example="Sample Task Title")
    description: Optional[str] | None = Field(None, example="This is a description of the task.")
    status: StatusType = Field(..., example="Pending")
    due_date: Optional[str]| None = Field(None, example="2024-12-25")


class UpdateTaskRequest(Schema):
    title: str | None = Field(None, example="Sample Task Title")
    description: Optional[str] | None = Field(None, example="This is a description of the task.")
    status: StatusType | None = Field(None, example="Pending")
    due_date: Optional[str]| None = Field(None, example="2024-12-25")


# 回應
class BaseResponse(BaseModel):
    data: None

class TaskDataResponse(BaseModel):
    data: BaseTaskSchema
