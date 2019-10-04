from django import forms
from .models import ClubMember, NonMember


class ClubMemberForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ClubMember
        fields = [
            'firstName',
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
            'clubRank'
        ]
        labels= {
            'firstName': 'First name',
            'surname': 'Surname',
            'password': 'Password',
            'email': 'Email address',
            'phoneNumber': 'Phone Number',
            'preferredName': 'Preferred Name',
            'preferredPronoun': 'Preferred Pronoun',
            'guildMember': 'Guild Membership',
            'isStudent': 'Current Student',
            'universityID': 'University/Student ID',
            'joinDate': 'Join Date',
            'incidents': 'Previous Incidents',
            'clubRank': 'Club Rank'
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

