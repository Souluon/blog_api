from .models import Post, Tag
from django.forms import ModelForm, TextInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "tags"]

class TagForm(ModelForm):
    class Meta:
        model = Tag
        exclude = ["id"]


