# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import six


def to_text(value, encoding='utf-8'):
    """将 value 转为 unicode，默认编码 utf-8
    """
    if not value:
        return ''
    if isinstance(value, six.text_type):
        return value
    if isinstance(value, six.binary_type):
        return value.decode(encoding)
    return six.text_type(value)


def to_binary(value, encoding='utf-8'):
    """将 values 转为 bytes，默认编码 utf-8
    """
    if not value:
        return b''
    if isinstance(value, six.binary_type):
        return value
    if isinstance(value, six.text_type):
        return value.encode(encoding)

    if six.PY3:
        return six.binary_type(str(value), encoding)  # For Python 3
    return six.binary_type(value)


class CollegeJiaowuException(Exception):
    """异常基类
    """
    pass


class CollegeJiaowuRequestException(CollegeJiaowuException):
    """request 异常类
    """

    def __init__(self, errmsg, status_code):
        """
        :param errmsg: 错误信息
        :param status_code: http返回码
        """
        self.status_code = status_code
        self.errmsg = errmsg

    def __str__(self):
        if six.PY2:
            return to_binary('{status_code}: {msg}'.format(code=self.status_code, msg=self.errmsg))
        else:
            return to_text('{status_code}: {msg}'.format(code=self.status_code, msg=self.errmsg))
