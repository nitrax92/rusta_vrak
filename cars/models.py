# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator

from django.db import models

# Need to support python 2
# Old Car Table.
@python_2_unicode_compatible
class Car(models.Model):
    car_type = models.PositiveSmallIntegerField('Kategori', choices=[(1, 'Personbil'), (2, 'Varebil'), (3, 'Kombibil')])
    #Misc information
    brand = models.CharField('Bilmerke', max_length=70)
    model = models.CharField('Biltype', max_length=70)
    year = models.PositiveSmallIntegerField(blank=True, null=True)

    seats = models.PositiveSmallIntegerField('Antall seter')
    fuel_type = models.CharField('Type drivstoff', choices=[('Diesel', 'Diesel'), ('Bensin', 'Bensin'), ('Hybrid', 'Hybrid'), ('Elbil', 'Elbil')], max_length=20)

    main_image = models.CharField('Lenke til hovedbilde', max_length=50, default='')
    gallery_images = models.CharField('Bilder til galleri. Splitt lenkene via komma ","', max_length=255, blank=True, null=True)

    transmission = models.CharField('Gir', choices=[('Manuell', 'Manuell'), ('Automatgir', 'Automatgir')], default='Manuell', max_length=15)
    extra_accessories = models.CharField('Ekstra informasjon, splitt med komma (",")', blank=True, null=True, max_length=255)

    price = models.IntegerField('Dagspris leie', default=250)

    for_rent = models.BooleanField('Bilen klar for utleie.', default=True)

    license_plate = models.CharField('Skiltnummer', blank=True, null=True, max_length=10, unique=True)


    def __str__(self):
        if self.license_plate:
            return str(self.id) + self.license_plate + " | " + self.brand + " | " + self.model
        else:
            return str(self.id) + str(self.car_type) + " | " + self.brand + " | " + self.model

    class Meta:
        verbose_name = 'Bil'
        verbose_name_plural = 'Biler'






"""
@python_2_unicode_compatible
class Car_Rental(models.Model):
    reg_number = models.CharField('Skiltnummer',primary_key=True, max_length=10, unique=True)
    car_type = models.PositiveSmallIntegerField('Kategori', choices=[(1, 'Personbil'), (2, 'Varebil'), (3, 'Kombibil')])

"""