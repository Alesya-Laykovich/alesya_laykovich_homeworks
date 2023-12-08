from django import template
from django.db.models import Count

from taskmanager.models import Category, Completed, Priority, Favourite

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()
def get_completed():
    return Completed.objects.all()

@register.simple_tag()
def get_priorities():
    return Priority.objects.all()

@register.simple_tag()
def get_favourite():
    return Favourite.objects.all()

# @register.inclusion_tag('taskmanager/list_categories.html')
# def show_categories():
#     categories = Category.objects.annotate(cnt=Count('taskmanager')).filter(cnt__gt=0)
#     return {'categories': categories}