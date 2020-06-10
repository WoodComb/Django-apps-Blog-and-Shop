from django.shortcuts import render, redirect
from .models import Post
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
                        ListView,
                        DetailView,
                        CreateView)
# Create your views here.

'''
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'userpost/home.html', context)
'''

def user(request):
    return render(request, 'userpost/profile.html')

class PostListView(ListView):
    model = Post
    template_name = 'userpost/home.html'
    context_object_name = 'posts'
    ordering = ['-updated_at']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login-page')
    else:
        form = UserRegisterForm()
    return render(request, 'userpost/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'userpost/profile.html')
