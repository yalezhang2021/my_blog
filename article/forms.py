from socket import fromshare
from django import forms #y引入表单
from .models import ArticlePost #引入文章模型

#ArticlePostForm 类 继承了django的表单类 forms.ModelForm
#并在类中定义了内部类 class Meta
class ArticlePostForm(forms.ModelForm):
    class Meta:
        #指明数据模型来源
        model = ArticlePost
        #定义表单包含的字段
        fields = ('title', 'body')
        

