#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

AUTHOR = 'Mounir Messelmeni'
SITENAME = 'Awesome notes'
SITEURL = 'http://mounirmesselmeni.github.io'
SITESUBTITLE = 'We must learn to live together as brothers or perish together as fools. “Martin Luther King, Jr“'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "pelican-octopress-theme"
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

GITHUB_URL = 'http://github.com/MounirMesselmeni/'
DISQUS_SITENAME = "mounir-blog"
GOOGLE_ANALYTICS = "UA-42132208-1"


SOCIAL = (
    ('Linkedin', 'https://de.linkedin.com/in/mounirmesselmeni'),
    ('Github', 'http://github.com/MounirMesselmeni'),)

PLUGIN_PATHS = [os.path.join(BASE_DIR, 'pelican-plugins')]
PLUGINS = ["assets", "liquid_tags", "sitemap", "pelican_gist"]

TYPOGRIFY = True
