from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'fourth_task/index.html')

def shop(request):
    title = 'Смартфоны'
    phones = ['IPhone 16', 'Samsung Galaxy S24', 'Honor Magic 6 Pro']
    context = {'title': title,
               'phones': phones,
               }
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')
