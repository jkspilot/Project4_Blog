# Project4_Blog
Project4-Blog应用程序设计（2022280432）
```bash
Project4/
├── accounts/ # 用户认证应用 (课程示例代码)
├── learning_logs/ # 学习日志应用 (课程示例代码)
├── blogs/ # 博客应用 (本实验新增)
│ ├── migrations/ # 数据库迁移文件
│ ├── templates/ # HTML模板
│ │ └── blogs/
│ │ ├── index.html # 博客首页
│ │ ├── detail.html # 文章详情页
│ │ ├── new_post.html # 发布文章页
│ │ └── edit_post.html # 编辑文章页
│ ├── init.py
│ ├── admin.py # 管理后台配置
│ ├── apps.py
│ ├── forms.py # 文章表单
│ ├── models.py # BlogPost数据模型
│ ├── tests.py
│ ├── urls.py # 博客URL路由
│ └── views.py # 视图函数
├── ll_projects/ # 项目主配置目录
│ ├── init.py
│ ├── settings.py # Django设置
│ ├── urls.py # 主URL路由
│ └── wsgi.py
└── manage.py # Django管理脚本（课程示例代码提供）
实验用到的命令行指令：
应用数据库迁移
python manage.py migrate
创建超级用户
python manage.py createsuperuser
```
