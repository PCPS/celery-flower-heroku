import os
from kombu_fernet.serializers.json import MIMETYPE

broker_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
celery_result_backend = os.getenv('REDIS_URL', 'redis://localhost:6379')
task_serializer='fernet_json',
accept_content=[MIMETYPE,'json','pickle','application/x-fernet-json']