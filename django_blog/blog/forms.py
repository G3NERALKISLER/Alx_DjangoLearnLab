from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment,Tag

# Allow editing User basic info
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

# Allow editing Profile info
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. django, python, blog'})
    )
    class Meta:
        model = Post
        fields = ['title', 'author']
   
    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
        # handle tags
        tags_str = self.cleaned_data.get('tags', '')
        tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]
        post.tags.clear()
        for name in tag_names:
            tag_obj, created = Tag.objects.get_or_create(name=name.lower())
            post.tags.add(tag_obj)
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your comment...',
                'class': 'form-control'
            }),
        }

    def clean_content(self):
        content = (self.cleaned_data.get('content') or '').strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(content) < 2:
            raise forms.ValidationError("Comment is too short.")
        return content

