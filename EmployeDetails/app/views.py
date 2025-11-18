from django.shortcuts import render,redirect
from app.forms import employe_from
# Create your views here.
from app.models import employe_model
def Employedetails(request):
    data = employe_model.objects.all()
    context = {
        'data':data
    }
    return render(request,'frontend_app1/table.html',context)

def emp_form(request):
    form = employe_from
    if request.method == 'POST':
        form = employe_from(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emptable')
    else:
        form = employe_from
    contest = {
        'form':form
    }
    return render(request,'frontend_app1/form.html',contest)