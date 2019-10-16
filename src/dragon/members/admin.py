from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#these will be added to the admin page
from .models import NonMember,ClubMember

admin.site.register(ClubMember)
admin.site.register(NonMember)

#limit non-superusers permission
class UserAdmin(BaseUserAdmin):
        list_display = ('username', 'email', 'is_staff')
        list_filter = ('is_staff',)
        #this displays after initial user creation for additional information
        fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        #('Personal info', {'fields': ('first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups')}),
        )
        # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
        # overrides get_fieldsets to use this attribute when creating a user.
        add_fieldsets = (
        (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2')}
        ),
        )
        search_fields = ('username',)
        ordering = ('username',)

    #unregister the default user admin
admin.site.unregister(User)
    # Now register the new UserAdmin...
admin.site.register(User, UserAdmin)


