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
            'FirstName': 'First Name',
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
            'FirstName',
            'surname',
            'email',
            'phoneNumber',
            'organization',
            'incidents',
            'addedDate'
        ]
        labels= {
            'FirstName': 'First name',
            'surname': 'Surname',
            'email': 'Email address',
            'phoneNumber': 'Phone Number',
            'organization': 'Organization Name',
            'incidents': 'Previous Incidents',
            'addedDate': 'Date added:'
        }
