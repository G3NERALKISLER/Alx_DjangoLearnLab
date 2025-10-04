from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy,reverse
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html' # blog/post_list.html
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' # blog/post_detail.html
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html' # blog/post_form.html


def form_valid(self, form):
    # set the author to the logged-in user
    form.instance.author = self.request.user
    return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


def form_valid(self, form):
    # Ensure the author doesn't change
    form.instance.author = self.request.user
    return super().form_valid(form)


def test_func(self):
    post = self.get_object()
    return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post-list')


def test_func(self):
    post = self.get_object()
    return post.author == self.request.user
def homeView(request):
        return render(request, 'blog/base.html')
def PostView(request):
        posts = Post.objects.all()
        return render(request, 'blog/post.html', {'posts': posts})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log them in immediately
            return redirect('home')  # Use a URL name, not a template file
    else:
        form = UserCreationForm()

    return render(request, 'blog/register.html', {'form': form})

        
def Login_View(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect (request.POST)
        else:
                return redirect("home") 
    else:
        form = AuthenticationForm()
        return render(request, 'blog/login.html', {'form':form})

@login_required
def profile_view(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # Redirect back to profile page after saving
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comments/comment_list.html'
    context_object_name = 'comments'
    paginate_by = 20

    def get_queryset(self):
        self.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return Comment.objects.filter(post=self.post).order_by('created_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['post'] = self.post
        return ctx

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comments/comment_form.html'  # used if user visits create page directly

    def dispatch(self, request, *args, **kwargs):
        self.post = get_object_or_404(Post, pk=kwargs['post_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.post.pk})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comments/comment_form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comments/comment_confirm_delete.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk})

