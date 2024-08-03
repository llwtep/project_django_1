from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import PostCreateForm
from .models import Post
from django.views.generic.list import ListView
def main(request):
    return render(request, 'main/main.html')


class PostListView(ListView):
    model = Post
    ordering = ['-created_at']
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@login_required
def PostCreationView(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('main')
    else:
        form = PostCreateForm()
    return render(request, 'posts/post-create.html', {'form': form})


