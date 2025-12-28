from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

# 19-1要求：公开访问的主页
def index(request):
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blogs/detail.html', {'post': post})

# 19-5要求：仅注册用户可添加/编辑
@login_required
def new_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user  # 关联当前用户
            new_post.save()
            return redirect('blogs:detail', post_id=new_post.id)
    
    return render(request, 'blogs/new_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    # 19-5核心：验证用户只能编辑自己的文章
    if post.owner != request.user:
        return redirect('blogs:index')
    
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:detail', post_id=post.id)
    
    return render(request, 'blogs/edit_post.html', {'form': form, 'post': post})
