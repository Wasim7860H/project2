from django.shortcuts import render
from .forms import Studentregistration

# Create your views here.
def showformdata(request):
    fm = Studentregistration()
    return render(request, 'core/forms.html', 
    {'form':fm})
