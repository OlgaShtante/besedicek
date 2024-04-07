from django import template
import os

register = template.Library()

@register.simple_tag
def get_env(key):
    return os.environ.get(key, '')