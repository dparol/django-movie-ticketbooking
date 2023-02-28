from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_name = models.CharField(max_length=200,null=True,blank=True)
    date_of_release=models.DateField(null=True,blank=True)
    def __str__(self):
        return self.movie_name

class Theater(models.Model):
    theater_name=models.CharField(max_length=200,null=True,blank=True)
    NoOfScreen=models.IntegerField(null=True,blank=True)
    Movies=models.ForeignKey(Movies,on_delete=models.CASCADE,null=True,blank=True)
    



    def __str__(self):
        return self.theater_name


class Seat(models.Model):
    Theater=models.ForeignKey(Theater,on_delete=models.CASCADE,null=True,blank=True)
    no=models.CharField(max_length=5)
    show=models.ForeignKey("Screen", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.no



   



class Screen(models.Model):
    Theater=models.ForeignKey(Theater,on_delete=models.CASCADE,null=True, blank=True)
    Screen=models.CharField(max_length=20,null=True,blank=True)
    show_movie=models.ForeignKey(Movies,on_delete=models.CASCADE,null=True, blank=True)
    show_time=models.TimeField()
    available_seat=models.IntegerField(default=80)
    

    def __str__(self):
        return self.Screen









