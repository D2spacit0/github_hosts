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
    f = open(r'C:\Windows\System32\drivers\etc\hosts', 'r+')
    # 删除原有hosts
    lines = []
    earse = True  # 打标记
    for line in f:
        if line.strip() == "# GitHub520 Host Start":
            earse = False  # 起始行开始不再添加
        if earse:
            lines.append(line)  # 需求之外的行添加到列表
        if line.strip() == "# GitHub520 Host End":
            earse = True
    f.truncate(0)
    f.close()
    file = open(r'C:\Windows\System32\drivers\etc\hosts', 'a+')
    file.writelines(lines)
    file.write('\n')
    # 写入新的hosts
    file.write(text)
    file.close()
    system("ipconfig /flushdns")


if __name__ == '__main__':
    update_hosts()
