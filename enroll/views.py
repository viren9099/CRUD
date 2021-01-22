from django.shortcuts import render , HttpResponseRedirect
from enroll import views
from .models import Student

# Create your views here.

def add_show(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        try:
            all_user = Student.objects.all()
            print(name,email,password)
            Student.objects.create(name=name,email=email,password=password)
            msg = "student created successfully"
            return render(request,'addandshow.html',{'msg':msg,'all_user': all_user})
        except:
            msg = "fill form properly"
            return render(request,'addandshow.html',{'msg':msg})
    else:
        all_user = Student.objects.all()
        return render(request,'addandshow.html',{'all_user': all_user})    
    
def update_data(request,id):
    if request.method=="POST":
        get_update_user = Student.objects.get(pk=id)   
        
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        updated_user = Student.objects.filter(id=id).update(name=request.POST['name'],email=request.POST['email'],password=request.POST['password'])
        get_update_user = Student.objects.get(pk=id)
        # return render(request,'update.html',{'id':id,'get_update_user':get_update_user})
        
    else:    
        get_update_user = Student.objects.get(pk=id)
        
    return render(request,'update.html',{'id':id,'get_update_user':get_update_user})
        
def delete_data(request,id):
    if request.method=="POST":
        delete_user = Student.objects.get(pk=id)
        delete_user.delete()
        return HttpResponseRedirect('/')
        