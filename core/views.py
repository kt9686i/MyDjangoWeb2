from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
   posts = Post.objects.all()
   return render(request, 'posts/index.html', {
       'posts':posts,
   })

def show(request, pk):
   #post = Post.objects.get(pk=pk) #posts = Post.objects.get(id=pk)
   post = get_object_or_404(Post, pk=pk)  #弄出404錯誤畫面
   return render(request, 'posts/show.html', {
       'post': post,
   })

def new():
   pass

def edit():
   pass

def delete():
   pass
