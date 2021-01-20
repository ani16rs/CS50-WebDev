from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    if "tasks" not in request.session:                              # look in the session, if tasks doesn't exist
        request.session["tasks"] = []                               # then create it

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]                           # render the tasks of the session
    })

def add(request): 
    if request.method == "POST":
        form = NewTaskForm(request.POST)                            # Take in the data the user submitted and save it as form

        if form.is_valid():
            task = form.cleaned_data["task"]                        # isolate new 'task' from 'cleaned' version of request.form
            request.session["tasks"] += [task]                      # add new task to session tasks
            return HttpResponseRedirect(reverse("tasks:index"))     # redirect after submitting
        else:
            return render(request, "tasks/add.html", {              # if form is invalid, re-render add.html using same info
                "form": form
            })

    return render(request, "tasks/add.html", {                      # render add.html as request.method != POST
        "form": NewTaskForm()
    })