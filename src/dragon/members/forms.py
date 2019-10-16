from django import forms
from .models import ClubMember, NonMember

class ClubMemberForm(forms.ModelForm):
    class Meta:
        model = ClubMember
        fields = [
            'FirstName',
            'surname',
            'email',
            'phoneNumber',
            'password',
            'preferredName',
            'preferredPronoun',
            'guildMember',
            'isStudent',
            'universityID',
            'joinDate',
            'incidents',
        ]
        labels= {
            'FirstName': 'First Name',
            'surname': 'Surname',
            'email': 'Email address',
            'phoneNumber': 'Phone Number',
            'password':'Password',
            'preferredName': 'Preferred Name',
            'preferredPronoun': 'Preferred Pronoun',
            'guildMember': 'Guild Membership',
            'isStudent': 'Current Student',
            'universityID': 'University/Student ID',
            'joinDate': 'Join Date',
            'incidents': 'Previous Incidents',
        }


class NonMemberForm(forms.ModelForm):
    class Meta:
        model = NonMember
        fields = [
            'FirstName',
            'surname',
            'email',
            'phoneNumber',
            'organization',
            'incidents',
            'addedDate'
        ]
        labels = {
            'FirstName': 'First name',
            'surname': 'Surname',
            'email': 'Email address',
            'phoneNumber': 'Phone Number',
            'organization': 'Organization Name',
            'incidents': 'Previous Incidents',
            'addedDate': 'Date added:'
        }
