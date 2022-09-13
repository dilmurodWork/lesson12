from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag

# Create your views here.
class NewsView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news.html'

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    news = News.objects.filter(tegs=tag)
    context = {
        'tag':tag,
        'news':news,
    }
    return render(request, 'home.html', context)