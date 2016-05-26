# DjangoBlog 
####Powered by python 3.4 and django 1.9

> Note:
目前项目共两个分支，master 分支为纯粹的 Blog 项目，该项目的配套教程，会在每周的周五发布到简书、CSDN、开发者头条等平台，如果你对文档、代码等有任何建议，敬请反馈给我们。我们期待更多的反馈意见，这才能使我们更好改进该项目。
> 
feature 分支为 django 中国社区的开发分支，目前已经初步完成用户模块，见 usera app 文件，敬请有一定 django 开发经验的朋友加入到该项目中来，随时贡献您的代码，或者为我们的代码提供改进意见等，我们欢迎任何的意见。

**注意：已将 master 分支的一些代码移到了 feature 分支，以后 master 分支的代码更新进度将和教程保持严格一致。新功能代码请 pr 到 feature 分支。如果你觉得每周一更的教程速度太慢，请从 feature 分支获取最新的代码。**

### 小组招新
我们尝试将企业级的开发流程引入项目小组，目前我们项目组已有4名后台开发人员和2名经验丰富的前端人员。如果你在产品设计、UI 设计、项目测试、JS框架等有自己的经验和见解，敬请加入我们的小组。如有意请发送邮件至 zmrenwu@163.com，随时恭候。

### 项目配套教程

注：如果你完全没有接触过 Django，强烈建议你首先阅读官方文档的入门教程，我们组织首页仓库也有其[中文翻译版本](https://github.com/djangoStudyTeam/django-intro-zh)，强烈推荐先阅读该教程以掌握 Django 开发中的一些基础知识。

**第一周**：[Django 学习小组：博客开发实战第一周教程 —— 编写博客的首页面](http://www.jianshu.com/p/3bf9fb2a7e31)

### 项目运行方式
确保你的项目版本是 python 3

1. fork 本项目到你的仓库
2. 克隆你的仓库到本地
3. 命令行执行 pip install -r requirements.txt（注意在 requirements.txt 所在目录下执行，否则请输入完整路径名）安装依赖包
4. 迁移数据库，在 manage.py 所在目录执行 python manage.py migrate
5. 在 manage.py 所在目录执行 python manage.py runserver
6. 浏览器输入 http://127.0.0.1:8000/

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

