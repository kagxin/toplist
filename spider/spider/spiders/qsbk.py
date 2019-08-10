# -*- coding: utf-8 -*-
import scrapy
from apps.schedule.models import Entry
from django.db.utils import OperationalError
from django.utils.timezone import now


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/']
    rank = 1

    def parse(self, response):
        for res in response.xpath('//div[@class="recommend-article"]/ul/li'):
            title = res.xpath('div/a[@class="recmd-content"]/text()').get('')
            url = res.xpath('div/a[@class="recmd-content"]/@href').get('')
            try:
                Entry.objects.update_or_create(
                    target=1,
                    rank=self.rank,
                    defaults={'title': title, 'url': response.urljoin(url), 'release_date': now()},
                )
            except OperationalError as e:
                pass

            self.rank = self.rank + 1
            print(self.rank)
        next_page_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        if next_page_url:
            yield response.follow(next_page_url, self.parse)
