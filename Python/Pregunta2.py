#!/usr/bin/env python3
#_*_ coding:utf8 _*_

import requests


url = requests.get('https://es.wikipedia.org/wiki/Persea_americana')
print(url)