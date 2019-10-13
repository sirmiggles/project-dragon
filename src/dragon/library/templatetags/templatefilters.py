from django import template

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
