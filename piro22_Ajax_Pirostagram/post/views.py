from django.shortcuts import render, redirect
from .models import Post
from .forms import Postform
from comment.models import Comment
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# Create your views here.
def list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/list.html', context)


def create(request):
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post/list.html')
        else:
            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'post/create.html', context)
    else:
        form = Postform()
        context = {
            'form': form,
        }
        return render(request, 'post/create.html', context)


def detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Post.comments.all()
    context = {
        'post': post,
        'comments':comments,
    }
    return render(request, 'post/detail.html', context)


@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']

    post = Post.objects.get(id=post_id)

    if button_type == 'like':
        post.like += 1
    post.save()

    return JsonResponse({'id':post_id, 'type':button_type})