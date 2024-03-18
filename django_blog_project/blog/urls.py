from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.PostListView.as_view(),name="blog-home"),
    path('About/',views.About,name="blog-About"),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name="post-detail"),
     path('post/new/',views.PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update/',views.UpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name="post-delete")
]
