from django.shortcuts import render
from . forms import studentregistration

# Create your views here.
def showsformdata(request):
    fm = studentregistration(auto_id="sulrt", label_suffix='', initial={"name":'wasim', 'email':'wasim@gamil.com',"mobilenumber":'8459555107'  })
    return render(request, 'core/stuinfo.html', {'form':fm})
