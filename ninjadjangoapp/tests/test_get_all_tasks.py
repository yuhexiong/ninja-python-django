from django.urls import reverse
from rest_framework import status
from ninjadjangoapp.models import Task
from ninjadjangoapp.tests.base import BaseTestCase


class GetAllTasksTestCase(BaseTestCase):

    def setUp(self):

        super().setUp()

        self.task = Task.objects.create(
            title="Sample Task 1",
            description="This is the first task",
            status="pending",
            due_date="2024-12-31"
        )

        self.url = reverse(self.get_test_path('get_all_tasks'))


    def test_get_all_tasks_success(self):
        """
        測試成功查詢所有任務
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        tasks = response.json()['data']
        self.assertEqual(len(tasks), 1)

        task = tasks[0]
        expected_fields = ['title', 'description', 'status', 'due_date']

        for field in expected_fields:
            self.assertEqual(
                task[field], 
                getattr(self.task, field),
                msg=f"task 內的 {field} 預期為 {getattr(self.task, field)}，實際為 {task[field]}"
            )
