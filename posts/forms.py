from django import forms
from .models import Post, Comment 


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['titulo','cuerpo','imagen','tags']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['cuerpo']
		labels  = {
			'cuerpo':'Escribe un Comentario'
		}


