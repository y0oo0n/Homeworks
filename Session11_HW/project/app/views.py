from django.shortcuts import render, redirect
from .models import Song, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    songs = Song.objects.all()
    
    return render(request, 'home.html', {'songs':songs})

@login_required(login_url="/registration/login")
def new(request):
    if request.method == 'POST':
        title = request.POST['title'],
        content = request.POST['content'],
        new_song = Song.objects.create(
            title=title, content=content, author=request.user
        )
        return redirect('song', new_song.pk)
    
    return render(request, 'new.html')

@login_required(login_url="/registration/login")
def song(request, song_pk):
    song = Song.objects.get(pk=song_pk)
    print(type(song.author), "song.author")
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            song=song,
            content=content,
            author=request.user
        )
        return redirect('song', song_pk)
    return render(request, 'song.html', {'song':song})

def edit(request, song_pk):
    song = Song.objects.get(pk=song_pk)

    if request.method == 'POST':
        Song.objects.filter(pk=song_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('song', song_pk)

    return render(request, 'edit.html', {'song':song})

def delete(request, song_pk):
    song = Song.objects.get(pk=song_pk)
    song.delete()

    return redirect('home')

def delete_comment(request, song_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('song', song_pk)

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        found_user = User.objects.filter(username=username)
        if len(found_user) :
            error = "이미 아이디가 존재합니다"
            return render(request, "registration/signup.html", {"error":error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect("home")
    return render(request, "registration/signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:   
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
                )
            return redirect(request.GET.get("next", "/"))
        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, "registration/login.html", {"error":error})

    return render(request, "registration/login.html")

def logout(request):
    auth.logout(request)

    return redirect("home")
