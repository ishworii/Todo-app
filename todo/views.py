from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewTask


def home(request):
    context = {"todo_list": NewTask.objects.all()}
    return render(request, "todo/home.html", context=context)


def insert_item(request):
    content = request.POST.get("content")
    if content == "":
        return redirect("home")
    new_task = NewTask(title=content)
    new_task.save()
    return redirect("home")


def delete_item(request, id):
    item = NewTask.objects.get(id=id)
    item.delete()
    return redirect("home")
