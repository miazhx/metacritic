### Critic Review Spider 

from scrapy import Spider, Request 
from metacritic.items import MetacriticItem
import re 

class MetaCriticSpider2(Spider):
    name = 'metacritic_spider2'
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
        review_pages = ['https://www.metacritic.com{}/critic-reviews'.format(x) for x in detail_urls]
        for review in review_pages:
            yield Request(url=review, callback=self.parse_review_page)
        

    def parse_review_page(self, response):

        reviews = response.xpath('//div[@class="review pad_top1 pad_btm1"]')
        print(len(reviews))
        print('=' * 50) 
        for review in reviews:

            movie_title = response.xpath('.//div[@class="product_page_title upper pad_top2 pad_btm_half oswald"]/a/h1/text()').extract()[0]
            
            try:
                distributor = response.xpath('//span[@class="distributor"]/a/text()').extract()[0]
            except:
                distributor = None


            release_date = response.xpath('.//span[@class="release_date"]/span[2]/text()').extract()[0]

            try:
                metascore, userscore = response.xpath('.//a[@class="metascore_anchor"]/span/text()').extract()
            except:
                metascore = None
                userscore = None



            individual_meta_score = review.xpath('.//div[@class="left fl"]/div/text()').extract_first()
            
            try:
                text = review.xpath('.//div[@class="summary"]/a/text()').extract_first().strip()
            except:
                text = None
            try:
                critic_name = review.xpath('.//span[@class="author"]/a/text()').extract_first()
            except:
                critic_name = None     
            try:
                review_date = review.xpath('.//span[@class="date"]/text()').extract_first()
            except:
                review_date = None              
            try:
                media = review.xpath('.//span[@class="source"]/a/img/@title').extract_first()
            except:
                media = None 

            




            item = MetacriticItem()
            item['individual_meta_score'] = individual_meta_score
            item['critic_name'] = critic_name
            item['review_date'] = review_date
            item['movie_title'] = movie_title
            item['media'] = media
            item['text'] = text
            item['distributor'] = distributor
            item['release_date'] = release_date
            item['metascore'] = metascore
            item['userscore'] = userscore

               
            yield item