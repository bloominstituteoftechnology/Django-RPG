from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('armory/', views.view_all_armory, name='armory'),
]



# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('characters/', views.view_all_characters, name='characters'),
# ]
