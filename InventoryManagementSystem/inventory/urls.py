from django.urls import path, include, re_path
from . import views

app_name = 'inventory'

urlpatterns = [

    path('homepage/', views.homepage, name='homepage'),
    path('new_inventory/', views.add_inventory, name='new_inventory'),
    
    path('<int:item_id>/listview/', views.list_view, name='listview'),
    path('<int:item_id>/new_item/', views.add_item, name='new_item'),
    
    path('<int:item_pk>/del_item/', views.delete_item, name='del_item'),
    path('<int:item_pk>/ed_item/', views.edit_item, name='edit_item'),
    path('<int:item_pk>/ed_save/', views.edit_save, name='edit_save'),
]
