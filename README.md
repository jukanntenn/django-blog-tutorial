####Powered by python 3 and django 1.9

> Note:
> 目前项目共 2 个分支，blog-tutorial 分支为 Blog 教学项目，该项目附带有配套教程，请参考下方的链接。
>
> dev 分支为我的个人博客的分支，实现了诸多更为高级的特性，并会持续完善和改进以及添加新的功能。具体特性请查看 dev 分支的 readme 文件。

### 项目配套教程

注：如果你完全没有接触过 Django，强烈建议你首先阅读官方文档的入门教程，我们组织首页仓库也有其[中文翻译版本](https://github.com/djangoStudyTeam/django-intro-zh)，强烈推荐先阅读该教程以掌握 Django 开发中的一些基础知识。

**第一周**：[Django 学习小组：博客开发实战第一周教程 —— 编写博客的 Model 和首页面](http://www.jianshu.com/p/3bf9fb2a7e31)

**第二周**：[Django 学习小组：博客开发实战第二周教程 —— 博客详情页面和分类页面](http://www.jianshu.com/p/b74a6c5382c1)

**第三周**：[Django 学习小组：博客开发实战第三周教程——文章列表分页和代码语法高亮](http://www.jianshu.com/p/6c4615751854)

**第四周**：[Django 学习小组：博客开发实战第四周——标签云与文章归档](http://www.jianshu.com/p/1603c8494fed)

**第五周**：[Django 学习小组：博客开发实战第五周——基于类的通用视图详解（一）](http://www.jianshu.com/p/00bf223873b3)

**第六周**：[Django 学习小组：博客开发实战第六周教程 —— 实现评论功能](http://www.jianshu.com/p/8aadfa2a4ab6)

最佳实践一：[Django Blog 统计某个分类下有多少篇文章的优雅实现方法](http://www.jianshu.com/p/02db8f2ef200)

最佳实践二：[Django Blog 文章按发表时间自动归档的优雅解决方案](http://www.jianshu.com/p/3f846ecbd945)

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
