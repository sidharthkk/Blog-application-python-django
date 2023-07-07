

# Create your views here.
from django.shortcuts import render
from myapp.models import addDetails

def project_view(request):
       return render(request,'home.html',{})

def newpost_view(request):
       return render(request,'newpost.html',{})

def addpost(request):
    title=request.POST.get("title")
    print(title)
    description = request.POST.get("description")
    print(description)
    blog=addDetails(title=title,description =description )
    blog.save()
    return render(request, 'newpost.html',{})

def home_view(request):
    blogs = addDetails.objects.all()
    print(blogs)
    context = {
        "addDetails": blogs,
    }
    return render(request, 'home.html', context)


def delete_project(request, pk):
    print("In delete")
    addDetails.objects.filter(pk=pk).delete()

    projects = addDetails.objects.all()
    print(projects)
    context = {
        'projects': projects
    }
    return render(request, 'home.html', context)