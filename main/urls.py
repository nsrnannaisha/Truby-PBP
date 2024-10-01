from django.urls import path
from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, main_view

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product', add_product, name='add_product'),
    path('json/', show_json, name='json'),
    path('xml/', show_xml, name='xml'),
    path('json/<str:id>/', show_json_by_id, name='json_by_id'),
    path('xml/<str:id>/', show_xml_by_id, name='xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<str:id>', edit_product, name='edit_product'),
    path('delete/<str:id>', delete_product, name='delete_product'),
    path('', main_view, name='home'),
]