import logging
from settings import celery_app
from spider.spider.spiders.qsbk import QsbkSpider
from scrapy.crawler import CrawlerProcess

log = logging.getLogger('scripts')

@celery_app.task()
def add(a, b):
    c = a + b
    print('{}'.format(c))
    log.info('{}'.format(c))
    print('adsfasfdshello.')
    return c


@celery_app.task()
def fetch():
    process = CrawlerProcess(settings=dict(
        USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    ))
    process.crawl(QsbkSpider)
    process.start(stop_after_crawl=False)  # the script will block here until the crawling is finished
