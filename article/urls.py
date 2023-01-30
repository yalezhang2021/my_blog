from django.urls import path
from . import views #引入views.py

#正在部署的应用的名称
#这里我们正在article，因为article里面以后会有其他更多的内容
#每个新的内容都会有自己在article之下的url
app_name = 'article'

urlpatterns = [
    #path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
    #article detail
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    #article create
    path('article-create/', views.article_create, name='article_create'),
    #article delete
    #path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    #article safe delete
    path('article-safe-delete/<int:id>/',
          views.article_safe_delete,
          name='article_safe_delete'),
    #article update, edit
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    
]