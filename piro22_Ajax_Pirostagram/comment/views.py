from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from post.models import Post
from .forms import Commentform

def create(request, post_id):
    # 요청된 게시물 가져오기
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = Commentform(request.POST)
        if form.is_valid():
            # 댓글 저장하기 전에 게시물 연결
            comment = form.save(commit=False)
            comment.post = post  # 외래키 연결
            comment.save()
            return redirect('post/detail', pk=post.id)  # 게시물 상세 페이지로 리디렉션
    else:
        form = Commentform()
        context = {
            'form': form,
            'post': post,
            'errors': form.errors,
        }
        return render(request, 'comment/create.html', context)