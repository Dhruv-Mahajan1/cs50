from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import util
from django import forms
import markdown
import random
from django.urls import reverse


class NewEnteryForm(forms.Form):
    
    title = forms.CharField(label="title")
    description= forms.CharField(widget=forms.Textarea(attrs={'style':'bottom:2rem'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def gettitle(request,title):
    entery=util.get_entry(title)
    if entery!=None:
        return render(request, "encyclopedia/entery.html", {
            "title":title,
            "entry": markdown.markdown(entery)
        })
    else:
        return HttpResponse('<h1>Page not found</h1>')


def randomtitle(request):
    enteries=util.list_entries()
    title=random.choice (enteries)
    return gettitle(request,title)

def search(request):
    title=request.GET.get("q").lower()
    allEnteries= util.list_entries()
    desiredEnteries=[]
    for entry in allEnteries:
        if title in entry.lower():
            desiredEnteries.append(entry)

    if len(desiredEnteries)==1:
        return gettitle(request,desiredEnteries[0])

    return render(request, "encyclopedia/searchresult.html", {
        "entries": desiredEnteries
    })
    
def createnewpage(request):
    if request.method=='POST':
        form = NewEnteryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            entries=util.list_entries()
            for entry in entries:
                if title in entry.lower():
                    return HttpResponse('<h1>Title already in the database</h1>')
            util.save_entry(title,description)        
            return HttpResponseRedirect(reverse("index"))
    else:
        form = NewEnteryForm()
    return render(request, 'encyclopedia/createpage.html', {'form': form})


def editentry(request,title):
    entry=util.get_entry(title.lower())
    data = {'title':title,'description':entry} 
    form = NewEnteryForm(initial=data)
    return render(request, 'encyclopedia/edit.html', {'form': form,'title':title})
    
def saveedit(request,title):
    if request.method=='POST':
        form = NewEnteryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            util.save_entry(title,description)        
            return HttpResponseRedirect(reverse( "gettitle",kwargs={'title':title}))
    