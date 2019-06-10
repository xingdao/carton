# _*_ coding:utf-8 _*_

"""
@author: qiao
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

my_log = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] - %(message)s',
            # 日志格式
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }, 'simple': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s:%(funcName)s] - %(message)s',
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/all.log'),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'simple',  # 使用哪种formatters日志格式
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/warn.log'),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'simple',  # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/error.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'request_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/request.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'simple',
        },
        'celery_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/celery.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'simple',
        },
        'celery_warning_handler': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/celery-warning.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'simple',
        },
        'admin_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/admin.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'simple',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'error', 'warning', 'info'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'carton.views': {
            'handlers': ['console', 'error', 'warning', 'info'],
            'level': 'INFO',
            'propagate': False
        },
        "carton.token": {
            "handlers": ['console', 'error', 'warning', 'info'],
            'level': 'INFO',
            'propagate': False
        },
        'api.views': {
            'handlers': ['console', 'error', 'warning', 'info'],
            'level': 'INFO',
            'propagate': False
        },
        'api.tasks': {
            'handlers': ['console', 'celery_warning_handler', 'celery_handler'],
            'level': 'INFO',
            'propagate': False
        }
    },
}
