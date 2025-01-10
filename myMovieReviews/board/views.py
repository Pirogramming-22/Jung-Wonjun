from django.shortcuts import render, redirect
from board.models import Board

# 리스트 페이지 (메인 페이지)
def board_list(request):
    boards = Board.objects.all()
    context = {
        'boards': boards,
    }
    return render(request, 'board/list.html', context)


# 디테일 페이지
def board_detail(request, pk):
    board = Board.objects.get(id=pk)
    hour = board.runtime//60
    minute = board.runtime%60
    runtime_display = f"{hour}시간 {minute}분"
    context = {
        'board': board,
        'runtime_display': runtime_display
    }
    return render(request, 'board/detail.html', context)


# 리뷰 추가 페이지
def board_create(request):
    if request.method == "POST":
        board = Board.objects.create(
            title = request.POST['title'],
            year = request.POST['year'],
            genre = request.POST.get('genre', ''),
            score = request.POST['score'],
            runtime = request.POST['runtime'],
            review = request.POST['review'],
            director = request.POST['director'],
            actor = request.POST['actor'],
        )
        return redirect('board:board_list')
    
    context = {
        'genres': Board.GENRE_CHOICES
    }
    return render(request, 'board/create.html', context)


# 리뷰 수정 페이지
def board_update(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST.get('title')
        board.year = request.POST.get('year')
        board.genre = request.POST.get('genre')
        board.score = request.POST.get('score')
        board.runtime = request.POST.get('runtime')
        board.review = request.POST.get('review')
        board.director = request.POST.get('director')
        board.actor = request.POST.get('actor')
        board.save()
        return redirect('board:board_detail', pk=board.pk)
    
    context = {
        'board': board,
    }
    return render(request, 'board/update.html', context)


def board_delete(request, pk):
    if request.method == "POST":
        board = Board.objects.get(id=pk)
        board.delete()
        return redirect('board:board_list')
    return redirect('board:board_list')
    