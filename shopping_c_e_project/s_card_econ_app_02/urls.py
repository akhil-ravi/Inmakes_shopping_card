from django.urls import path

from s_card_econ_app_02 import views
app_name = 's_card_econ_app_02'

urlpatterns = [
    path('',views.searchResult,name='searchResult'),
]