import os
from dotenv import load_dotenv
from ninjadjangoproject.settings import BASE_DIR

load_dotenv(os.path.join(BASE_DIR, '.env'))

def get_database():
    return {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'postgres'),    
        'USER': os.getenv('DB_USER', 'postgres'),    
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),    
        'HOST': os.getenv('DB_HOST', 'localhost'),   
        'PORT': os.getenv('DB_PORT', '5432'),        
    }

