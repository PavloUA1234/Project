from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def news_home(request):
    news = Articles.objects.order_by('-created_date')[:2]
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

def post_new(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.published_date = timezone.now()
            news.save()
            return redirect('news-detail', pk=news.pk)
    else:
        form = ArticlesForm()
    return render(request, 'news/post_edit.html', {'form': form})


def post_edit(request, pk):
    news = get_object_or_404(Articles, pk=pk)
    if request.method == "POST":
        form = ArticlesForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.published_date = timezone.now()
            news.save()
            return redirect('news-detail', pk=news.pk)
    else:
        form = ArticlesForm(instance=news)
    return render(request, 'news/post_edit.html', {'form': form})

