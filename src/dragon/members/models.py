from django.db.models import Model, CharField, AutoField, BooleanField, IntegerField, EmailField, DateField, TextField
import django.utils
#from django.contrib.auth.models import PermissionsMixin,AbstractUser
from django.db import models
#from guardian.models import GroupObjectPermissionBase


class User(Model):
    id = AutoField(primary_key=True)
    FirstName = CharField(max_length=50)
    surname = CharField(max_length=50)
    email = EmailField(default='',unique=True)
    phoneNumber = CharField(max_length=20, default='',unique=True)

    def __str__(self):
        return self.FirstName
        #return self.id


class ClubMember(User):

    preferredName = CharField(max_length=50, default='')
    preferredPronoun = CharField(max_length=20, default='')
    guildMember = BooleanField(default=True)
    isStudent = BooleanField(default=True)
    universityID = CharField(max_length=8, default='',unique=True)
    joinDate = DateField(default=django.utils.timezone.now)
    incidents = TextField(max_length=400, default='N/A')
    
    rankChoices = [
        ('MEM', 'Member'), 
        ('GK', 'Gate Keeper'), 
        ('OCM', 'Ordinary Committee'), 
        ('EXEC', 'Club Executive')]
    clubRank = TextField(choices=rankChoices, default='MEM')


    def __str__(self):
        return self.FirstName
        #return self.id

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NonMember(User):

    organization = CharField(max_length=200)
    addedDate = DateField(default=django.utils.timezone.now)
    incidents = TextField(max_length=400, default='N/A')

    def __str__(self):
        return self.FirstName

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


