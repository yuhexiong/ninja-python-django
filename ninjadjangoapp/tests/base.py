from django.test import TestCase
from datetime import datetime



class BaseTestCase(TestCase):
    """
    自定義的測試基類

    功能：自動印出當前測試類別和方法名稱
    方法：取得完整測試路徑
    """

    def setUp(self):
        super().setUp()

        timestamp = datetime.now().strftime('[%d/%b/%Y %H:%M:%S]')
        color = "\033[33m"  
        print(f"{timestamp} {color}[Test] {self.__class__.__name__}: {self._testMethodName}\033[0m")


    def get_test_path(self, view_function_name):
        """
        取得完整測試路徑
        """
        
        return 'api-1.0:' + view_function_name
