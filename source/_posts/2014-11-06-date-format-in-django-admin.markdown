---
layout: post
title: "Date Format in Django Admin"
date: 2014-11-06 14:04
comments: true
categories: [Django, Python, Django Admin]
keywords: python, django, django admin, date format, settings, date, datetime, internalization, i18n, i10n, list_display, local, django.conf.locale
description: Django Admin list_display custom date time format and default locale settings overriding
---


Recently I was working on a Django project where I wanted a different date time format other than the default one when English language is active in the Admin `list_display`.

Many posts on [Stackoverflow][1] I found, suggest to add a custom method in the `ModelAdmin` class like this:

{% codeblock lang:python %}

def time_seconds(self, obj):
    return obj.timefield.strftime("%d %b %Y %H:%M:%S")

time_seconds.short_description = 'Precise Time'    

list_display = ('id', 'time_seconds', )

{% endcodeblock %}

The problem with this code, that I must update all my ModelAdmin with DateTime fields like this and without date time internalization.

The more comfortable solution for which avoid this repetition is by overriding the default language format (For this case, French format was correct, I need only to change the formatting for English for the DateTime fields).

You need just to override Django's defaults locale settings. Add this to your `settings.py` file

{% codeblock lang:python settings.py %}

from django.conf.locale.en import formats as en_formats
en_formats.DATETIME_FORMAT = "d b Y H:i:s"

{% endcodeblock %}

You can override for example German's default `DATETIME_FORMAT` by importing `from django.conf.locale.de import formats as de_formats`.


[1]: http://stackoverflow.com/questions/7216764/in-the-django-admin-site-how-do-i-change-the-display-format-of-time-fields
