from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr):
    if hasattr(obj, attr):
        val = getattr(obj, attr)
        if val is None:
            return ""
        return val
    return ""

@register.filter
def replace_underscore(value):
    return value.replace("_", " ")
