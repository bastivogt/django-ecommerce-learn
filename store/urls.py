from django.urls import path

from store import views


app_name = "store"
urlpatterns = [

    path("", views.index, name="index"),
    path("categories/", views.categories_list, name="categories_list"),
    path("category/<str:slug>/", views.category_detail, name="category_detail"),
    path("product/<str:slug>/", views.product_detail, name="product_detail")
]