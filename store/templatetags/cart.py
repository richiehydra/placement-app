from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(company  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == company.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(company, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == company.id:
            return cart.get(id)
    return 0;