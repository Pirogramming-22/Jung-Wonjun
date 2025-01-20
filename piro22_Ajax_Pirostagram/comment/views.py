from django.shortcuts import render, redirect, get_object_or_404
from post.models import Post
from comment.models import Comment
from .forms import Commentform

def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == "POST":
        form = Commentform(request.POST)
        if form.is_valid():
            # 댓글 저장
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('comment:comment', post_id=post.id)
    else:
        form = Commentform()

    context = {
        'form': form,
        'post': post,
        'comments': comments,
    }
    return render(request, 'comment/comment.html', context)

def delete(request, post_id, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return redirect('comment:comment', post_id=post_id)