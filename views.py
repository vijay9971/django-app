from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

def home(request):
    return render(request,'blog/home.html')


def create(request):
    form = BlogForm()
    if request.method =='POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    
    context= {'form':form}
    return render(request,'blog/create.html',context)


def displayBlog(request):
    blog = BlogModel.objects.all()
    context = {'blog' : blog}
    return render(request, 'blog/display.html',context)


def deletelist(request,id):
    blog = get_object_or_404(BlogModel,id=id)
    if request.method=='POST':
        blog.delete()
        return redirect('/')
    return render(request, 'blog/delete.html')




def updatelist(request,id):
    blog = get_object_or_404(BlogModel, id = id)
    form=BlogForm(instance=blog)
    if(request.method=="POST"):
        form=BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'form':form}
    return render(request,'blog/update.html',context)       
            




     

