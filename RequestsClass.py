#!/usr/bin/python3

import requests

class RequestsClass:

    url = 'https://www.baidu.com'

    def __init__(self):
        print(self.url)

    def get_content(self):
        r = requests.get(self.url, timeout=0.05)
        r = r.text
        print(r)