from django import forms
 
class SubForm(forms.Form):
    subject = forms.CharField(label='Название предмета', max_length=256, required=True)
    hours = forms.IntegerField(label='Кол-во часов', min_value=0)
    sid = forms.IntegerField(widget=forms.HiddenInput(), required=False)

class StudentForm(forms.Form):
	name = forms.CharField(label ='Имя студента', max_length=256, required=True)
	email = forms.EmailField(label='E-mail', required=True)
	group_number = forms.IntegerField(label='Номер группы',min_value=0)
	stid = forms.IntegerField(widget=forms.HiddenInput(), required=False)

class AddScoreForm(forms.Form):
	stud_id = forms.CharField(label='Имя студента', widget=forms.TextInput(attrs={'readonly':'readonly'})) 
	subj_id = forms.CharField(label='Название предмета', widget=forms.TextInput(attrs={'readonly':'readonly'})) 
	score = forms.IntegerField(min_value=0,required=True)
	sid =forms.IntegerField(widget=forms.HiddenInput(),required=False)
	stid =forms.IntegerField(widget=forms.HiddenInput(),required=False)




		