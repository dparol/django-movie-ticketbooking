from django.urls import path
from . import views 

urlpatterns = [
    path('alltheater',views.Theaterlist.as_view(),name='alltheater'),
    path('alltheater/<str:id>',views.Theaterwiselist.as_view(),name='alltheater'),
    path('Theaterscreen/<int:id>',views.Theaterscreen.as_view(),name='Theaterscreen'),
    path('createTheaterscreen/',views.createTheaterscreen.as_view(),name='createTheaterscreen'),
    path('ticketbook/',views.ticketbook.as_view(),name='ticketbook'),
    path('allmovies/',views.AllMovies.as_view(),name='AllMovies'),
    path('single_movie/<int:id>',views.specific_movie.as_view(),name='specific_movie'),
    path('availableseat/<int:theater_id>/<int:screen_id>/',views.availableseat.as_view(),name='availableseat'),

    
]
