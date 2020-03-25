import os

from decouple import config

bind = "0.0.0.0:8000"
loglevel = config("LOG_LEVEL", "INFO")
workers = config("WORKERS", default='1', cast=int)
accesslog = "-"
