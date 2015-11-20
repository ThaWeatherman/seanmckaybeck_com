#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sean Beck'
SITENAME = 'Show Me the Code'
SITEURL = 'https://seanmckaybeck.com'

PATH = 'content'
THEME = './themes/flasky'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

SECTIONS = [('Blog', 'index.html'),
            ('Archive', 'archives.html'),
            ('Tags', 'tags.html'),
            ('About', 'about.html')]

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
'en': '%Y %d %m'
}
DEFAULT_DATE_FORMAT = '%d %m %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# OUTPUT_PATH = '/your/output/directory'
# static paths will be copied under the same name
STATIC_PATHS = ["images"]

# Optional social media links
# =============================
# DISQUS_SITENAME = "your_disqus_user"
TWITTER_USERNAME = 'seanmckaybeck'
LINKEDIN_URL = 'https://www.linkedin.com/in/seanmckaybeck'
GITHUB_URL = 'https://github.com/ThaWeatherman'
# FACEBOOK_URL = 'http://www.facebook.com/you'
# GOOGLEPLUS_URL = 'https://plus.google.com/your_profile_id/posts'
# PINTEREST_URL = 'http://pinterest.com/you'
MAIL_USERNAME = 'seanmckaybeck'
MAIL_HOST = 'gmail.com'

# Optional analytic trackers
# =============================
# GOOGLE_ANALYTICS_ACCOUNT = 'UA-00000000-1'
# PIWIK_URL = 'myurl.com/piwik'
# PIWIK_SSL_URL = 'myurl.com/piwik'
# PIWIK_SITE_ID = '1'

# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
