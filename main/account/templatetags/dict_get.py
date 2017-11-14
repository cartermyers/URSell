# This is a file to create simple functions used in template tags
# (i.e. {% code here %} in html templates)

# Right now, it's only used for easy dictionary access

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
