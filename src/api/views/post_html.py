from django.shortcuts import render, redirect
from django.http import JsonResponse
from api.models import Post, Tag
from api.serializers import PostListSerializers, Post_detailsListSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.forms import PostForm
from authe.models import Author


def index(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        posts = Post.objects.filter(author_id=request.user)
    # posts = Post.objects.filter('-id')
    return render(request, 'index.html', {'posts': posts})

def create(request):
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                note = form.save(commit = False)
                note.author = request.user
                note.save()
                return redirect('api:home')
            else:
                error = 'Форма была неверной'

        form = PostForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'create.html', context)
    return redirect('authe:login')

def deletepost(request, post_id):
    post = Post.objects.filter(id = post_id).delete()
    return redirect('api:home')

