from django.shortcuts import render
from core.models import Student

# Create your views here.
def student(request):

    stud = Student.objects.all()
    print('Myoutput', stud)
    return render(request, 'core/studetails.html', {'stu':stud})

