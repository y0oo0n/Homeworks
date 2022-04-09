from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def list(request):
    articles = Article.objects.all()
    hobby = Article.objects.filter(category='hobby')
    food = Article.objects.filter(category='food')
    programming = Article.objects.filter(category='programming')
    return render(request, 'list.html', {'articles':articles, 'hobby':hobby, 'food':food, 'programming':programming})


def new(request):
    if request.method == 'POST':
        #POST 요청으로 온 데이터 확인
        print(request.POST)
        #데이터가 잘 왔나 확인하기 위해 프린트 한 번 진행
        Article.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
        )
        return redirect('list')

    #POSt요청이 아닐 경우
    return render(request, 'new.html')

def detail(request, article_id):
    article_detail = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article_detail':article_detail})

def hobby(request):
    hobby = Article.objects.filter(category='hobby')
    return render(request, 'hobby.html', {'hobby':hobby})

def food(request):
    food = Article.objects.filter(category='food')
    return render(request, 'food.html', {'food':food})

def programming(request):
    programming = Article.objects.filter(category='programming')
    return render(request, 'programming.html', {'programming':programming})