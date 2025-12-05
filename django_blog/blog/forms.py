from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from taggit.forms import TagField


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    tags = TagField(widget=forms.TextInput(attrs={'placeholder': 'Add tags (comma separated)'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include all necessary fields here
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your blog post content here...'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

