from django.db import models

# Create your models here.
class Machines(models.Model):
	version = models.CharField(max_length = 50, blank=False)

	def __unicode__(self):
		return self.version