from django import template

register = template.Library()


# METOD 2 USING DECORATORS
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')

# METOD 1 -- 'cut' = string name and cut= function
# register.filter('cut', cut)