from django.db import models

# Create your models here.
class VendorListing(models.Model):
    dateServing = models.DateField(null=True)
    Name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    Address = models.CharField(max_length=60)
    zipCode = models.IntegerField()
    beginning = models.CharField(max_length=60)
    ending = models.CharField(max_length=60)
    city = models.CharField(max_length=69)
    userlocation = models.CharField(max_length=120)

    def __str__(self):
        return self.Name

class Lala(models.Model):
    COLOR_CHOICES = (
        ('Green', 'Green'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
    )
    PRIORITY_CHOICES = (
        (0, '1'),
        (1, '2'),
        (2, '3'),
        (3, '4'),
     )
    TIME_CHOICES = (
        ('12:00 am', '12:00 am'),
        ('12:30 am', '12:30 am'),
        ('01:00 am', '01:00 am'),
        ('01:30 am', '01:30 am'),
        ('02:00 am', '02:00 am'),
        ('02:30 am', '02:30 am'),
        ('03:00 am', '03:00 am'),
        ('03:30 am', '03:30 am'),
        ('04:00 am', '04:00 am'),
        ('04:30 am', '04:30 am'),
        ('05:00 am', '05:00 am'),
        ('05:30 am', '05:30 am'),
        ('06:00 am', '06:00 am'),
        ('06:30 am', '06:30 am'),
        ('07:00 am', '07:00 am'),
        ('07:30 am', '07:30 am'),
        ('08:00 am', '08:00 am'),
        ('08:30 am', '08:30 am'),
        ('09:00 am', '09:00 am'),
        ('09:30 am', '09:30 am'),
        ('10:00 am', '10:00 am'),
        ('10:30 am', '10:30 am'),
        ('11:00 am', '11:00 am'),
        ('11:30 am', '11:30 am'),
        ('12:00 pm', '12:00 pm'),
        ('12:30 pm', '12:30 pm'),
        ('01:00 pm', '01:00 pm'),
        ('01:30 pm', '01:30 pm'),
        ('02:00 pm', '02:00 pm'),
        ('02:30 pm', '02:30 pm'),
        ('03:00 pm', '03:00 pm'),
        ('03:30 pm', '03:30 pm'),
        ('04:00 pm', '04:00 pm'),
        ('04:30 pm', '04:30 pm'),
        ('05:00 pm', '05:00 pm'),
        ('05:30 pm', '05:30 pm'),
        ('06:00 pm', '06:00 pm'),
        ('06:30 pm', '06:30 pm'),
        ('07:00 pm', '07:00 pm'),
        ('07:30 pm', '07:30 pm'),
        ('08:00 pm', '08:00 pm'),
        ('08:30 pm', '08:30 pm'),
        ('09:00 pm', '09:00 pm'),
        ('09:30 pm', '09:30 pm'),
        ('10:00 pm', '10:00 pm'),
        ('10:30 pm', '10:30 pm'),
        ('11:00 pm', '11:00 pm'),
        ('11:30 pm', '11:30 pm')
     )
    name = models.CharField(max_length=20)
    date = models.DateField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    color = models.CharField(max_length=6, choices=COLOR_CHOICES)
    beginning = models.CharField(max_length=9, choices=TIME_CHOICES)
    ending = models.CharField(max_length=9, choices=TIME_CHOICES)

    def __str__(self):
        return self.name
