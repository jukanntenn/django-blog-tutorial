from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .forms import CommentForm


def post_comment(request, post_pk):
    # 先获取被评论的文章，
    # 因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 django 提供的一个快捷函数 get_object_or_404
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；
    # 否则返回 404 页面给用户。
    post = get_object_or_404(Post, pk=post_pk)

    # http 请求有 get 和 post 两种方法，
    # 一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST
        # 我们利用这些数据构造了 CommentForm 的实例，
        # 这样 django 的表单就生成了
        form = CommentForm(request.POST)

        # 当调用 form.is_valid() 方法时，
        # django 自动帮我们检查表单的数据是否符合格式要求
        if form.is_valid():
            # 检查到数据是合法的，
            # 调用表单的 save 方法保存数据到数据库
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例
            # 但还不保存数据到数据库
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.post = post
            # 最终将评论数据保存进数据库，
            # 调用模型实例的 save 方法
            comment.save()

            # 重定向到 post 的详情页
            return redirect(post)

        else:
            # 检查到数据不合法，
            # 重新渲染详情页，
            # 并且渲染表单的错误
            # 因此我们传了三个模板变量给 detail.html
            # 一个是文章（Post），
            # 一个是评论列表，
            # 一个是表单 form
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)

    # 不是 post 请求，
    # 说明用户没有提交数据，
    # 重定向到文章详情页
    return redirect(post)
