from django.shortcuts import render
from django.http import HttpResponse
from .models import order

# Create your views here.
def home(request):
    
    return render(request, 'index.html')
  #  return render(request,'index.html')
  
def orders(request):
    if request.method == "POST":
        print("hello")
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('num')
        food = request.POST.get('ord')
        addr = request.POST.get('addr')  # Match the name attribute in the textarea
        # No need to get 'date' from POST data, as 'add_date' is automatically set to current date and time

        contact = order(name=name, email=email, phone=phone, food=food, address=addr)
        contact.save()
        
        return render(request, 'index.html', {'order_received': True})

    return HttpResponse("Order received successfully!")
    
