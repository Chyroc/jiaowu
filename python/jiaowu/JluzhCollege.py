# -*- coding: utf-8 -*-
import time
from PIL import Image
from .base import CollegeJiaowuBase


class JluzhCollege(CollegeJiaowuBase):
    def __init__(self, username=None, password=None):
        super().__init__()
        self.username = username
        self.password = password
        self.login_url = 'http://jw.jluzh.com/default2.aspx'
        self.vcode_url = 'http://jw.jluzh.com/CheckCode.aspx'
        self.vcode_file = 'vcode.jpg'

    def login_by_request(self):
        param = self.get_request_param(self.login_url)
        r = self.get(self.vcode_url)
        with open(self.vcode_file, 'wb') as f:
            f.write(r.content)
        open(self.vcode_file)
        data = {
            '__VIEWSTATE': param.get('__VIEWSTATE', ''),
            'txtUserName': self.username,
            'TextBox2': self.password,
            'RadioButtonList1': '确认',
            'txtSecretCode': input(),
            'Button1': ''
        }
        headers = {
            'Host': 'jw.jluzh.com',
            'Referer': self.login_url,
        }
        r = self.post(self.login_url, data=data, headers=headers)
        if self.username in r.text and '登陆' not in r.text:
            return True
        return False

    def test(self):
        headers = {
            'Referer': 'http://jw.jluzh.com/xsxk.aspx?xh=04151405&xm=%B2%CC%C0%A4%BB%D4&gnmkdm=N121101'
        }
        r = self.get('http://jw.jluzh.com/kcxx.aspx?xh=04151405&kcdm=041031&xkkh=%26nbsp%3bk', headers=headers)
        print(r.text)
