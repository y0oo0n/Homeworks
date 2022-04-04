from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def list(request):
    hobby = Article.objects.filter(category='hobby')
    food = Article.objects.filter(category='food')
    programming = Article.objects.filter(category='programming')
    return render(request, 'list.html', {'hobby':hobby, 'food':food, 'programming':programming})


def new(request):
    if request.method == 'POST':
        #POST 요청일 경우
        print(request.POST)
        new_article = Article.objects.create(
            category = request.POST['category'],
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('detail', article_pk=new_article.pk)

    #POSt요청이 아닐 경우
    return render(request, 'new.html')

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})

def hobby(request):
    hobby = Article.objects.filter(category='hobby')
    return render(request, 'hobby.html', {'hobby':hobby})

def food(request):
    food = Article.objects.filter(category='food')
    return render(request, 'food.html', {'food':food})

def programming(request):
    programming = Article.objects.filter(category='programming')
    return render(request, 'programming.html', {'programming':programming})