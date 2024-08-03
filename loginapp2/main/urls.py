from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(template_name='main/main.html'), name='main'),
    path('create-post', views.PostCreationView, name='post-create')

]
