from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    title = 'Магазин'
    phone1 = 'IPhone 16'
    phone2 = 'Samsung Galaxy S24'
    phone3 = 'Honor Magic 6 Pro'
    context = {'title': title,
               'phone1': phone1,
               'phone2': phone2,
               'phone3': phone3,
               }
    return render(request, 'third_task/shop.html', context)

def cart(request):
    return render(request, 'third_task/cart.html')
