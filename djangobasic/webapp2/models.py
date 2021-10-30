from django.db import models

# Create your models here.
class Customer(models.Model):
    user_id = models.CharField(max_length=10,primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=150)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    class Meta:
        db_table = "customer"
        managed = False
    def __str__(self):
        return self.user_id

class Flight(models.Model):
    fid = models.CharField(max_length=10,primary_key=True)
    flightnumber = models.CharField(max_length=50)
    amount = models.IntegerField()
    accept = models.BooleanField()
    username = models.CharField(max_length=100)
    dob = models.DateField()
    depart_time = models.TimeField(null=True, blank=True)
    depart_date = models.DateField(null=True, blank=True)
    return_time = models.TimeField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=150)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    pnr = models.CharField(max_length=256)
    class Meta:
        db_table = "flight"
        managed = True
    def __str__(self):
        return "%s %s %d %s" %(self.fid,self.flightnumber,self.amount,self.username)


