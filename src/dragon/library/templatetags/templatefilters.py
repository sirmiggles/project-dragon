from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter
def trimlist(value, arg):
    result = ""
    for word in value:
        if len(result) == 0:
            result = word.name
        elif len(result) + len(word.name) < arg:
            result = result + ', ' + word.name
    return result

@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group =  Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False

    return group in user.groups.all()

