from django.urls import path, re_path
from .import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    # path('products/', views.all_products, name='all_products'),
    # path('products/<int:product_id>', views.products_details_by_id, name='products_by_id'),
    # path('products/name/<str:product_name>', views.products_details_by_name, name='products_by_name'),
    # path('filter-products/', views.filter_products, name = "filter_products"),
    
    # Regular expression
    re_path(r'^$', views.home, name = 'home'),
    re_path(r'^about/$', views.about, name = 'about'),
    re_path(r'^user/(?P<username>[a-zA-Z0-8_]+)/$', views.user, name = 'user'),
    re_path(r'^blog/(?P<year>\d{4})/(?P<month>0[1-9]|1[0-2])/(?P<slug>[-\w]+)/$', views.blog, name='blog')

]