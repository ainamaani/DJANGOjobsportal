from django.http import HttpResponseServerError
from django.shortcuts import render,redirect
from . models import Jobs

# Create your views here.

def home(request):
    return render(request, 'home.html')

def newjob(request):
    if request.method == "POST":
        try:
            title = request.POST['title']
            description = request.POST['description']
            company = request.POST['company']
            email = request.POST['email']
            location = request.POST['location']
            salary = request.POST['salary']
            jobtype = request.POST['jobtype']
            category = request.POST['category']
            contact = request.POST['contact']
            qualifications = request.POST['qualifications']
            skills = request.POST['skills']
            experience = request.POST['experience']
            aboutus = request.POST['aboutus']
            applicationmethod = request.POST['applicationmethod']

            job = Jobs.objects.create(title=title, description=description, company=company, email=email,
                                      location=location, salary=salary, jobtype=jobtype, category=category,
                                      contact=contact, qualifications=qualifications, skills=skills, experience=experience,aboutus=aboutus,
                                      applicationmethod=applicationmethod)
            job.save()
            return redirect('/home')
        except Exception as e:
            print(e)
            return HttpResponseServerError("An error occurred while saving the job.")
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
