####Powered by python 3 and django 1.9

> Note:
> 目前项目共 2 个分支，blog-tutorial 分支为 Blog 教学项目，该项目附带有配套教程，具体特性请查看 blog-tutorial 分支的 readme 文件。
>
> dev 分支为我的个人博客的分支，实现了诸多更为高级的特性，并会持续完善和改进以及添加新的功能。具体特性请参考下方说明。

**演示地址**：yangxg.top

**Features**
- 博客文章 markdown 渲染
- 文章侧栏分类统计和标签云
- 文章按照发表时间自动归档
- 评论，二级评论
- 全文搜索
- 登录，注册，用户管理（完成度 90%）
- 第三方账号登录（完成度 50%）
- 评论@某人通知提醒（完成度 50%）
- 点赞 （完成度 50%）

（标示了完成度的特性仍在开发中，只在后台开发，前台暂无演示）

### 项目运行方式
确保你的开发环境是 python3，如果不是，请考虑使用虚拟环境virtualenv搭建python3, 自行度娘并参照相关教程。

1. fork 本项目到你的仓库
2. 克隆你的仓库到本地
3. 在 weblog/ 下分别建立 static,media,database 文件夹
4. 命令行执行 pip install -r requirements.txt（注意在 requirements.txt 所在目录下执行，否则请输入完整路径名）安装依赖包（项目依赖 pillow，确保你的环境能够安装 pillow）
5. 迁移数据库，在 manage.py 所在目录执行

        python manage.py makemigrations
        python manage.py migrate

6. 类似步骤4，运行命令创建超级用户
    
        python manage.py createsuperuser

7. 类似步骤4、5，在 manage.py 所在目录执行

        python manage.py runserver

8. 浏览器输入 http://127.0.0.1:8000/
