from django import forms
from django.core.exceptions import ValidationError
from board.models import Posts


class PostForm(forms.Form):
    class Meta:
        model = Posts
        fields = [
            'authors',
            'post_title',
            'post_text',
            'name_category'
        ]

    def clean(self):
        cleaned_data = super().clean()
        post_title = cleaned_data.get('post_title')
        post_text = cleaned_data.get('post_text')
        if post_text is not None and post_text == post_title:
            raise ValidationError({
                'post_text': 'Текст статьи не должен быть идентичен заголовоку'
            })
        return cleaned_data


class RespondForm(forms.ModelForm):
    text = forms.CharField(label='Оставить отклик', widget=forms.Textarea)

    class Meta:
        fields = ['text']

















