from django.urls import path
from .views import tags, tag_details, post_details, PostListView, PostDetailView, TagListView, TagDetailView, PostCreateView, TagCreateView, index, create, post_detail, tags_detail, createtag, tag_post_html, deletepost, deletetag



app_name = 'api'

urlpatterns = [
    path('', index, name='home'),

    path('posts/', PostListView.as_view(), name="posts"),
    path('tags/', TagListView.as_view(), name="tags"),
    path('tag/<int:tag_id>', TagDetailView.as_view()),
    path('post/<int:post_id>', PostDetailView.as_view()),
    path('create', create, name='create'),
    path('create2', PostCreateView.as_view()),
    path('createtag', TagCreateView.as_view()),


    path('postform/<int:post_id>', post_detail, name="postdetail"),
    path('tagsform/', tags_detail, name="tagdetail"),
    path('createtags', createtag, name="createtags"),
    path('tag_post_html/<int:tag_id>', tag_post_html, name="tagposts"),
    path('deletepost/<int:post_id>', deletepost, name="deletepost"),
    path('deletetag/<int:tag_id>', deletetag, name="deletetag"),
]
