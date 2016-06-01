from django.db import models

# Create your models here.

class feedback(models.Model):
	subject = models.CharField(max_length=1000)
	feedback_text = models.TextField()
	def __str__ (self):
		return self.subject
