# -*- coding:utf-8 -*-
from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import StaticFilesStorage

def jinja2_environment(**options):

    #创建jinja2 Environment对象
    env = Environment(**options)

    #实现模板方法,{{ static('静态文件相对路径') }}    {{ url('路由命名空间') }}
    env.globals.update(
        {
            "url":reverse,  #修改反向解析方法，在模板中直接调用key
            "static":StaticFilesStorage.url   #获取静态文件的前缀
        }
    )
    #返回环境对象
    return env