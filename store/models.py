from django.db import models
from django.utils.translation import gettext as _
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

class BaseTimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))
    class Meta:
        abstract = True


class Category(BaseTimeStampMixin):
    name = models.CharField(max_length=250, db_index=True, verbose_name=_("name"))
    slug = models.SlugField(max_length=250, unique=True, verbose_name=_("slug"))

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("store:category_detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name_plural = _("categories")
        ordering = [
            "name"
        ]
    

class Size(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = [
            "name"
        ]



class Product(BaseTimeStampMixin):
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, null=True, related_name="products", verbose_name=_("category"))
    title = models.CharField(max_length=250, verbose_name=_("title"))
    # available_sizes = models.ManyToManyField(Size, blank=True, related_name="products_size")
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.SET_NULL, related_name="products_size", verbose_name=_("size"))
    brand = models.CharField(max_length=250, default="un-branded", verbose_name=_("brand"))
    description = models.TextField(blank=True, verbose_name=_("description"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("slug"))
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=_("price"))
    image = models.ImageField(upload_to="images/", verbose_name=_("image"))
    featured = models.BooleanField(default=False, verbose_name=_("featured"))
    published = models.BooleanField(default=True, verbose_name=_("published"))

    def __str__(self):
        return self.title
    

    def delete(self, *args, **kwargs):
        self.image.delete()
        return super().delete(*args, **kwargs)
    
    @admin.display(description=_("Image preview"))
    def get_image_tag(self):
        if self.image:
            img_tag = f'<img src="{self.image.url}" title="{self.title}" alt="{self.title}" style="width: 80px; height: 80px; object-fit:cover;" />'
            return format_html(img_tag)
        return None
    
    @property
    def short_description(self):
        return self.description[:150] + " [...]"
    
    # @admin.display(description=_("Available sizes"))
    # def available_sizes_str(self):
    #     sizes = self.available_sizes.all()
    #     sizes_list = [item.name for item in sizes]
    #     return ", ".join(sizes_list)
    
    def get_absolute_url(self):
        return reverse("store:product_detail", kwargs={"slug": self.slug})
    

    class Meta:
        verbose_name_plural = _("products")
        ordering = [
            "-created_at"
        ]



