from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Return an item from a dictionary by key."""
    return dictionary.get(key)


@register.filter
def mul(value, arg):
    return value * arg
