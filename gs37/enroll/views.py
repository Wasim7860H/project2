from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  print(fm)
  print('YE POST REQUEST SE AAYA HAI')
   
 else:
  fm = StudentRegistration()
  print('YE GIT REQUEST SE AAYA HAI')

 return render(request, 'enroll/userregistration.html', {'form':fm})
