from django.urls import path
from . import views


app_name = 'offer'

urlpatterns = [
    path('', views.offer_list, name='offer_list'),
    path('<slug:category_slug>/', views.offer_list,
         name='offer_list_by_category'),
    path('<int:id>/<slug:slug>/', views.offer_detail,
         name='offer_detail'),
]
