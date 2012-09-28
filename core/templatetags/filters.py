# Some custom filters for dictionary lookup.
from __future__ import unicode_literals
from django.template.defaultfilters import register
import re
from datetime import date, datetime

from django.conf import settings
from django.template import defaultfilters
from django.utils.formats import number_format
from django.utils.translation import pgettext, ungettext, ugettext as _

from htmlentitydefs import name2codepoint
import string
# for some reason, python 2.5.2 doesn't have this one (apostrophe)
name2codepoint['#39'] = 39

@register.filter(name='htmlunescape')
def htmlunescape(s):
    "unescape HTML code refs; c.f. http://wiki.python.org/moin/EscapingHtml"
    return re.sub('&(%s);' % '|'.join(name2codepoint),
              lambda m: unichr(name2codepoint[m.group(1)]), s)
    
@register.filter(name='removequotes')
def removequotes(s):
    return string.replace(s,'"','')