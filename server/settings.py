import os
from mongomodels.db import MongoDatabaseBackend, MemoryDatabaseBackend

MONGODB_URI = 'localhost'
MONGODB_NAME = 'cents'

if os.environ.get('API_ENV', None) is None:
    BACKEND = MongoDatabaseBackend(MONGODB_URI, MONGODB_NAME)
elif os.environ.get('API_ENV', None) == 'test':
    BACKEND = MemoryDatabaseBackend()