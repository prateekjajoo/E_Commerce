from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, ProductView, CartView, CheckOutView, RegisterView, ContactView
from .views import ProductDetailsView

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('product/<category_name>', ProductView.as_view(), name='product'),
    path('product/<category_name>/<subcategory_name>', ProductView.as_view(), name='product'),
    path('cart', CartView.as_view(), name='cart'),
    path('checkout', CheckOutView.as_view(), name='checkout'),
    path('register', RegisterView.as_view(), name='register'),
    path('contect', ContactView.as_view(), name='contect'),
    path('product_details/<int:pk>', ProductDetailsView.as_view(), name='product_details'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
