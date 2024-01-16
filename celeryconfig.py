import os
broker_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
celery_result_backend = os.getenv('REDIS_URL', 'redis://localhost:6379')