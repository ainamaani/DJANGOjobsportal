from django.shortcuts import render,redirect
from . models import Jobs

# Create your views here.

def home(request):
    return render(request, 'home.html')

def newjob(request):
    if request.method=="POST":
        title = request.POST['title']
        description = request.POST['description']
        company = request.POST['company']
        email = request.POST['email']

        job = Jobs.objects.create(title=title,description=description,company=company,email=email)
        job.save()
        return redirect(request.build_absolute_uri('/home'))
    return render(request, 'jobform.html')

def jobs(request):
    jobs = Jobs.objects.all()

    return render(request, 'jobs.html',{
        'jobs':jobs
    })

def details(request,id):
    jobdetails = Jobs.objects.get(id=id)

    return render(request, 'details.html',{
        'jobdetails':jobdetails
    })
