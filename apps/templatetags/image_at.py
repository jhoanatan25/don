from django import template

register = template.Library()

@register.filter
def image_at(value, arg):
    return value[arg].image.url if value[arg] is not None else ''
