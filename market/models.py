from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=255)
    my_price = models.DecimalField(max_digits=15, decimal_places=2)
    in_stock = models.IntegerField()
    in_build = models.IntegerField()
    in_need = models.IntegerField()
    total_sold = models.IntegerField()

    def __unicode__(self):
        return self.item_name

class Material(models.Model):
    material_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.material_name

class ItemMaterial(models.Model):
    item = models.ForeignKey("Item")
    material = models.ForeignKey("Material")
    quantity = models.IntegerField()

    def __unicode__(self):
        return self.item.item_name + " - " + self.material.material_name
