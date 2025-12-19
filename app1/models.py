
from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=800, null=True, blank=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email
class BusDetail(models.Model):
    bus_name = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    source_time = models.TimeField(blank=True, null=True)
    dest_time = models.TimeField(blank=True, null=True)
    driver_name=models.CharField(max_length=30,null=True,blank=True)
    mobile=models.PositiveIntegerField(null=True,blank=True)
    password=models.CharField(max_length=30,null=True,blank=True)
    nos = models.IntegerField(null=True,blank=True)
    rem = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.bus_name
class Seat(models.Model):
    bus = models.ForeignKey(BusDetail, on_delete=models.CASCADE)
    nos = models.IntegerField(blank=True, null=True)
    timing=models.DateTimeField(blank=True, null=True)
    booked_by_user = models.CharField(max_length=200, blank=True)
    


class Route(models.Model):
    bus=models.ForeignKey(BusDetail,on_delete=models.CASCADE,null=True,blank=True)
    Location=models.CharField(max_length=50,null=True,blank=True)
    marked=models.BooleanField(default=False,blank=True,null=True)
    marked_time=models.TimeField(null=True,blank=True)

    def __str__(self):
        return self.Location
