from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import ProductModel

# Create your views here.


def home(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        # image2 = request.POST.get('image')
        print(name)
        # print(type(image2))
        print(price)
        print(type(image))


        product = ProductModel.objects.create(name=name, price=price,image=image)
        return redirect(to='/show/', request=request)

    return render(template_name= 'home.html', request=request)



def show(reqeust: HttpRequest):
    product_list = ProductModel.objects.all()
    print(reqeust.get_host())

    return render(template_name='show.html' , request=reqeust, context={'list':product_list, 'host':reqeust.get_host})
