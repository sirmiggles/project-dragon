from django.contrib import admin
from .models import NonMember,ClubMember

admin.site.register(ClubMember)
admin.site.register(NonMember)
