from django.shortcuts import render
from . form import Studentregistration

# Create your views here.
def studentinfo(request):
    fm = Studentregistration(auto_id=True)
    return render(request, 'core/home.html', {'form':fm})
