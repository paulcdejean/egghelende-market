from django.shortcuts import render
from market.models import Item

def items(request):
    return render(request, "items.html", {"items": Item.objects.all()})
