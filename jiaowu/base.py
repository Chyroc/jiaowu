# -*- coding: utf-8 -*-

import re
import requests

from jiaowu.exceptions import CollegeJiaowuRequestException


class CollegeJiaowuBase(object):
    """基类
    """

    def __init__(self):
        self.session = requests.session()

    def get_encoding_from_reponse(self, r):
        """获取编码
        """
        encoding = requests.utils.get_encodings_from_content(r.text)
        return encoding[0] if encoding else requests.utils.get_encoding_from_headers(r.headers)

    def get(self, url, **kwargs):
        r = self.session.get(url, **kwargs)
        if r.status_code == requests.codes.ok:
            r.encoding = self.get_encoding_from_reponse(r)
            return r
        else:
            raise CollegeJiaowuRequestException(r.status_code, 'get url error: ' + url)

    def post(self, url, data=None, json=None, **kwargs):
        r = self.session.post(url, data=data, json=json, **kwargs)
        if r.status_code == requests.codes.ok:
            r.encoding = self.get_encoding_from_reponse(r)
            return r
        else:
            raise CollegeJiaowuRequestException(r.status_code, 'post url error: ' + url)

    def get_request_param(self, url):
        r = self.get(url)
        __VIEWSTATE = re.findall('__VIEWSTATE" value="(.*?)"', r.text)
        param = dict()
        if __VIEWSTATE:
            param['__VIEWSTATE'] = __VIEWSTATE[0]
        return param
