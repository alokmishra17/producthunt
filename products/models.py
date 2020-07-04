from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#product class
class Product(models.Model):
	title=models.CharField(max_length=200)
	pub_date=models.DateTimeField()
	body=models.TextField()
	url=models.TextField()
	image=models.ImageField(upload_to='images/')
	icon=models.ImageField(upload_to='images/')
	votes_total=models.IntegerField(default=1)
	#hunter
	hunter=models.ForeignKey(User,on_delete=models.CASCADE)

	def pub_date_formatted(self):
		return self.pub_date.strftime('%b %e %Y')

	def summary(self):
		return self.body[:200]
	
	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:200]


