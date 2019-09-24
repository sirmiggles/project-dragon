from django.db.models import Model, CharField, AutoField, BooleanField, IntegerField, EmailField, DateField, TextField
import django.utils
from datetime import datetime


class User(Model):
    Id = AutoField(primary_key=True, default=0)
    FirstName = CharField(max_length=50, default='')
    Surname = CharField(max_length=50, default='')
    Email = EmailField(default='')
    PhoneNumber = CharField(max_length=20, default='')

    def __str__(self):
        return self.Id


class ClubMember(User):

    PreferredName = CharField(max_length=50, default='')
    PreferredPronoun = CharField(max_length=20, default='')
    GuildMember = BooleanField(default=False)
    IsStudent = BooleanField(default=True)
    UniversityID = CharField(max_length=8, default='')
    JoinDate = DateField(default=django.utils.timezone.now)
    Incidents = TextField(max_length=400, default='N/A')

    rank_choices = ((0, 'Regular Member'), (1, 'Gatekeeper'), (2, 'Committee Member'))
    ClubRank = IntegerField(choices=rank_choices, default=0)

    def __str__(self):
        return self.Id

