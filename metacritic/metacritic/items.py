# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item, Field


class MetacriticItem(Item):
	# movie_title = scrapy.Field()
	# release_date = scrapy.Field()

	# metascore = scrapy.Field()
 #    userscore = scrapy.Field()

    
  
 #    critic_review = scrapy.Field()
 #    user_review = scrapy.Field()

	movie_title = Field()
	release_date = Field()
	metascore = Field()
	userscore = Field()
	critic_review = Field()
	user_review = Field()
   