from django.shortcuts import render, redirect

from .models import News, Category, Color, Car


def index_view(request):
    categories = Category.objects.all()
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars, 'categories': categories})

# def car_detail_view(request, pk):
#     car = Car.objects.get(id=pk)
#     return render(request, 'app/car_detail.html', {'car': car})
#
# def category_view(request, category_title):
#     category = Category.objects.filter(category__title=category_title)
#     return render(request, 'app/category.html', {'category': category})

def news_create_view(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        news = News(title=title, description=description)
        news.save()
    return render(request, 'app/news_create.html')
def car_create_view(request):
    categories = Category.objects.all()
    colors = Color.objects.all()
    if request.method == "POST":
        title = request.POST['title']
        model = request.POST['model']
        color_id = request.POST['color_id']
        year = request.POST['year']
        odometer = request.POST['odometer']
        make = request.POST['make']
        engine_capacity = request.POST['engine_capacity']
        image = request.FILES['image']
        category_id = request.POST['category_id']

        category = Category.objects.get(id=category_id)
        color = Color.objects.get(id=color_id)

        car = Car(title=title,category=category, model=model, year=year, odometer=odometer,
                  make=make,engine_capacity=engine_capacity, image=image, color=color)
        car.save()
        return redirect(car_create_view)
    return render(request, 'app/car_create.html',context={'categories': categories, 'colors': colors})




