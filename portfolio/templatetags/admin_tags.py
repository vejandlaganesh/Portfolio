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

@register.filter
def split_csv(value):
    """'React, Node.js, Tailwind CSS' -> ['React', 'Node.js', 'Tailwind CSS'].

    Django's built-in `.split` in templates splits on whitespace, which broke
    multi-word technologies ("Tailwind CSS") and left trailing commas.
    """
    return [part.strip() for part in str(value or "").split(",") if part.strip()]
