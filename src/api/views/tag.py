from django.shortcuts import render, redirect
from django.http import JsonResponse
from api.models import Tag, Post
from api.forms import TagForm
from api.serializers import TagListSerializers, PostListSerializers, TagCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

@api_view(['GET'])
def tags(request):
    tags = Tag.objects.all()
    spisok = TagListSerializers(tags, many = True)
    return Response({'data':spisok.data})

@api_view(['GET'])
def tag_details(request, tag_id):
    posts = Post.objects.filter(tags__id = tag_id)
    ser = PostListSerializers(posts, many = True)
    # for post in posts:
    #     spis.append({'title': post.title, 'body': post.body, 'id': post.id})
    return Response({'data': ser.data})

class TagListView(ListAPIView):
    serializer_class = TagListSerializers
    queryset = Tag.objects.all()

class TagDetailView(RetrieveAPIView):
    serializer_class = PostListSerializers
    queryset = Post.objects.all()
    lookup_field = 'tags__id'
    lookup_url_kwarg = 'tag_id'

class TagCreateView(CreateAPIView):
    serializer_class = TagCreateSerializer


def tags_detail(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags})

def tag_post_html(request, tag_id):
    posts=Post.objects.filter(tags__id=tag_id)
    return render(request, 'index.html', {'posts':posts})

def createtag(request):
    error = ''
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('api:tagdetail')
        else:
            error = 'Форма была неверной'

    form = TagForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'createtag.html', context)

def deletetag(request, tag_id):
    tag = Tag.objects.filter(id = tag_id).delete()
    return redirect('api:tagdetail')