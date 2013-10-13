from django.conf import settings
from django.db import models
from django.contrib import admin

class Technology(models.Model):
	name = models.CharField(max_length=100)
	PHP = 'php'
	CSS = 'css'
	LANGUAGES = (
		(PHP, 'PHP'),
		(CSS, 'CSS'),
	)
	language = models.CharField(max_length=10, choices=LANGUAGES)
	CMS = 'cms'
	FRAMEWORK = 'frame'
	LANGUAGE = 'lang'
	TYPE = (
		(CMS, 'CMS'),
		(FRAMEWORK, 'Framework'),
		(LANGUAGE, 'Language'),
	)
	classType = models.CharField(max_length=10, choices=TYPE)
	def __unicode__(self):
		return self.name


ITEM_TYPES = (
	('P', 'Plugin'),
	('L', 'Library'),
)
class TechItem(models.Model):
	name = models.CharField(max_length=100)
	projectUrl = models.URLField()
	technology = models.ForeignKey('Technology')
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
	userID = models.ForeignKey(settings.AUTH_USER_MODEL)
	techItem = models.ForeignKey('TechItem')
	grade = models.IntegerField()
	radar = models.CharField(max_length=1, choices=RADAR_OPTIONS)
	notes = models.TextField(max_length=500)
	project = models.CharField(max_length=100)
	def __unicode__(self):
		return "Review of " + self.techItem.name + " by " + self.userID.username

#################
# Admin Classes #
#################
class TechItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'technology', 'itemType', 'subscriptionRequired')

admin.site.register(Technology)
admin.site.register(ItemReview)
admin.site.register(TechItem, TechItemAdmin)
