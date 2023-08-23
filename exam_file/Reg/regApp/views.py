from django.shortcuts import get_object_or_404, render,redirect
from .forms import NewReg,EditReg
from .models import Registration

# Create your views here.

def index(request):
    return render(request,'regApp/index.html')


def registration(request):
    form = NewReg()
    if request.method == 'POST':
        form = NewReg(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(register)

    return render(request,'regApp/registeration.html',{
        'form':form
    })


def register(request):
    registrations = Registration.objects.all()
    return render(request,'regApp/register.html',{
        'registrations':registrations
    })


def edit(request,pk):
    u = get_object_or_404(Registration,pk=pk)
    if request.method == 'POST':
        form = EditReg(request.POST,request.FILES,instance= u)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = EditReg(instance=u)

    return render(request,'regApp/editregister.html',{
        'form':form,
    })

def delete(request,pk):
    u = get_object_or_404(Registration,pk=pk)
    u.delete()
    return redirect(register)


