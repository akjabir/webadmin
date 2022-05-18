import os
import datetime
from django.utils import timezone
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField

class Category(models.Model):
	cat_name            = models.CharField(max_length = 200)
	ordering 		    = models.IntegerField(default = 0)
	meta_description    = models.TextField(blank = True)
	meta_keywords       = models.TextField(blank = True)
	meta_title          = models.TextField(blank = True)
	status     		    = models.BooleanField(default=True)

	def __str__(self):
		return self.cat_name

	class Meta:
		verbose_name ='catagory'
		verbose_name_plural ='catagories'  
  
class Service(models.Model):
	catagory 		   = models.ForeignKey(Category , on_delete = models.CASCADE)
	title              = models.CharField(max_length = 200)
	title_url          = models.CharField(max_length = 200, unique= True, blank= True, null = True)
	images             = models.FileField(upload_to="service_images/")
	image_alt_tag      = models.CharField(max_length = 200, blank = True)
	details            = RichTextField(blank = True)
	meta_description   = models.TextField(blank = True)
	meta_keywords      = models.TextField(blank = True)
	meta_title         = models.TextField(blank = True)
	ordering 		   = models.IntegerField(default = 0)
	views   		   = models.IntegerField(default = 1)
	status     		   = models.BooleanField(default=True)
	
	def url(self):
		return os.path.join('/static/history/media/service_images/', os.path.basename(str(self.images)))

	def photo(self):
		return mark_safe('<img src = "{}" width="50"/>'.format(self.url()))

	def was_published_recently(self): 
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name ='Service'
		verbose_name_plural ='Services'

	
  
class SeoContent(models.Model):
	index_meta_title          = models.TextField(blank = True)
	index_meta_description    = models.TextField(blank = True)
	index_meta_keywords       = models.TextField(blank = True)
	status                    = models.BooleanField(default=True)

	def __str__(self):
		return self.index_meta_title   

	class Meta:
		verbose_name = 'Seo Content'
		verbose_name_plural = 'Seo Contentes'
		
class Privacy(models.Model):
	pri_details				  = RichTextField(blank = True)
	meta_description   		  = models.TextField(blank = True)
	meta_keywords      		  = models.TextField(blank = True)
	meta_title			      = models.TextField(blank = True)

	def __str__(self):
		return self.pri_details

	class Meta:
		verbose_name = 'Privacy'
		verbose_name_plural = 'Privacy'

class Aboutus(models.Model):
	about_details			  = RichTextField(blank = True)
	meta_description   		  = models.TextField(blank = True)
	meta_keywords      		  = models.TextField(blank = True)
	meta_title			      = models.TextField(blank = True)

	def __str__(self):
		return self.about_details

	class Meta:
		verbose_name = 'Aboutus'
		verbose_name_plural = 'Aboutus'

class Term(models.Model):
	term_details			  = RichTextField(blank = True)
	meta_description   		  = models.TextField(blank = True)
	meta_keywords      		  = models.TextField(blank = True)
	meta_title			      = models.TextField(blank = True)

	def __str__(self):
		return self.term_details

	class Meta:
		verbose_name = 'Term'
		verbose_name_plural = 'Term'

class Contact(models.Model):
	contact_details 		  = RichTextField(blank = True)
	meta_description   		  = models.TextField(blank = True)
	meta_keywords      		  = models.TextField(blank = True)
	meta_title			      = models.TextField(blank = True)

	def __str__(self):
		return self.contact_details
	
	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contact'