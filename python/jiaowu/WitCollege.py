# -*- coding: utf-8 -*-
import time

from jiaowu.base import CollegeJiaowuBase


class WitCollege(CollegeJiaowuBase):
    def __init__(self, username=None, password=None):
        super().__init__()
        self.username = username
        self.password = password
        self.login_url = 'http://218.199.178.12/(ocpjbeqk0nfm50zvj0mfnc45)/default2.aspx'

    def login_by_request(self):
        param = self.get_request_param(self.login_url)
        data = {
            '__VIEWSTATE': param.get('__VIEWSTATE', ''),
            'TextBox1': self.username,
            'TextBox2': self.password,
            'RadioButtonList1': '确认',
            'Button1': ''
        }
        headers = {
            'Host': '218.199.178.12',
            'Referer': self.login_url,
        }
        time.sleep(6)
        r = self.post(self.login_url, data=data, headers=headers)
        if '<span id="xhxm">' + self.username in r.text:
            return True
        return False

    def get_url(self, url):
        headers = {
            'Host': '218.199.178.12',
            'Referer': 'http://218.199.178.12/(2g3tpr55dhuzr045jzpjiear)/xs_main.aspx?xh=' + str(self.username)
        }
        r = self.get(url, headers=headers)
        return r


if __name__ == '__main__':
    username = '11111111111'
    password = '22222222222'
    wit = WitCollege(username, password)
    login = wit.login_by_request()
    print(login)
    if login:
        chenji = wit.get_url(
            'http://218.199.178.12/(2g3tpr55dhuzr045jzpjiear)/xscjcx.aspx?xh=' + username + '&xm=%D0%DC%D4%AA%BD%DC&gnmkdm=N121617')
        print(chenji.text)
