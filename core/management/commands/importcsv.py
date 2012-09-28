from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
import re
from core.models import Devotional
import csv 
from StringIO import StringIO 


class Command(BaseCommand):
    args = '<filename ...>'
    help = 'Imports the csv data'

    def handle(self, *args, **options):
        filename = 'programming-sample.tab'
        for name in args:
            filename = name
        
        with open(filename, "r") as f:
            PATTERN = re.compile(r'(.*?),(.*?),(.*?),(.*)')
            for line in f:
                try:
                    m = PATTERN.match(line)
                    title,month,day,body = m.group(1), m.group(2), m.group(3), m.group(4)
                    devotional = Devotional(title=title,month=month,day=day,body=body)
                    devotional.save()
                except Exception as e:
                    print e
        
        self.stdout.write('Import completed from: '+ filename + '\n')