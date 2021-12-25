# -*- coding: utf-8 -*-
# @Time : 2021/12/25 21:25
# @Author : D2spacit0
# @File : flush_host
# @Email:yldiabolo@outlook.com


import requests


def get_host():
    response = requests.get("https://raw.hellogithub.com/hosts")
    response.enconding = 'utf-8'
    return response.text


if __name__ == "__main__":
    get_host()
