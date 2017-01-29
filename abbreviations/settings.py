# -*- coding: utf-8 -*-

# Scrapy settings for abbreviations project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'abbreviations'

SPIDER_MODULES = ['abbreviations.spiders']
NEWSPIDER_MODULE = 'abbreviations.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'abbreviations (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'random_useragent.RandomUserAgentMiddleware': 400
}
USER_AGENT_LIST = "/home/kuhn/Data/GitHub/jurabbrv/user_agents.txt"

AUTOTHROTTLE_ENABLED = True

ITEM_PIPELINES = {

    'abbreviations.pipelines.JurabbrvPipeline': 500


}

