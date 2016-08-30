from django import template
register = template.Library()
from ..models import Post
from django.contrib.auth.models import User


@register.simple_tag()
def total_post():
	return Post.objects.all().count()

@register.simple_tag()
def user_number():
	return User.objects.all().count()


#puedes acceder al tag desde un template con {% chispo %}
# @register.simple_tag(name='chispo')
# def total_post():
# 	return Post.objects.all().count()



## tag que recibe una variable y renderiza un pequeno template html
@register.inclusion_tag('posts/ultimos.html')
def show_last(count=5):
	ultimos= Post.objects.all().order_by('-fecha')[:count]
	return {
	'ultimos':ultimos
	}





# assignment _tag devuelve una variable de la cual podemos dispo
from django.db.models import Count

@register.assignment_tag
def most_commented(count=5):
	return Post.objects.all().annotate(
		##usar el related_name comentarios
		total_comments = Count('comentarios')
		).order_by('-total_comments')[:count]
