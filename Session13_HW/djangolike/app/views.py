from django.shortcuts import render, redirect
from .models import Post, Comment, Like, Scrap
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.user
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')

#좋아요 눌린 값에 False,True값 부여
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    is_like = False
    if not request.user.is_anonymous:
        like = Like.objects.filter(
            post=post,
            user=request.user
        )

        if like.count() > 0:
            is_like = True

    return render(request, 'detail.html', {"post":post, "is_like": is_like})

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post': post})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)


def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error': error})

        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')

    return render(request, 'registration/signup.html')


def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error': error})
        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))
    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='/registration/login')
def mypage(request):
    user = User.objects.get(username=request.user)
    posts = Post.objects.filter(author=user)

    return render(request, 'mypage.html', { "posts":posts  })

# 좋아요 (버튼 클릭 시 숫자 증가+red)
@csrf_exempt
def like(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        post_pk = request_body["post_pk"]

        like, is_liked = Like.objects.get_or_create(
            post = Post.objects.get(pk=post_pk),
            user = request.user
        )

        #좋아요 취소
        if not is_liked:
            like.delete()

        #좋아요 생성
        # else:
        #     Like.objects.create(
        #         post = Post.objects.get(pk=post_pk),
        #         user = request.user
        #     )

    post_likes = Like.objects.filter(
        post = Post.objects.get(pk=post_pk)
    )

    response = {
        'like_count' : post_likes.count(),
        'is_liked' : is_liked
    }

    return HttpResponse(json.dumps(response))

# 스크랩 (마이페이지에서 확인)
@csrf_exempt
def scrap(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        post_pk = request_body['post_pk']

        scrap, is_scrap = Scrap.objects.get_or_create(
            post=Post.objects.get(pk=post_pk),
            user=request.user
        )

        #스크랩 취소
        if not is_scrap:
            scrap.delete()

        #스크랩 생성
        # else:
        #     Scrap.objects.create(
        #         post = Post.objects.get(pk=post_pk),
        #         user = request.user
        #     )

    post_scraps = Scrap.objects.filter(
        post=Post.objects.get(pk=post_pk)
    )

    response = {
        'scrap_count' : post_scraps.count(),
        'is_scrap' : is_scrap
    }

    return HttpResponse(json.dumps(response))