from django.shortcuts import render
from . import serializers
from .serializers import Theaterserializer,Screenserializer,Seatserializer,movieserializer
from rest_framework.generics import CreateAPIView,ListAPIView
from .models import Theater,Seat,Movies,Screen
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.db.models import Q

# Create your views here.




class Theaterlist(ListAPIView):
    queryset=Theater.objects.all()
    queryset=Movies.objects.all()
    permission_classes = [AllowAny]

    def get(self,request):
        data=Theater.objects.all()
        serializer=Theaterserializer(data,many=True)
        return Response(serializer.data)


class Theaterwiselist(ListAPIView):
    queryset=Movies.objects.all()
    queryset=Theater.objects.all() 
    permission_classes = [AllowAny]

    
    def get(self,requset,id):
            data=Theater.objects.filter(theater_name__icontains=id)
            print(data)
            serializer=Theaterserializer(data,many=True)
            return Response(serializer.data)
    
class Theaterscreen(ListAPIView):
    queryset=Screen.objects.all()
    queryset = Seat.objects.all()

    permission_classes = [AllowAny]

    def get(self,request,id):
        data=Screen.objects.filter(Theater__id=id)
        serializer=Screenserializer(data,many=True)
        return Response(serializer.data)
class createTheaterscreen(CreateAPIView):
    permission_classes = [AllowAny]

    queryset=Screen.objects.all()
    serializer_class=Screenserializer
    def post(self,request):
        data=request.data
        theater_id=request.data.get('Theater',None)
        screen=request.data['Screen']
        print(screen)
        show_movie_id=request.data['show_movie']
        available_seat=request.data['available_seat']
        show_time=request.data['show_time']
        theater=Theater.objects.get(id=theater_id)
        show_movie=Movies.objects.get(id=show_movie_id)
        
        newscreen=Screen.objects.create(
            Theater=theater,
            Screen=screen,
            show_movie=show_movie,
            show_time=show_time,
            available_seat=available_seat,
            )
        serializer=Screenserializer(newscreen,many=False)
        return Response(serializer.data)



class ticketbook(CreateAPIView):
    serializer_class=Seatserializer
    queryset=Seat.objects.all()
    permission_classes = [AllowAny]

    def post(self,request):
        seat_no=request.data.get("seat_no",None)
        if seat_no:
            theater=request.data.get('Theater',None)
            theatre_id = Theater.objects.get(id=theater)
            show=request.data.get('show',None)
            screen=Screen.objects.get(id=show)
            if show:
                for each in seat_no:
                    booking = Seat.objects.create(
                        no=each,
                        Theater=theatre_id,
                        show=screen
                    )
        return Response("successfuly created")
   


class AllMovies(ListAPIView):
    serializer_class=movieserializer
    queryset = Movies.objects.all()
    permission_classes = [AllowAny]
    def get(self,request):
        allmovies=Movies.objects.all()
        serializer=movieserializer(allmovies,many=True)
        return Response(serializer.data)
    def post(self,request):
        queryset=Movies.objects.all()
        data=request.data
        newmovie=Movies.objects.create(
     
            movie_name=request.data['movie_name'],
            date_of_release=request.data['date_of_release']

        )
        allmovies=Movies.objects.all()
        serializer=movieserializer(allmovies,many=True)
        
        return Response(serializer.data)



class specific_movie(CreateAPIView):
    queryset=Movies.objects.all()
    serializer_class=movieserializer
    permission_classes = [AllowAny]

    def put(self,request,id):
        movie=Movies.objects.get(id=id)
        serializer=movieserializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,id):
        queryset=Movies.objects.all()
        data=Movies.objects.get(id=id)
        serializer=movieserializer(data,many=False)
        return Response(serializer.data)

    def delete(self,request,id):
        try:

            movie=Movies.objects.get(id=id)
            movie.delete()
            return Response({'message':'movie successfully removed'})
        except :
            return Response({'message':"we can't find the specific movie"})



class availableseat(ListAPIView):
    serializer_class = Seatserializer
    queryset = Seat.objects.all()
    queryset = Screen.objects.all()
    queryset = Theater.objects.all()
    permission_classes = [AllowAny]
    
    def get(self,request,**kwargs):
        theater_id=kwargs['theater_id']
        screen_id=kwargs['screen_id']
        seat=Seat.objects.filter( Q(Theater=theater_id) | Q(show=screen_id)).count()
        theater=Theater.objects.get(id=theater_id)
        screen=Screen.objects.get(id=screen_id)
        screen_name=screen.Screen
        movie=screen.show_movie.movie_name
        theater_name=theater.theater_name
        availableseat=80-int(seat)


        context={
            movie,
            theater_name,
            screen_name,
            availableseat,

        }
        return Response(context)
        
