# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chats(models.Model):
    id1 = models.ForeignKey('Users', models.DO_NOTHING, db_column='id1', related_name='+')
    id2 = models.ForeignKey('Users', models.DO_NOTHING, db_column='id2', related_name='+')
    locaton = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'chats'


class Shared(models.Model):
    owner = models.ForeignKey('Users', models.DO_NOTHING, related_name='+')
    shared = models.ForeignKey('Users', models.DO_NOTHING, related_name='+')
    field = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'shared'


class Users(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    seed = models.CharField(max_length=100)
    token = models.CharField(max_length=128)
    email = models.CharField(max_length=100)
    social = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.CharField(max_length=100, blank=True, null=True)
    hobby = models.CharField(max_length=100, blank=True, null=True)
    career = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    cigaretes = models.CharField(max_length=100, blank=True, null=True)
    alcohol = models.CharField(max_length=100, blank=True, null=True)
    music = models.CharField(max_length=100, blank=True, null=True)
    films = models.CharField(max_length=100, blank=True, null=True)
    videogames = models.CharField(max_length=100, blank=True, null=True)
    serials = models.CharField(max_length=100, blank=True, null=True)
    books = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
