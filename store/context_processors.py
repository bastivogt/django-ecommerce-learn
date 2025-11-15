from store import models

def categories(request):
    categories_all = models.Category.objects.all()
    return {
        "categories_all": categories_all
    }