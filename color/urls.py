from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('about-us/', views.about, name="about_us"),
    path('collaborate/', views.collaborate, name="collaborate"),
    path('membership/', views.membership, name="membership"),
    path('product/<int:id>/', views.product_details, name="product-details"),
    path('search/<str:cat>/<int:id>', views.search, name="search"),
    path('add-to-cart/<int:id>/', views.add_to_cart, name="cart"),
]