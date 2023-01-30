from django.shortcuts import render, get_object_or_404, redirect #重定向模块
from django.http import HttpResponse
from .models import ArticlePost
import markdown
from .forms import ArticlePostForm
from django.contrib.auth.models import User




def article_list(request):
    #取出所有博客文章
    articles = ArticlePost.objects.all()
    #需要传递给模板templates的对象
    context = {'articles':articles}
    #render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)

# def article_detail(request, id):
#     #取出相应的文章
#     article = ArticlePost.objects.get(id=id)
#     #需要传递给模板的对象
#     context = {'article': article }
#     #载入模板，并返回context对象
#     return render(request, 'article/detail.html', context)

def article_detail(request, id=None):
    article = get_object_or_404(ArticlePost, id=id)

    #将markdown语法渲染成html样式
    article.body  = markdown.markdown(article.body,
        extensions=[
            #包含缩写，表格等常用扩展
            'markdown.extensions.extra',
            #语法高亮扩展
            'markdown.extensions.codehilite',
            ])
            
    context = {'article': article}
    return render(request, 'article/detail.html', context)

def article_create(request):
    #判断用户是否提交数据
    if request.method == "POST":
        #将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data = request.POST)
        #判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            #保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            #指定数据库中id=1的用户位作者
            #如果你进行过删除数据表的操作，可能会找不到id=1的用户
            #此时请重新创建用户，并传入此用户的 id
            new_article.author = User.objects.get(id = 1)
            #将新文章保存到数据库中
            new_article.save()
            #完成后返回到文章列表
            return redirect("article:article_list")#这里冒号后不要有空格！
        #如果数据不满足模型要求
        else:
            return HttpResponse("标题或文章不能为空，请重新填写。")
    #如果用户请求获取数据
    else:
        #创建表达类实例
        article_post_form = ArticlePostForm()
        #赋值上下文
        context = {'article_post_form': article_post_form}
        #返回模板
        return render(request, 'article/create.html', context)

# def article_delete(request, id):
#     #根据id获取需要删除的文章
#     article = ArticlePost.objects.get(id=id)
#     #调用.delete()方法删除文章
#     article.delete()
#     #完成删除后返回文章列表
#     return redirect("article:article_list")

# use get_project_or_404 rewrite article_delete() fucntion

# def article_delete(request, id):
#     article = get_object_or_404(ArticlePost, id=id)
#     article.delete()
#     return redirect("article:article_list")

def article_safe_delete(request, id):
    if request.method == 'POST':
        article = get_object_or_404(ArticlePost, id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")

def article_update(request, id):
    """更新文章的视图，通过POST方法提交表单，更新title，body字段
        get方法进入初始表单页面
        id: 文章的id
    """
    article = get_object_or_404(ArticlePost, id=id)

    if request.method == "POST":
        #将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data = request.POST)
        #判断提交的数据是否满足模型要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("article:article_detail", id)
        else:
            return HttpResponse("标题或文章不能为空，请重新填写。")#这个地方之后写一个弹窗或者单独的html
    else:
        #如果用户GET请求获取数据
        article_post_form = ArticlePostForm()
        #赋值上下文，将article文章对象也传递进去， 以便提取旧的内容
        context = {'article':article, 'article_post_form':article_post_form}
        return render(request, 'article/update.html', context)

