from django.urls import path
from .import views


urlpatterns = [
    #/genre/
    path('',views.index.as_view(),name='index'),

    #/genre/1(1 represents the id of the collection chosen by the user)
    path('<pk>/',views.details.as_view(),name='details'),

    path('register/',views.UserFormView.as_view(),name='userform'),
]