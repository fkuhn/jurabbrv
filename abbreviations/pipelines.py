# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class JurabbrvPipeline(object):

    def __init__(self):

        self.abbrvfile = codecs.open('/tmp/legal_abbrv.jl', encoding='utf-8', mode='wb')

    def process_item(self, item, spider):

        line = json.dumps(dict(item)) + "\n"

        self.abbrvfile.write(line)

        return item


