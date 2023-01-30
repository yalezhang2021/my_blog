from django.db import models 
from django.contrib.auth.models import User #导入内建的user模型
from django.contrib import admin
import datetime
from django.utils import timezone

# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)

    # 文章正文。保存大量文本使用 TextField
    body = models.TextField()

    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    #额外定义一些内容，规范ArticlePost中数据的行为
    class Meta:
        #ordering 指定模型返回的数据的排列顺序
        #'-created'表明数据以倒序排列
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
