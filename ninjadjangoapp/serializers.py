from ninjadjangoapp.models import Task
from rest_framework.serializers import ModelSerializer, Field

class EnumField(Field):
    """
    用於處理枚舉（Enum）的自定義序列化欄位。
    在序列化時，將枚舉實例轉換為其對應的值。
    """

    def to_representation(self, data):
        if hasattr(data, 'value'):
            return data.value
        return data


# 任務序列化
class TaskSerializer(ModelSerializer):
    status = EnumField() 

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at'  
        ]
