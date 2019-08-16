#!/usr/bin/env python
#!-*- coding:utf-8 -*-

import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'py3_login.settings'

if __name__ == '__main__':

    send_mail(
        '来自deepnight.cn的测试邮件',
        '测试测试测试！',
        'it@deepnight.cn',
        ['gaoming@ielife.com'],
    )
