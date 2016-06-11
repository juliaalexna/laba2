from django import forms
 
class SubForm(forms.Form):
    subject = forms.CharField(label='Название предмета', max_length=256)
    hours = forms.IntegerField(label='Кол-во часов')
    sid = forms.IntegerField(widget=forms.HiddenInput(), required=False)