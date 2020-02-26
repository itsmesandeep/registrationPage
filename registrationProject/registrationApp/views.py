from django.shortcuts import render, redirect
from .models import Employee_registraion_data
from django.http import HttpResponse


# Create your views here.
def registrationView(request):
    if request.method == "POST":
        eid = request.POST.get('empid')
        uname = request.POST.get('uname')
        ename = request.POST.get('ename')
        eage = request.POST.get('eage')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        if pwd == cpwd:
            data = Employee_registraion_data(
                emp_id=eid,
                emp_name=ename,
                emp_username=uname,
                emp_age=eage,
                emp_gender=gender,
                emp_email=email,
                emp_mobile=mobile,
                emp_password=pwd
            )
            data.save()
            return render(request, 'registrationPage.html')
        else:
            return HttpResponse('<h1>Password Miss Matched</h1>')
    else:
        return render(request, 'registrationPage.html')


def loginView(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = Employee_registraion_data.objects.filter(emp_username=uname, emp_password=pwd)
        if user:
            edata = Employee_registraion_data.objects.filter(emp_username=uname)
            print(edata)

            context ={
                'edata':edata[0]
            }
            return render(request, 'employeeView.html',context)
        else:
            return HttpResponse("User Not Found")
    else:
        return render(request, 'login.html')


def updateView(request,pk):
    if request.method =="POST":
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        if pwd == cpwd:
            employeeData = Employee_registraion_data.objects.get(id = pk)
            employeeData.emp_id = request.POST.get('empid')
            employeeData.emp_username =uname= request.POST.get('uname')
            employeeData.emp_name = request.POST.get('ename')
            employeeData.emp_age = request.POST.get('eage')
            employeeData.emp_gender = request.POST.get('gender')
            employeeData.emp_email = request.POST.get('email')
            employeeData.emp_mobile = request.POST.get('mobile')
            employeeData.emp_password =pwd= request.POST.get('pwd')
            employeeData.save()
            user = Employee_registraion_data.objects.filter(emp_username=uname, emp_password=pwd)
            if user:
                edata = Employee_registraion_data.objects.filter(emp_username=uname)
                print(edata)

                context = {
                    'edata': edata[0]
                }
                return render(request, 'employeeView.html', context)

        else:
            return HttpResponse('<h1>Password Miss Match</h1>')

    else:

        data = Employee_registraion_data.objects.get(id=pk)

        if data.emp_gender == 'Male':
            male = True
        else:
            male = False
        context = {
            'data': data,
            'male': male
        }
        return render(request, 'updateData.html', context)


def deleteView(request,pk):
    edata = Employee_registraion_data.objects.get(id=pk)
    edata.delete()
    return redirect('login')
