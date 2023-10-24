from django.urls import path
from . import views 


urlpatterns=[
    
    path('navbar', views.navbar, name='navbar'),
    path('categories',views.categories, name='categories'),
    path('footer',views.footer, name='footer'),
   
    path('carousel',views.carousel, name='carousel'),
    path('index',views.index, name='index'),
    path('',views.content, name='content'),
    path('search/',views.search, name='search'),
    path('base',views.base, name='base'),
  
   
    path('nav', views.nav, name='nav'),
    path('category_products',views.category_products, name='category_products'),
 
  
]