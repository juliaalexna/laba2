from django.db import models


# Create your models here.
class Student (models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	group_number = models.IntegerField()
	def __str__(self):
		return self.name
	

class Subject (models.Model):
	sub_name = models.CharField(max_length=30)
	sub_hours = models.IntegerField()
	def __str__(self):
		return self.sub_name


class Score (models.Model):
	# unique_together = (Student, Subject)
	stud_id = models.ForeignKey(Student) 
	subj_id = models.ForeignKey(Subject) 
	score = models.IntegerField()


#Student.objects.create(name = 'K', email = 're@mail.ru', group_number = 724)
#Student.objects.create(name = 'L', email = 'LOL@mail.ru', group_number = 724)
#Subject.objects.create(sub_name = 'fizika', sub_hours = 42)
#Subject.objects.create(sub_name = 'fil', sub_hours = 42)
#Score.objects.create(score = 5)



        