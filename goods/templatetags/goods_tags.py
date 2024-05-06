from django import template
from goods.models import Categories, Subcategories

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag()
def tag_subcategories():
    return Subcategories.objects.all()
