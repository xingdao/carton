# _*_ coding:utf-8 _*_

"""
@author: qiao
"""

# SUCCESS MESSAGE
C_OK = {"code": 0}

# ERROR JSON MESSAGE
E_ERROR = {"code": -1, "detail": "未知错误"}
E_USERNAME_OR_PASSWORD = {"code": 1, "detail": "用户名或密码错误"}
E_USERNAME_REPEAT = {"code": 2, "detail": "用户名已存在"}
E_EMAIL_REPEAT = {"code": 3, "detail": "邮箱已存在"}
E_NO_JSON_DATA = {"code": 4, "detail": "数据格式错误"}
E_MSM_CODE = {"code": 5, "detail": "验证码错误"}

