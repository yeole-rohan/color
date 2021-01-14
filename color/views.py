from django.shortcuts import render, redirect
from .models import Banner, HomeBanner, ThemeCategory, Theme, Product, Image, Cart, User
from .forms import RegisterUser
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Project Views
 
def dashboard(request):
    get_replaceable_banner = Banner.objects.first()
    get_home_banners = HomeBanner.objects.first()
    get_all_theme_categories = ThemeCategory.objects.all()
    get_all_themes = Theme.objects.all()
    get_six_theme_categories = ThemeCategory.objects.all().order_by('-date')[:6]
    get_six_themes = Theme.objects.all().order_by('-date')[:6]
    get_cult_favs = Product.objects.all().order_by('-date')[:4]
    return render(request, template_name='dashboard.html', context={'get_all_theme_categories' : get_all_theme_categories, 'get_replaceable_banners' : get_replaceable_banner, 'get_home_banners' : get_home_banners, 'get_all_themes' : get_all_themes, 'get_cult_favs' : get_cult_favs, 'get_six_themes' : get_six_themes, 'get_six_theme_categories' : get_six_theme_categories })

def product_details(request, id):
    get_single_product = Product.objects.get(id=id)
    get_images = Image.objects.filter(product_for=get_single_product.id)
    single_cat = []
    single_theme = []
    for get_cat in get_single_product.product_category.all():
        single_cat.append(get_cat)
    
    for get_theme in get_single_product.product_theme.all():
        single_theme.append(get_theme) 
    get_similar_products_by_category = Product.objects.filter(product_category = single_cat[0]).order_by('-id')[:4]
    get_similar_products_by_theme = Product.objects.filter(product_theme = single_theme[0]).order_by('-id')[:4] 
    return render(request, template_name="pages/product-details.html", context={'get_single_product' : get_single_product, 'get_images' : get_images, 'get_similar_products' : get_similar_products_by_category, 'get_similar_products_by_theme' : get_similar_products_by_theme})

def search(request, cat, id):
    get_all_theme_categories = ThemeCategory.objects.all()
    get_all_themes = Theme.objects.all()
    get_home_banners = HomeBanner.objects.first()
    get_products_by_category_or_theme = ''
    try:
        get_products_by_category_or_theme = Product.objects.filter(product_category = id, product_theme = id).order_by('-date')
    except:
        pass
    paginator = Paginator(get_products_by_category_or_theme, 12)  # 1 posts in each page
    page = request.GET.get('page')
    try:
        get_products_by_category_or_theme = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        get_products_by_category_or_theme = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        get_products_by_category_or_theme = paginator.page(paginator.num_pages)
    return render(request, template_name="pages/search.html", context={'get_all_theme_categories' : get_all_theme_categories, 'category_or_theme' : cat, 'get_all_themes' : get_all_themes, 'get_home_banners' : get_home_banners, 'get_products_by_category_or_theme' : get_products_by_category_or_theme, 'page': page})

'''Need to Create User'''

def add_to_cart(request, id):
    if request.method=="POST":
        id = request.POST.get('id')
        user  = User.objects.get(id = request.user.id)
        get_product = ''
        try:
            get_product = Product.objects.get(id = id)
        except:
            pass
        cart = Cart.objects.create(user=user, product = get_product.id)
        return JsonResponse({'status' : 'ok'})
    else:
        return JsonResponse({'status' : 'error'})
    return JsonResponse({'status' : 'ok'})


def about(request):
    return render(request, template_name = 'pages/about.html', context={})

def collaborate(request):
    register_member = RegisterUser(request.POST or None)
    return render(request, template_name = 'pages/collaborate.html', context={'register_member' : register_member})

def membership(request):
    return render(request, template_name = 'pages/membership.html', context={})