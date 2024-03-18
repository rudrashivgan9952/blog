from django.forms import BaseModelForm
from django.shortcuts import render,HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

def Home(request):
    context={
        'posts':Post.objects.all(),
        'title':"Rudra's project"
    }
    return render(request,'blog/Home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blog/Home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author=self.request.user
        return super().form_valid(form)

class UpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self) -> bool | None:
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
       
    
def About(request):
    return render(request,'blog/About.html')


class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self) -> bool | None:
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
        