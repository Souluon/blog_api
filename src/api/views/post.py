from django.shortcuts import render, redirect
from django.http import JsonResponse
from api.models import Post
from api.serializers import PostListSerializers, Post_detailsListSerializers, PostCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.forms import PostForm



# @api_view(['GET'])
# def posts(request):
#     posts = Post.objects.all()
#     spisok = PostListSerializers(posts, many = True)
#     return Response({'data': spisok.data})

@api_view(['GET'])
def post_details(request, post_id):
    post = Post.objects.get(id = post_id)
    ser = Post_detailsListSerializers(post)
    return Response({'data': ser.data})

class PostListView(ListAPIView):
    serializer_class = PostListSerializers
    queryset = Post.objects.all()

class PostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = Post_detailsListSerializers
    queryset = Post.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'

class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'post_details.html', {'post': post})

