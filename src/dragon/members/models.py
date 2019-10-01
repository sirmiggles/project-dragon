from django.db.models import Model, CharField, AutoField, BooleanField, IntegerField, EmailField, DateField, TextField
import django.utils
from datetime import datetime


class User(Model):
    id = AutoField(primary_key=True, default=0)
    firstName = CharField(max_length=50, default='')
    surname = CharField(max_length=50, default='')
    email = EmailField(default='')
    phoneNumber = CharField(max_length=20, default='')

    def __str__(self):
        return self.id


class ClubMember(User):

    preferredName = CharField(max_length=50, default='')
    preferredPronoun = CharField(max_length=20, default='')
    guildMember = BooleanField(default=True)
    isStudent = BooleanField(default=True)
    universityID = CharField(max_length=8, default='')
    joinDate = DateField(default=django.utils.timezone.now)
    incidents = TextField(max_length=400, default='N/A')

    rank_choices = ((0, 'Regular Member'), (1, 'Gatekeeper'), (2, 'Committee Member'))
    clubRank = IntegerField(choices=rank_choices, default=0)

    def __str__(self):
        return self.id

