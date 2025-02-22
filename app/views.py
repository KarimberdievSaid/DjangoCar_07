from unicodedata import category

from django.shortcuts import render, redirect
from django.db.models import Q
from .models import News, Category, Color, Car
from .forms import CarForm

def index_view(request):
    cars = Car.objects.all()
    if 'search' in request.GET:
        search =request.GET['search']
        cars = Car.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))

    return render(request, 'app/index.html', {'cars': cars})


def car_create_view_2(request):
    form = CarForm(request.POST, request.FILES)
    if form.is_valid():

        form.save()
        return redirect('index')
    form = CarForm()
    return render(request, 'app/car_create_2.html', {'form': form})


# def news_create_view(request):
#     if request.method == "POST":
#         title = request.POST['title']
#         description = request.POST['description']
#
#         news = News(title=title, description=description)
#         news.save()
#     return render(request, 'app/news_create.html')
def car_create_view(request):
    categories = Category.objects.all()
    colors = Color.objects.all()
    if request.method == "POST":
        title = request.POST['title']
        model = request.POST['model']
        description = request.POST['description']
        color_id = request.POST['color_id']
        year = request.POST['year']
        odometer = request.POST['odometer']

        engine_capacity = request.POST['engine_capacity']
        image = request.FILES['image']
        category_id = request.POST['category_id']

        category = Category.objects.get(id=category_id)
        color = Color.objects.get(id=color_id)

        car = Car(title=title,category=category, model=model, year=year, odometer=odometer,
                  engine_capacity=engine_capacity, image=image, color=color,description=description)

        car.save()
        return redirect(car_create_view)
    return render(request, 'app/car_create.html',context={'categories': categories, 'colors': colors})

def car_detail_view(request,pk):
    car = Car.objects.get(id=pk)

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect("detail", car.id)
    form = CarForm(instance=car)
    return render(request, 'app/car_detail.html', {'car': car, 'form': form})



def car_detail_view_2(request,pk):
    categories = Car.objects.all()
    colors = Color.objects.all()
    car = Car.objects.get(id=pk)

    if request.method == "POST":
        title = request.POST['title']
        model = request.POST['model']
        description = request.POST['description']
        color_id = request.POST['color_id']
        year = request.POST['year']
        odometer = request.POST['odometer']
        engine_capacity = request.POST['engine_capacity']
        image = request.FILES['image']
        category_id = request.POST['category_id']

        category = Category.objects.get(id=category_id)
        color = Color.objects.get(id=color_id)

        car.title = title
        car.model = model
        car.description = description
        car.year = year
        car.odometer = odometer
        car.engine_capacity = engine_capacity
        car.image = image
        car.color_id = color
        car.catategory_id = category
        car.save()
        return redirect('index')
    print(Car.objects.all())

    return render(request, 'app/car_detail_2.html',context={'car': car, 'colors': colors, 'categories': categories })

def car_delete_view(request,pk):
    car = Car.objects.get(id=pk)
    car.delete()
    return redirect('index')

