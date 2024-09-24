from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Article

# Create your views here.

# def index(request):
#     context = {}
#     return render(request, 'index.html', context)


class IndexView(ListView):

    template_name = 'index.html'
    queryset = Article.objects.filter(is_published=True).order_by('-created')[:6]
    context_object_name = 'articles'

    def get_context_data(self, **kwargs: Any):
        context  = super().get_context_data(**kwargs)
        popular_articles = Article.objects.filter(is_published=True).values('uuid', 'title').order_by('-views')[:5]
        context['popular_articles'] = popular_articles
        return context
    
index = IndexView.as_view()


### Article 一覧ページ
class ArticleListView(ListView):

    template_name = 'article/list.html'
    queryset = Article.objects.filter(is_published=True).order_by('-created')
    context_object_name ='articles'
    paginate_by = 10

article_list = ArticleListView.as_view()

### Article 詳細ページ
class ArticleDetailView(DetailView):
    template_name = 'article/detail.html'
    queryset = Article.objects.filter(is_published=True)
    context_object_name = 'article'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get(self, request, *args,**kwargs):
        get = super().get(request, *args, **kwargs)
        context = get.context_data

        # increment views
        article =self.object
        article.views = +1
        article.save()

        recommend = Article.objects.filter(is_published=True).order_by('views').last()
        context['recommend'] = recommend

        return get

article_detail = ArticleDetailView.as_view()