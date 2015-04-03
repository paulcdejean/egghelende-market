from django.shortcuts import render
from market.models import Item
from django.http import HttpResponse

from market.models import Item
from market.models import Material
from market.models import ItemMaterial


def items(request):
    return render(request, "items.html", {"items": Item.objects.all()})

def shopping(request):
    # Hard coding this because I'm lazy.
    spacing = 15

    result = ""
    for material in Material.objects.all():
        total = 0
        for item_material in ItemMaterial.objects.filter(material=material):
            total += item_material.quantity * item_material.item.in_need
        result += str(total) + " " * (spacing - len(str(total)))
        result += material.material_name + "\n"
    return HttpResponse(result, content_type="text/plain")
