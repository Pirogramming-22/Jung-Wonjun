from django.shortcuts import render, redirect
from apps.tool.models import Tool
from apps.tool.forms import Toolform

def list(request):
    tools = Tool.objects.all()
    context = {
        'tools': tools,
    }
    return render(request, 'tool/list.html', context)


def detail(request, pk):
    tool = Tool.objects.get(id=pk)
    context = {
        'tool': tool,
    }
    return render(request, 'tool/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = Toolform(request.POST, request.FILES)
        if form.is_valid():
            tool = form.save()
            return redirect(f'detail/{tool.pk}', tool.pk)
        else:
            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'tool/create.html', context)
    else:
        form = Toolform()
        context = {
            'form': form,
        }
        return render(request, 'tool/create.html', context)


def update(request, pk):
    tool = tool.objects.get(id=pk)
    if request.method == 'POST':
        form = Toolform(request.POST, request.FILES, instance=tool)
        if form.is_valid():
            form.save()
            return redirect(f'detail/{pk}', pk)
        else:
            context = {
                'tool': tool,
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'tool/update.html', context)
    else:
        form = Toolform(instance=tool)
        context = {
            'form': form,
        }
        return render(request, 'tool/update.html', context)