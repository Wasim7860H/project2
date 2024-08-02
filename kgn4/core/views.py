from django.shortcuts import render
from core.models import Stu_list

# Create your views here.
def stu_list(request):
    wasim = Stu_list.objects.all()
    return render(request, 'core/coreinfo.html', {'name':wasim})

