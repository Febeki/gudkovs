from django import template

register = template.Library()

@register.filter
def get_field_value(obj, field_name):
    field = obj._meta.get_field(field_name)
    if field.is_relation:
        return '-'
    return getattr(obj, field_name)

@register.filter
def getattribute(obj, attr):
    return getattr(obj, attr)