from django.db import models

#class defines what input is captured into database
class Join(models.Model):
	email = models.EmailField()

	#foreignkey, also gives blank referall if they weren't referred
	friend = models.ForeignKey("self", related_name = 'referral', null=True, blank=True)
	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
		return "%s" %(self.email)

	#this class makes sure the reference ID is unique
	class Meta:
		unique_together = ("email", "ref_id",)
