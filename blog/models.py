# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


class Category(models.Model):
   
    name = models.CharField(u"Kategori",max_length = 255)
    slug = models.SlugField(u"Slug")
    
    def __unicode__(self):
	return u'%s'%self.name
    
    class Meta:
	verbose_name = u"Kategori"
	verbose_name_plural = u"Kategoriler"


class Post(models.Model):

    title = models.CharField(u"Başlık", max_length = 255)
    slug = models.SlugField(u"Slug")
    keywords = models.CharField(u"Keywords", max_length = 255)
    date = models.DateField(u"Tarih")
    description = models.TextField(u"Kısa Açıklama")
    image = models.ImageField(u"Resim", upload_to="blog")
    text = RichTextField(u"Yazı")
    categories = models.ManyToManyField(Category, blank=True, null=True)

    def __unicode__(self):
	return u'%s'%self.title

    class Meta:
	verbose_name = u"Yazı"
	verbose_name_plural = u"Yazılar"

class Contact(models.Model):
    name = models.CharField(u"Başlık", max_length=255)
    mail = models.EmailField(u"E-Mail")
    date = models.DateTimeField(u"Tarih", default=datetime.now())
    message = models.TextField(u"Konu")