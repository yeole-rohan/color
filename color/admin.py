from django.contrib import admin
from .models import User, Banner, HomeBanner, Theme, ThemeCategory, Product, ProductSize, Gender, FrameSize, PageSize, Image, Color, Cart
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'first_name', 'last_name', 'phone_number')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id','first_image', 'second_image', 'third_image','long_banner_image', 'img_height', 'img_width')

@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_one', 'banner_two', 'banner_three', 'banner_four')

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'date', 'theme_image')

@admin.register(ThemeCategory)
class ThemeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'date', 'category_image')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'date')

class ColorInline(admin.StackedInline):
    model = Color
    extra = 1

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    def save_model(self, request, obj, form, change):
        obj.save()
        for image in request.FILES.getlist('image_multiple'):
            obj.product.create(product = image)
    list_display = ('id', 'creator', 'prodcut_description', 'cult_member_price', 'price')

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'product_sizes') 

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'product_related_to_gender')

@admin.register(FrameSize)
class FrameSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'size')

@admin.register(PageSize)
class PageSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'page_size')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'product_images')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'user', 'product')