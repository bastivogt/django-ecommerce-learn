from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.translation import gettext as _

from store import models




def index(request):
    products_featured = models.Product.objects.filter(published=True, featured=True)
    return render(request, "store/index.html", {
        "title": _("Home"),
        "products_featured": products_featured
    })


def categories_list(request):
    categories_all = models.Category.objects.all()
    return render(request, "store/categories_list.html", {
        "title": _("Categories"),
        "categories_all": categories_all
    })

def category_detail(request, slug):
    category = get_object_or_404(models.Category, slug=slug)
    products = category.products.filter(published=True)

    return render(request, "store/category_detail.html", {
        "title": category.name,
        "category": category,
        "products": products
    })




def product_detail(request, slug):
    product = get_object_or_404(models.Product, slug=slug, published=True)

    return render(request, "store/product_detail.html", {
        "title": product.title,
        "product": product
    })



