from django.shortcuts import render 

def table(request):
    num1 = None
    table = {}

    if request.method == 'POST':
        num1 = request.POST.get('num1')  # Get input from form
        if num1:  
            try:
                num1 = int(num1)  # Convert to integer
                table = {i: i * num1 for i in range(1, 11)}
            except ValueError:
                num1 = None  # Handle cases where conversion fails

    return render(request, 'table.html', {'num': num1, 'table': table})
