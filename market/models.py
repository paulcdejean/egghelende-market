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
