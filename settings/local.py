import os
"""
create database django_template character set utf8;
"""
mysql_host = os.environ.get('mysqlhost', '')
DATABASES = {
    'default': {
        'NAME': 'toplist',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '{}'.format(mysql_host),
        'CHARSET': 'utf8'
    }
}
redis_host = os.environ.get('redishost', '127.0.0.1')
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{}/1".format(redis_host),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": ""
        }
    },
    "token": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{}/2".format(redis_host),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
        }
    }
}

MONGODB_DATABASES = {
    "default": {
        "name": 'django_template',
        "host": 'localhost:3717',
        "password": 'password',
        "username": 'username',
        "tz_aware": True,  # if you using timezones in django (USE_TZ = True)
    },
}

## other local setting

## oss
ACCESS_KEY_ID = "****"
ACCESS_KEY_SECRET = "****"
END_POINT = "oss-cn-shanghai.aliyuncs.com"
BUCKET_NAME = "****"
ALIYUN_OSS_CNAME = "" # 自定义域名，如果不需要可以不填写
BUCKET_ACL_TYPE = "private" # private, public-read, public-read-write
# mediafile将自动上传
# DEFAULT_FILE_STORAGE = 'aliyun_oss2_storage.backends.AliyunMediaStorage'
# staticfile将自动上传
# STATICFILES_STORAGE = 'aliyun_oss2_storage.backends.AliyunStaticStorage'

# ==================
# = celery
# ==================
CELERY_BROKER_URL = 'redis://{}/1'.format(redis_host)
CELERY_RESULT_BACKEND = 'redis://{}/1'.format(redis_host)


