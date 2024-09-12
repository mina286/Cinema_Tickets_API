from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('guests_crud',views.Viewsets_Guests)
router.register('movie_crud',views.Viewsets_Movie)
router.register('reverstion_crud',views.Viewsets_Reverstion)

app_name = 'tickets'
urlpatterns = [
    # 1
    path('no_rest_model/',views.no_rest_model,name='no_rest_model'),
    # 2 
    path('no_rest_but_from_model/',views.no_rest_but_from_model,name='no_rest_but_from_model'),
    #  3.1 GET POST
    path('fbv_list/',views.fbv_list,name='fbv_list'),
    # 3.2 GET PUT DELETE
    path('fbv_pk_guest/<int:pk>/',views.fbv_pk_guest,name='fbv_pk_guest'),
    # 3.3 GET POST
    path('fbv_list_reservtion/',views.fbv_list_reservtion,name='fbv_list_reservtion'),
    # 4.1 GET POST class based views
    path('CBV_List/',views.CBV_List.as_view(),name='CBV_List'),
    # 4.2 GET PUT DELETE class based views
    path('CBV_PK/<int:pk>/',views.CBV_PK.as_view(),name='CBV_PK'),
    # 5.1 GET POST mixins
    path('Mixins_List/',views.Mixins_List.as_view(),name='Mixins_List'),
    # 5.2 GET PUT DESTROY mixins
    path('Mixins_pk/<int:pk>/',views.Mixins_pk.as_view(),name='Mixins_pk'),
    # 6.1 GET POST Generics
    path('Generics_List/',views.Generics_List.as_view(),name='Generics_List'),
    # 6.2 GET PUT DELETE Generics
    path('Generics_PK/<int:pk>/',views.Generics_PK.as_view(),name='Generics_PK'),
    # 7.1  viewsets
    path('Viewsets_Guests/',include(router.urls),name='Viewsets_Guests'),
    path('Viewsets_Movie/',include(router.urls),name='Viewsets_Movie'),
    path('Viewsets_Reverstion/',include(router.urls),name='Viewsets_Reverstion'),
    # 8 find movie
    path('find_movie/',views.find_movie,name='find_movie'),
    # 9 create new reverstion
    path('new_reservation/',views.new_reservation,name='new_reservation'),





]
