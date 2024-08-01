from django.shortcuts import render
from django.utils import timezone

from .models import Post
from django.views.generic.list import ListView
def main(request):
    return render(request, 'main/main.html')


class PostListView(ListView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


