import os
from celery import Celery
from kombu_fernet.serializers.json import MIMETYPE
app = Celery(broker=os.getenv('REDIS_URL','redis://localhost:6379'))
app.conf.update(
    task_serializer='fernet_json',
    accept_content=[MIMETYPE,'json','pickle','application/x-fernet-json']
)