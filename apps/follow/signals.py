# coding: utf-8
from django.dispatch.dispatcher import Signal
'''
使用dispatch的Signal，定义followed和unfollow，需提供参数用户，目标用户，实例
'''
followed = Signal(providing_args = ['user', 'target', 'instance'])
unfollow = Signal(providing_args = ['user', 'target', 'instance'])
