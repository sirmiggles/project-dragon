from django import forms
from .models import ClubMember


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
            'clubRank'
        ]
        labels= {
            'firstName': 'First name',
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
            'clubRank': 'Club Rank'
    }
