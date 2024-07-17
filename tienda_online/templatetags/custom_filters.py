from django import template

register = template.Library()


@register.filter(name='custom_format')
def custom_format(value):
    try:
        value = float(value)
        formatted_value = "{:,.2f}".format(value)
    except (ValueError, TypeError):
        return value

    return formatted_value
