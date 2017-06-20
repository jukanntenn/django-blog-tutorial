免费、中文、零基础，完整的项目，基于最新版 Django 1.10 和 Python 3.5。带你从零开始一步步开发属于自己的博客网站，帮助你以最快的速度掌握 Django 开发的技巧。

## 资源列表

- 项目演示：[Demo](http://demo.zmrenwu.com/)
- 教程：[Django 博客开发入门教程](http://zmrenwu.com/category/django-blog-tutorial/)
- 博客模板：[Blog templates](https://github.com/zmrenwu/django-blog-tutorial-templates)
- 答疑与求助：[Pythonzhcn - Python 中文社区](http://www.pythonzh.cn/)

## 分支说明

每篇教程的代码都位于项目相应的分支中，点击上方的 **Branch** 按钮可以查看到，例如分支 Step1_build-development-environment 对应第 1 篇教程 [1 - 搭建开发环境](http://zmrenwu.com/post/3/)。

master 主分支是项目的完整代码。

demo 分支是演示项目的分支代码。

## 在本地运行项目

1. 克隆项目到本地

   打开命令行，进入到保存项目的文件夹，输入如下命令：

   ```
   git clone https://github.com/zmrenwu/django-blog-tutorial.git
   ```

2. 创建并激活虚拟环境

   在命令行进入到保存虚拟环境的文件夹，输入如下命令创建并激活虚拟环境：

   ```
   virtualenv blogproject_env

   # windows
   blogproject_env\Scripts\activate

   # linux
   source blogproject_env/bin/activate
   ```

   关于如何使用虚拟环境，参阅：[搭建开发环境](http://zmrenwu.com/post/3/) 的 Virtualenv 部分。如果不想使用虚拟环境，可以跳过这一步。

3. 安装项目依赖

   如果使用了虚拟环境，确保激活并进入了虚拟环境，在命令行进入项目所在的 django-blog-tutorial 文件夹，运行如下命令：

   ```
   pip install -r requirements.txt
   ```

4. 迁移数据库

   在上一步所在的位置运行如下命令迁移数据库：

   ```
   python manage.py migrate
   ```

5. 创建后台管理员账户

   在上一步所在的位置运行如下命令创建后台管理员账户

   ```
   python manage.py createsuperuser
   ```

   具体请参阅 [在 Django Admin 后台发布文章](http://zmrenwu.com/post/9/)

6. 运行开发服务器

   在上一步所在的位置运行如下命令开启开发服务器：

   ```
   python manage.py runserver
   ```

   在浏览器输入：127.0.0.1:8000

7. 进入后台发布文章

   在浏览器输入：127.0.0.1:8000/admin

   使用第 5 步创建的后台管理员账户登录

   具体请参阅 [在 Django Admin 后台发布文章](http://zmrenwu.com/post/9/)

## 教程目录索引

**基础部分**

- [0 - Django 博客教程：前言](http://zmrenwu.com/post/2/)
- [1 - 搭建开发环境](http://zmrenwu.com/post/3/)
- [2 - 建立 Django 博客应用](http://zmrenwu.com/post/4/)
- [3 - 创建 Django 博客的数据库模型](http://zmrenwu.com/post/5/)
- [4 - 让 Django 完成翻译：迁移数据库](http://zmrenwu.com/post/6/)
- [5 - Django 博客首页视图](http://zmrenwu.com/post/7/)
- [6 - 真正的 Django 博客首页视图](http://zmrenwu.com/post/8/)
- [7 - 在 Django Admin 后台发布文章](http://zmrenwu.com/post/9/)
- [8 - 博客文章详情页](http://zmrenwu.com/post/10/)
- [9 - 支持 Markdown 语法和代码高亮](http://zmrenwu.com/post/11/)
- [10 - 页面侧边栏：使用自定义模板标签](http://zmrenwu.com/post/12/)
- [11 - 分类与归档](http://zmrenwu.com/post/13/)
- [12 - 评论](http://zmrenwu.com/post/14/)
- [13 - 已知小问题修正](http://zmrenwu.com/post/16/)
- [14 - 使用 Nginx 和 Gunicorn 部署 Django 博客](http://zmrenwu.com/post/20/)
- [15 - 使用 Fabric 自动化部署](http://zmrenwu.com/post/21/)

**进阶部分**

- [16 - 统计文章阅读量](http://zmrenwu.com/post/29/)
- [17 - 自动生成文章摘要](http://zmrenwu.com/post/32/)
- [18 - 基于类的通用视图：ListView 和 DetailView](http://zmrenwu.com/post/33/)
- [19 - Django Pagination 简单分页](http://zmrenwu.com/post/34/)
- [20 - Django Pagination 完善分页](http://zmrenwu.com/post/37/)
- [21 - 统计各个分类下的文章数](http://zmrenwu.com/post/38/)
- [22 - 标签云](http://zmrenwu.com/post/39/)
- [23 - RSS 订阅](http://zmrenwu.com/post/41/)
- [24 - 自动生成目录](http://zmrenwu.com/post/43/)
- [25 - 简单全文搜索](http://zmrenwu.com/post/44/)
- [26 - Django Haystack 全文检索与关键词高亮](http://zmrenwu.com/post/45/)

## 交流讨论和继续学习 Django

这里汇聚了大量经验丰富的 Django 开发者，遇到问题随时请教，以及获取更多的 Django 学习资料。

- Django 博客，更多 Django 开发文章和教程：[追梦人物的博客](http://zmrenwu.com/)
- Django 学习小组 QQ 群：561422498
- Django 学习交流论坛：[Pythonzhcn - Python 中文社区](http://www.pythonzh.cn/)
- Django 学习小组邮件列表：django_study@groups.163.com
- [Django 入门学习规划与资料推荐](http://zmrenwu.com/post/15/)