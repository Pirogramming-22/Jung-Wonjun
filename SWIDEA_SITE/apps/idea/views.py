from django.shortcuts import render, redirect
from apps.idea.models import Idea
from apps.idea.forms import Ideaform

# Create your views here.
def list(request):
    ideas = Idea.objects.all()
    context = {
        'ideas': ideas,
    }
    return render(request, 'idea/list.html', context)


def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {
        'idea': idea,
    }
    return render(request, 'idea/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = Ideaform(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect(f'detail/{idea.pk}', idea.pk)
        else:
            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'idea/create.html', context)
    else:
        form = Ideaform()
        context = {
            'form': form,
        }
        return render(request, 'idea/create.html', context)


def update(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == 'POST':
        form = Ideaform(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea:detail', pk=pk)
        else:
            context = {
                'idea': idea,
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'idea/update.html', context)
    else:
        form = Ideaform(instance=idea)
        context = {
            'form': form,
        }
        return render(request, 'idea/update.html', context)


def delete(request, pk):
    Idea.objects.get(id=pk).delete()
    return redirect('idea:list')