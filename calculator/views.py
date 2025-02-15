from django.shortcuts import render

# Create your views here.
def cal(request):
    result=None
    error=None
    if request.method=='POST':
        try:
            num1=float(request.POST.get('num1','2'))
            num2=float(request.POST.get('num2'))
            operation=request.POST.get('operation')
            if operation=="add":
                result=num1+num2
            elif operation=="substract":
                result=num1-num2
            elif operation=="multiply":
                result=num1*num2
            elif operation=="divide":
                if num2==0:
                    error="Error:divide by zero not allowed"
                else:
                    result=num1/num2
            else:
                error="invalid operation selected"
        except ValueError:
            error="inavalid please enter valid operation"

    return render(request, 'cal.html',{'result':result ,'error':error})
