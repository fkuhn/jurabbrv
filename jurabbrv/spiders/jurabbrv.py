

from items import JurabbrvItem
from string import ascii_lowercase

class OpenJurSpider(CrawlSpider):
    name = "jurabbrv"
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
        #    <td width="150" valign="top"><a name="AöR">AöR</a></td>
        #    <td width="350">Archiv des öffentlichen Rechts (Zeitschrift)</td>
        # </tr>


        for table in tree.iter('TABLE'):

            item = JurabbrvItem()

                for entryelem in table.iter('tr'):

                    if entryelem.attrib['width'] == '150':
                        item['abbrev'] = entryelem.text
                    elif entryelem.attrib('width') == '300':
                        item['paraphrase'] = entryelem.text
                if entryelem['abbrev']:
                    abbreviations.append(item)

        return abbreviations
