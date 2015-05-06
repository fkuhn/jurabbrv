# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class JurabbrvPipeline(object):
    def process_item(self, item, spider):

        with codecs.open('/tmp/legal_abbrv.txt', encoding='utf-8', mode='a+') as abbrvfile:

            abbrvfile.write(item['abbrev'] + '\n')

        
        return item


