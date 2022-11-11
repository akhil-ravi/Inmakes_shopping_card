from django.urls import path
from . import views
app_name='s_card_econ_app'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),

]