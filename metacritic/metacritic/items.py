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
	genre = Field()
	release_date = Field()
	distributor = Field()

	metascore = Field()
	
	meta_positive = Field()
	meta_mixed = Field()
	meta_negative = Field()


	userscore = Field()
	#user_positive = Field()
	#user_mixed = Field()
	#user_negative = Field()

	individual_meta_score = Field()
	critic_name = Field() 
	review_date = Field()
	media = Field()
	text = Field()

	#total_user_rating = Field()
	#individual_user_score = Field()
	#user_name = Field()

	##added 10/10 
	


