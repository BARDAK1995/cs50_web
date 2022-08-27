from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from . import util
from markdown2 import markdown
from django.urls import reverse
from django.http import HttpResponseRedirect
from random import randint

def index(request):
    #print(request.GET["q"])

    # checks if the get input is a query one
    if "q" in request.GET:
        return proces_search_query(request)
    
    # meaning no query imput, simply lists all entries
    return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
            })


def entry_page(request,entry_title):
    #if user makes a search request in a entry page
    if "q" in request.GET:
        return proces_search_query(request)

    md_entry = util.get_entry(entry_title)
    #print(md_entry)
    if md_entry:
        HTML_entry = markdown(md_entry)
    else:
        HTML_entry=""
    #print(HTML_entry)
    return render(request, "encyclopedia/entry.html", {
        "entry_title": entry_title, "HTML_entry" : HTML_entry,
        "isentry" : 'yes'})

def proces_search_query(request):
    entryList = util.list_entries()
    entry_request = request.GET["q"]
    candidate_list = []

    for entry_name in entryList:
        # if searched name is found EXACTLY the we direct to that page
        if entry_name.lower() == entry_request.lower():
            return HttpResponseRedirect(f"{entry_name}")
            
        # searched string is in some other entries name, but not exactly the same
        elif entry_request.lower() in entry_name.lower():
            candidate_list.append(entry_name)
    # returns the populated candidate list
    return render(request, "encyclopedia/index.html", {
        "entries": candidate_list
        })


def new_page(request):
    # if the request is port, meaning the entry is entered
    if request.method == "POST":
        new_title = request.POST["title"]
        markdown_txt = request.POST["markdown_txt"]
        #check if entry already exists
        if new_title in util.list_entries():
            return render(request, "encyclopedia/FAIL.html")
        util.save_entry(new_title,markdown_txt)
        return HttpResponseRedirect(f"{new_title}")
    else:
        return render(request, "encyclopedia/newpage.html")

def edit_page(request):
    if request.method == "POST":
        entry_title = request.POST["title"]
        markdown_txt = request.POST["markdown_txt"]
        util.save_entry(entry_title, markdown_txt)
        return HttpResponseRedirect(f"{entry_title}")
    else:
        entry_title = request.GET["edit_title"]
        markdown_data = util.get_entry(entry_title)
        return render(request, "encyclopedia/edit.html",{"entry_title":entry_title, "markdown_input":markdown_data })


def random_page(request):
    entryList = util.list_entries()
    entry_index = randint(0, len(entryList)-1)
    rnd_entry_title = entryList[entry_index]
    return HttpResponseRedirect(f"{rnd_entry_title}")