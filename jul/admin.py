from django.contrib import admin

# Register your models here.
from .models import Student,Subject,Score


class StudentAdmin(admin.ModelAdmin):
	list_display=('name','email', 'group_number')


class SubjectAdmin(admin.ModelAdmin):
	list_display=('sub_name','sub_hours')

class ScoreAdmin(admin.ModelAdmin):
	list_display=('stud_id','subj_id', 'score')
	#list_editable=('stud_id','subj_id', 'score')

admin.site.register(Student,StudentAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Score,ScoreAdmin)
