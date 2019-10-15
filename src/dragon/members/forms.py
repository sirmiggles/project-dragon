from django import forms
from .models import ClubMember, NonMember

class ClubMemberForm(forms.ModelForm):
    class Meta:
        model = ClubMember
        fields = [
            'firstName',
            'surname',
            'email',
            'phoneNumber',
            'preferredName',
            'preferredPronoun',
            'guildMember',
            'isStudent',
            'universityID',
            'joinDate',
            'incidents',
            'clubRank',
        ]
        labels= {
            'firstName': 'First Name',
            'surname': 'Surname',
            'email': 'Email address',
            'phoneNumber': 'Phone Number',
            'preferredName': 'Preferred Name',
            'preferredPronoun': 'Preferred Pronoun',
            'guildMember': 'Guild Membership',
            'isStudent': 'Current Student',
            'universityID': 'University/Student ID',
            'joinDate': 'Join Date',
            'incidents': 'Previous Incidents',
            'clubRank' : 'Rank',
        }


class NonMemberForm(forms.ModelForm):
    class Meta:
        model = NonMember
        fields = [
            'firstName',
            'surname',
            'email',
            'phoneNumber',
            'organization',
            'incidents',
            'addedDate'
        ]
        labels = {
            'firstName': 'First name',
            'surname': 'Surname',
            'email': 'Email address',
            'phoneNumber': 'Phone Number',
            'organization': 'Organization Name',
            'incidents': 'Previous Incidents',
            'addedDate': 'Date added:'
        }
