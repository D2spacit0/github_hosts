# -*- coding: utf-8 -*-
# @Time : 2022/1/5 16:58
# @Author : D2spacit0
# @File : update_host
# @Email:yldiabolo@outlook.com


import requests
from os import system

def get_hosts():
    response = requests.get("https://raw.hellogithub.com/hosts")
    response.enconding = 'utf-8'
    return response.text


def update_hosts():
    text = get_hosts()
    with open(r'C:\Windows\System32\drivers\etc\hosts', 'a+') as f:
        f.truncate(0)
        f.write(text)
    system("ipconfig /flushdns")


if __name__ == '__main__':
    update_hosts()
