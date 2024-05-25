# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        managed = False
        db_table = 'auth_user'

class Customerinfo(models.Model):
    name = models.CharField(max_length=45)
    phonenumber = models.FloatField(db_column='phoneNumber')  # Field name made lowercase.
    address = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customerInfo'
        unique_together = (('id', 'phonenumber'),)
