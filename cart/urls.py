from django.urls import path

from cart import views

app_name = "cart"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete")
]
