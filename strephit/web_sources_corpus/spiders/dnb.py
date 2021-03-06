#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import urlparse

from strephit.web_sources_corpus.items import WebSourcesCorpusItem
from strephit.web_sources_corpus.spiders.BaseSpider import BaseSpider


class DictionaryOfNationalBiographySpider(BaseSpider):
    """ A spider for the Dictionary of National Biography, in Wikisource """
    name = 'dnb'
    allowed_domains = ['en.wikisource.org']
    start_urls = ['https://en.wikisource.org/wiki/Dictionary_of_National_Biography,_1885-1900']

    list_page_selectors = 'xpath:.//dd/a/@href'
    detail_page_selectors = 'xpath:.//table//li/a/@href'
    next_page_selectors = 'xpath:.//span[@id="headernext"]/a/@href'

    item_class = WebSourcesCorpusItem
    item_fields = {
        'bio': 'clean:xpath:.//div//p//text()'
    }

    def refine_item(self, response, item):
        url = response.url
        item['url'] = url
        # Wiki URLs naming convention
        item['name'] = ' '.join(urlparse.urlsplit(url).path.split('/')[-1].split('_')[:-1])
        return super(DictionaryOfNationalBiographySpider, self).refine_item(response, item)
