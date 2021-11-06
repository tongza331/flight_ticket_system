from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

SEAT_CLASS = (
    ('economy', 'Economy'),
    ('first', 'First')
)

TICKET_STATUS =(
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('CANCELLED', 'Cancelled')
)

GENDER = (
    ('male','MALE'),    #(actual_value, human_readable_value)
    ('female','FEMALE')
)
class User(AbstractUser): # Customer
    phone = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"

class Location(models.Model):
    city = models.CharField(max_length=64)
    city_thai = models.CharField(max_length=300)
    airport = models.CharField(max_length=64)
    airport_thai = models.CharField(max_length=300)
    code = models.CharField(max_length=3)
    country = models.CharField(max_length=64) # Only Thailand
    class Meta:
        db_table = "location"

    def __str__(self):
        return self.city
class Ticket(models.Model):
    fid = models.CharField(max_length=10,primary_key=True)
    origin = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="arrivals")
    flightnumber = models.CharField(max_length=50)
    amount = models.FloatField()
    airline_list = models.CharField(max_length=100)
    depart_time = models.TimeField(null=True, blank=True)
    depart_date = models.DateField(null=True, blank=True)
    return_time = models.TimeField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    seat_class = models.CharField(max_length=20, choices=SEAT_CLASS)
    pnr = models.CharField(max_length=256)
    class Meta:
        db_table = "ticket"
    def __str__(self):
        return f"{self.origin},{self.destination},{self.fid}"
class Customer(models.Model):
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER, blank=True)
    #passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flights")
    #flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="passengers")
    class Meta:
        db_table = "customer"
    def __str__(self):
        return f"Passenger: {self.first_name} {self.last_name}, {self.gender}"



class Schedule(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bookings", blank=True, null=True)
    ref_no = models.CharField(max_length=6, unique=True)
    customer = models.ManyToManyField(Customer, related_name="flight_tickets")
    flight = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="tickets", blank=True, null=True)
    flight_desdate = models.DateField(blank=True, null=True)
    flight_arrdate = models.DateField(blank=True, null=True)
    flight_fare = models.FloatField(blank=True,null=True)
    other_charges = models.FloatField(blank=True,null=True)
    total_fare = models.FloatField(blank=True, null=True)
    seat_class = models.CharField(max_length=20, choices=SEAT_CLASS)
    booking_date = models.DateTimeField(default=datetime.now)
    phone = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=45, blank=True)
    status = models.CharField(max_length=45, choices=TICKET_STATUS)

    class Meta:
        db_table = "schedule"

    def __str__(self):
        return self.ref_no



