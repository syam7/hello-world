from django.db import models

# Create your models her

class Question (models.Model):
	question_text = models.TextField()
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text 


class Answer (models.Model):
	question = models.ForeignKey(Question,on_delete =models.CASCADE)
	answer_text = models.TextField()
	def __str__(self):
		return self.answer_text 
	 	

