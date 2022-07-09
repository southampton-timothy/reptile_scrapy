# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import logging

logger = logging.getLogger(__name__)

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class BossSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        logging.debug("#### 33333 response %s , spider %s ####" % (response, spider))
        return

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        logging.debug("#### 44444 response %s , result %s , spider %s ####" % (response, result, spider))
        return result

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        """
               第一次发送请求前调用,之后不再调用
               :param start_requests:
               :param spider:
               :return:
               """
        logging.debug("#### 2222222 start_requests %s , spider %s ####" % (start_requests, spider))
        last_request = []
        for one_request in start_requests:
            logging.debug("#### one_request %s , spider %s ####" % (one_request, spider))
            last_request.append(one_request)
        logging.debug("#### last_request %s ####" % last_request)

        return last_request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BossDownloaderMiddleware(object):
    """
    下载器中间件
    """
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        if spider.name == 'boss':
            if request.url == 'https://www.zhipin.com/c101210100/h_101210100/?page=1&ka=page-1':
                options = Options()
                options.add_argument('-headless')

                # geckodriver需要手动下载
                driver = Chrome(executable_path='/ddhome/bin/geckodriver', chrome_options=options)
                driver.get(request.url)

                searchText = driver.find_element_by_xpath('//div[@class="search-form-con"]//input[1]')
                searchText.send_keys(unicode("大数据研发工程师"))
                searchBtn = driver.find_element_by_xpath(
                    '//div[@class="search-form "]//button[@class="btn btn-search"]')
                searchBtn.click()

                html = driver.page_source
                driver.quit()

                # 构建response, 将它发送给spider引擎
                return HtmlResponse(url=request.url, body=html, request=request, encoding='utf-8')

        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
