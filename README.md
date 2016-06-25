####Powered by python 3.4 and django 1.9

> Note:
目前项目共三个分支，master 和 blog-tutorial 分支为纯粹的 Blog 项目，该项目的配套教程，会在每周的周五发布到简书、CSDN、开发者头条等平台，如果你对文档、代码等有任何建议，敬请反馈给我们。我们期待更多的反馈意见，这才能使我们更好改进该项目。
> 
develop 分支为 django 中国社区的开发分支，敬请有一定 django 开发经验的朋友加入到该项目中来，随时贡献您的代码，或者为我们的代码提供改进意见等，我们欢迎任何的意见。


**注意：master 分支的代码将在 7月1日清空，blog 项目的开发者到时请重新 fork 并合并 blog-tutorial 分支的代码**

### 小组招新
我们尝试将企业级的开发流程引入项目小组，目前我们项目组已有4名后台开发人员和2名经验丰富的前端人员。如果你在产品设计、UI 设计、项目测试、JS框架等有自己的经验和见解，敬请加入我们的小组。如有意请发送邮件至 zmrenwu@163.com，随时恭候。

### 项目配套教程

注：如果你完全没有接触过 Django，强烈建议你首先阅读官方文档的入门教程，我们组织首页仓库也有其[中文翻译版本](https://github.com/djangoStudyTeam/django-intro-zh)，强烈推荐先阅读该教程以掌握 Django 开发中的一些基础知识。

**第一周**：[Django 学习小组：博客开发实战第一周教程 —— 编写博客的 Model 和首页面](http://www.jianshu.com/p/3bf9fb2a7e31)

**第二周**：[Django 学习小组：博客开发实战第二周教程 —— 博客详情页面和分类页面](http://www.jianshu.com/p/b74a6c5382c1)

**第三周**：[Django 学习小组：博客开发实战第三周教程——文章列表分页和代码语法高亮](http://www.jianshu.com/p/6c4615751854)

**第四周**：[Django 学习小组：博客开发实战第四周——标签云与文章归档](http://www.jianshu.com/p/1603c8494fed)

**第五周**：[Django 学习小组：博客开发实战第五周——基于类的通用视图详解（一）](http://www.jianshu.com/p/00bf223873b3)

**第六周**：[Django 学习小组：博客开发实战第六周教程 —— 实现评论功能](http://www.jianshu.com/p/8aadfa2a4ab6)

### 项目运行方式
确保你的开发环境是 python3，如果不是，请考虑使用虚拟环境virtualenv搭建python3, 自行度娘并参照相关教程。

1. fork 本项目到你的仓库
2. 克隆你的仓库到本地
3. 命令行执行 pip install -r requirements.txt（注意在 requirements.txt 所在目录下执行，否则请输入完整路径名）安装依赖包
4. 迁移数据库，在 manage.py 所在目录执行 

        python manage.py makemigrations
        python manage.py migrate

5. 类似步骤4，运行命令创建超级用户
    
        python manage.py createsuperuser

6. 类似步骤4、5，在 manage.py 所在目录执行 

        python manage.py runserver

7. 浏览器输入 http://127.0.0.1:8000/

### 贡献人员名单：
JFluo2011，bdbai

### Django 学习小组简介
django学习小组是一个促进 django 新手互相学习、互相帮助的组织。

小组在一边学习 django 的同时将一起完成几个项目，包括：

- 一个简单的 django 博客，用于发布小组每周的学习和开发文档；
- django中国社区，为国内的 django 开发者们提供一个长期维护的 django 社区；

上面所说的这个社区类似于 segmentfault 和 stackoverflow ，但更加专注（只专注于 django 开发的问题）。

你也可以加入我们的邮件列表 django_study@groups.163.com ，随时关注我们的动态。我们会将每周的详细开发文档和代码通过邮件列表发出。

如有任何建议，欢迎提 issue，欢迎 fork，pr，当然也别忘了 star 哦！
