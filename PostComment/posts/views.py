from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Employee
from django.contrib.auth import authenticate, login
from .forms import PostForm, ReplyForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def posts_home(request):
    post = Post.objects.all().filter
    query = request.GET.get("q")
    if query:
        post = post.filter(
            Q(messageType__icontains=POST) |
            Q(dateTimeStamp__icontains=query)
        ).distinct()

        return render(request, 'posts/index.html', {
            'post': post,

        })
    else:
        return render(request, 'posts/index.html', {'post': post})

def posts_detail(request, messageId):
    post = get_object_or_404(Post, messageId=messageId)

    return render(request, 'posts/detail.html', {'post': post})




def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()


        return render(request, 'posts/detail.html', {'post': post})
    context = {
        "form": form, }
    return render(request, 'posts/form.html', context)

def post_reply(request, messageId):
    form = ReplyForm(request.POST or None)
    post = get_object_or_404(Post, messageId=messageId)



    if form.is_valid():
        reply = form.save(commit=False)
        reply.save()

        return render(request, 'posts/detail.html', {'post': post})
    context = {'post': post, 'form': form, }
    return render(request, 'posts/create_reply.html', context)

