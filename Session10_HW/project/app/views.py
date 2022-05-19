from django.shortcuts import render, redirect
from .models import Song, Comment

# Create your views here.
def home(request):
    songs = Song.objects.all()
    
    return render(request, 'home.html', {'songs':songs})

def new(request):
    if request.method == 'POST':
        new_song = Song.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('song', new_song.pk)
    
    return render(request, 'new.html')

def song(request, song_pk):
    song = Song.objects.get(pk=song_pk)

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            song=song,
            content=content
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