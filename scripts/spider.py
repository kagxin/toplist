from spider.spider.spiders.qsbk import QsbkSpider
from scrapy.crawler import CrawlerProcess


def run():
    process = CrawlerProcess(settings=dict(
        USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    ))
    process.crawl(QsbkSpider)
    process.start()  # the script will block here until the crawling is finished
