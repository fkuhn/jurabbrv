
import scrapy
from scrapy.contrib.spiders import CrawlSpider
from abbreviations.items import JurabbrvItem
from string import ascii_lowercase
from lxml import etree


class OpenJurSpider(scrapy.Spider):
    name = "abbreviations"
    allowed_domains = ['juristische-abkuerzungen.de']
    # start_urls = [
    #    'https://openjur.de/u-%d.html' % decimal
    # ]
    max_pages = 30

    def start_requests(self):
        """
        iterate over all pages that link to documents
        :return:
        """

        for letter in ascii_lowercase:
            yield scrapy.Request('http://www.juristische-abkuerzungen.de/juristische_abkuerzungen_%s.html' % letter, callback=self.parse)

    def parse(self, response):

        # define a html parser
        html_parser = etree.HTMLParser()
        tree = etree.fromstring(response.body, parser=html_parser)

        abbreviations = list()

        # <tr>
        #    <td width="150" valign="top"><a name="AoeR">AoeR</a></td>
        #    <td width="350">Archiv des oeffentlichen Rechts (Zeitschrift)</td>
        # </tr>

        for entry in tree.xpath('//a/@name'):

            yield JurabbrvItem(abbrev=unicode(entry))
