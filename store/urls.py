from django.urls import path

from store import views


app_name = "store"
urlpatterns = [

    path("", views.index, name="index"),
    path("categories/", views.categories_list, name="categories_list"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("categories/all/", views.categories_all, name="categories_all"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail")
]