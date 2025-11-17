from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.utils.translation import gettext as _


from cart.cart import Cart
from store import models as store_models


def index(request):
    return render(request, "cart/index.html", {
        "title": _("Shopping Cart")
    })


def add(request):
    cart = Cart(request)

    # if request.POST.get("action") == "POST":
    if request.method == "POST":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))

        print("product_id:", product_id)
        print("product_quantity:", product_quantity)

        product = get_object_or_404(store_models.Product, id=product_id)
        print(product)

        cart.add(product=product, quantity=product_quantity)
        print(cart.get())

        return JsonResponse({
            "success": "true",
            "product_title": product.title,
            "quantity": product_quantity
        })



    return HttpResponse("cart:add")

def update(request):
    return HttpResponse("cart:update")


def delete(request):
    return HttpResponse("cart:delete")
