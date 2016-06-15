# coding:utf-8
__author__ = 'Haddy Yang(Ysh)'
__start_date__ = '2016-06-12'
"""
    likes views
"""
from django.shortcuts import render
from django.http import HttpResponse
import json

from likes.models import Likes, LikesDetail
from django.contrib.contenttypes.models import ContentType

# 导入likes下自定义的装饰器
from .decorator import check_login, check_request


@check_login
@check_request('type', 'id', 'direct')
def likes_change(request):
    u"""处理改变点赞状态
        Method: GET
        params: 
            type  : object type
            id    : object id
            direct: -1 or 1 (add like or remove like)
        return: json
    """
    # 创建json对象需要的数据
    data = {}
    data['status'] = 200
    data['message'] = u'ok'
    data['nums'] = 0

    # 获取数据
    obj_type = request.GET.get('type')
    obj_id = request.GET.get('id')
    user = request.user

    direct = 1 if request.GET.get('direct') == '1' else -1
    c = ContentType.objects.get(model=obj_type)

    # 获取Likes对象
    try:
        l = Likes.objects.get(content_type=c, object_id=obj_id)
    except Exception, e:
        # 没有获取到对象，则新增一个Likes对象
        l = Likes(content_type=c, object_id=obj_id)
    data['nums'] = l.likes_num

    # 获取Likes明细对象
    try:
        detail = LikesDetail.objects.get(likes=l, user=user)
    except Exception, e:
        detail = LikesDetail(likes=l, user=user, is_like=False)
    liked = 1 if detail.is_like else -1

    # 判断是否赞过，或者取消赞
    if liked == direct:
        data['status'] = 403
        data['message'] = u'Invalid operation'
    else:
        # 更新记录
        l.likes_num += direct
        if l.likes_num < 0:
            l.likes_num = 0
        l.save()
        data['nums'] = l.likes_num

        # 修改明细
        detail.is_like = direct == 1
        detail.save()

    # 返回结果
    return HttpResponse(json.dumps(data), content_type="application/json")


@check_request('type', 'id')
def likes_nums(request):
    u"""单独获取点赞的数量（也可以访问Likes模型获取数量）
        Method: GET
        params: 
            type  : object type
            id    : object id
        return: json
    """
    # 创建json对象需要的数据
    data = {}
    data['status'] = 200
    data['message'] = u'ok'
    data['nums'] = 0

    try:
        # 获取对象模型
        obj_type = request.GET.get('type')
        obj_id = request.GET.get('id')
        c = ContentType.objects.get(model=obj_type)

        # 根据模型和id获取likes对象
        l = Likes.objects.get(content_type=c, object_id=obj_id)

        # 获取数量
        data['nums'] = l.likes_num
    except Exception, e:
        data['nums'] = 0

    # 返回结果
    return HttpResponse(json.dumps(data), content_type="application/json")
