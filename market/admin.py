from django.contrib import admin
import market.models

admin.site.register(market.models.Item)
admin.site.register(market.models.Material)
admin.site.register(market.models.ItemMaterial)
