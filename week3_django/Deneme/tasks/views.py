from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.http import HttpResponseRedirect
# Create your views here.
tasks = ["foo", "bar", "baz"]

# to automate the form generation
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index0(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

#INDEX SESSIONS
def index(request):
    if "tasks" not in request.session:
        # If not, create a new list
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "GET":
        return render(request, "tasks/add.html")
    else:
        task = request.POST["task"]
        tasks.append(task)
        return render(request, "tasks/add.html")

def add2(request):
    return render(request, "tasks/add2.html", {
        "form": NewTaskForm()
    })

def add3(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add3.html", {
                "form": form
            })
    else:
        return render(request, "tasks/add3.html", {
            "form": NewTaskForm()
        })