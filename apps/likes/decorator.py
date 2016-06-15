# coding:utf-8
__author__ = 'Haddy Yang(Ysh)'
__start_date__ = '2016-06-12'
"""
    likes decorators
"""
from django.http import HttpResponse
import json


# 装饰器，检测是否有登录用户
def check_login(func):
    u"""检查是否登录用户"""

    def warpper(request):
        if request.user.is_authenticated():
            # 若有登录，则继续执行方法
            return func(request)
        else:
            # 若未登录，不处理
            data = {}
            data['status'] = 401
            data['message'] = u'no login'
            return HttpResponse(json.dumps(data), content_type="application/json")

    return warpper


# 装饰器，检查request参数是否齐全
def check_request(*params):
    def __check_request(func):
        def warpper(request):
            # print params
            # 遍历参数
            for param in params:
                # print param
                # 判断参数是否存在
                if not request.GET.has_key(param):
                    data = {}
                    data['status'] = 402
                    data['message'] = u'no params:%s' % param
                    return HttpResponse(json.dumps(data), content_type="application/json")

            # 参数都存在，则继续执行
            return func(request)

        return warpper

    return __check_request
