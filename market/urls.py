from django.conf.urls import patterns, url

from market import views

urlpatterns = patterns(
    "",
    url(r"^items$", views.items, name="items"),
    url(r"^shopping$", views.shopping, name="shopping")
    )
