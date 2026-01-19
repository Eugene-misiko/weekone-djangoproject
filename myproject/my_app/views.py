from django.shortcuts import render,redirect
from django.utils import timezone
from .models import FoodItem
# Create your views here.
def index(request):
    today = timezone.now().date()
    foods = FoodItem.objects.filter(date_added=today)
    total_carlories = sum(food.carlories for food in foods)

    if request.method == "POST":
        name = request.POST.get("name")
        carlories = request.POST.get("carlories")

        if name and carlories:
            FoodItem.objects.create(
                name=name,
                carlories=int(carlories),
                date_added=today
            )
            return redirect("index")

    context = {
        "foods": foods,
        "total_carlories": total_carlories,
    }

    return render(request, "index.html", context)


def delete_food(request, food_id):
    FoodItem.objects.filter(id=food_id).delete()
    return redirect("index")


def reset_day(request):
    today = timezone.now().date()
    FoodItem.objects.filter(date_added=today).delete()
    return redirect("index")
