from django.shortcuts import render
from accounts.forms import usercreationform
from django.http import HttpResponse
from myroom.models import background

def register(request):
    obj=background.objects.all()
    if request.method == "POST":
        form=usercreationform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=usercreationform()

    context={
    'form':form,
    'obj':obj
    }

    return render(request,'accounts/register.html',context)
