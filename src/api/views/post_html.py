from django.shortcuts import render, redirect
from django.http import JsonResponse
from api.models import Post, Tag
from api.serializers import PostListSerializers, Post_detailsListSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.forms import PostForm


def index(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'main/index.html', {'posts': posts})

def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('api:home')
        else:
            error = 'Форма была неверной'

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def deletepost(request, post_id):
    post = Post.objects.filter(id = post_id).delete()
    return redirect('api:home')