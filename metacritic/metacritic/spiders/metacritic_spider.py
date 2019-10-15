

from scrapy import Spider, Request 
from metacritic.items import MetacriticItem
import re 

class MetaCriticSpider(Spider):
    name = 'metacritic_spider'
    allowed_domains = ['www.metacritic.com']
    start_urls = ['https://www.metacritic.com/browse/movies/score/metascore/all/filtered?page=0']
    
    

    # find individual page of the movie list 
    def parse(self, response):
        result_urls = ['https://www.metacritic.com/browse/movies/score/metascore/all/filtered?page={}'.format(x) for x in range(0,126)]
        for url in result_urls:
            yield Request(url=url, callback=self.parse_result_page)
        

    def parse_result_page(self, response):

        detail_urls = response.xpath('//td[@class="clamp-summary-wrap"]/a/@href').extract()
        print(len(detail_urls))
        print('=' * 50)
        review_pages = ['https://www.metacritic.com{}'.format(x) for x in detail_urls]
        for review in review_pages:
            yield Request(url=review, callback=self.parse_review_page)
        

    def parse_review_page(self, response):

        
        movie_title = response.xpath('.//div[@class="product_page_title oswald"]/h1/text()').extract()[0]
        genre = response.xpath('.//div[@class="genres"]/span[2]/span/text()').extract()
        release_date = response.xpath('.//span[@class="release_date"]/span[2]/text()').extract()[0]

        metascore, userscore = response.xpath('.//div[@class="score fl"]/a/div/text()').extract()
        meta_positive, meta_mixed, meta_negative, user_positive, user_mixed, user_negative = response.xpath('.//div[@class="count fr"]/text()').extract() 



        #critc_ueser_review_pages = response.xpath('.//div[@class="score fl"]/a/@href').extract()
        #critic_review_page , user_review_page = ['https://www.metacritic.com{}'.format(x) for x in critc_ueser_review_pages]


        item = MetacriticItem()
        item['movie_title'] = movie_title
        item['release_date'] = release_date
        item['genre'] = genre

        item['metascore'] = metascore
        item['userscore'] = userscore

        item['meta_positive'] = meta_positive
        item['meta_mixed'] = meta_mixed
        item['meta_negative'] = meta_negative
        item['user_positive'] = user_positive
        item['user_mixed'] = user_mixed
        item['user_negative'] = user_negative


           
        yield item


            # title = review.xpath('.//h3[@class="ugc-review-title c-section-title heading-5 v-fw-medium  "]/text()').extract_first()
            # text = review.xpath('.//div[@class="ugc-review-body body-copy-lg"]//p/text()').extract_first()
            # try:
            #     helpful = review.xpath('.//button[@data-track="Helpful"]/text()').extract()[1]
            # except IndexError:
            #     helpful = ""
            # try:
            #     unhelpful = review.xpath('.//button[@data-track="Unhelpful"]/text()').extract()[1]
            # except IndexError:
            #     unhelpful = ""
