# -*- coding: utf-8 -*-

from blog.models import Category, Post
from blog.forms import ContactForm
from django.shortcuts import render,get_object_or_404
from django.contrib import messages

def articles(request, template = 'index.html'):
	categories = Category.objects.all().order_by('name')
	posts = Post.objects.all().order_by('-date')

	ctx = {
		'posts' : posts,
		'category' : categories,
	}

	return render(request,template,ctx)

def loop(request, template = 'blog.html'):
	categories = Category.objects.all().order_by('name')
	posts = Post.objects.all().order_by('-date')

	ctx = {
		'posts' : posts,
		'category' : categories,
	}

	return render(request,template,ctx)	

def categories(request, template = 'category.html', slug=None):
	category = get_object_or_404(Category,slug=slug)
	categorylist = Category.objects.all().order_by('name')
	posts = category.post_set.all().order_by('-date')

	ctx = {
		'posts' : posts,
		'category' : category,
		'categorylist' : categorylist,
	}

	return render(request,template,ctx)	

def article(request, template = "detail.html", slug = None):
	categories = Category.objects.all().order_by('name')
	posts = Post.objects.all().order_by('-date')
	post = get_object_or_404(Post, slug=slug)

	ctx = {
		'posts' : posts,
		'category' : categories,
		'post' : post,
	}

	return render(request,template,ctx)

def contact(request, template="contact.html"):
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, u'Tamamdır')
			form=ContactForm()
	else:
		form=ContactForm()
	ctx = {
		'form' : form,
	}
	return render(request,template,ctx)

