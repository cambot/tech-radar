from django.db import models
from django.contrib import admin

ITEM_TYPES = (
	('P', 'Plugin'),
	('L', 'Library'),
)
class TechItem(models.Model):
	name = models.CharField(max_length=100)
	projectUrl = models.URLField()
	parent = models.CharField(max_length=100)  # alt names: category, type, ...
	subscriptionRequired = models.BooleanField()
	itemType = models.CharField(max_length=1, choices=ITEM_TYPES)	
	def __unicode__(self):
		return self.name


RADAR_OPTIONS = (
	('A', 'Adopt'),
	('H', 'Hold'),
	('T', 'Trial'),
	('R', 'Reject'),
)
class ItemReview(models.Model):
	person = models.CharField(max_length=100)
	techItem = models.ForeignKey('TechItem')
	grade = models.IntegerField()
	radar = models.CharField(max_length=1, choices=RADAR_OPTIONS)
	notes = models.TextField(max_length=500)
	project = models.CharField(max_length=100)
	def __unicode__(self):
		return "Review of " + self.techItem.name + " by " + self.person

#################
# Admin Classes #
#################

admin.site.register(ItemReview)
admin.site.register(TechItem)
