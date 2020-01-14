# Metacritic -- Scrapy Project

Launched in January 2001, ``Metacritic`` has evolved over the last decade to distill critics' voices into a single Metascore, a weighted average of the most respected critics writing reviews online and in print.  Metascores range from 0-100, with higher scores indicating better overall reviews. Metascores are highlighted in three colors for instantly compare: green scores for favorable reviews, yellow scores for mixed reviews, and red scores for unfavorable reviews.

## Inspiration 
Do you check IMDB and Rotten Tomato scores before watching a movie? As a regular moviegoer, I always check critic scores on [Metacritic][Metacritic]. At the time when I was deciding the topic for this project, two movies on my list caught my eyes: Joker and Parasite. They are both crime movies that are highly rated by the audience. Both scored more than 90 after they took home Top Prize at Film Festivals. However, Joker’s critic score dropped significantly to 59 around its release date, while Parasite's score remains the same.

Considering the difference in score for these two movies made me think of a two key questions:

* Why do movie scores change overtime and how?
* Do critics have movie preferences?

This project is intended to answer the questions above by scraping metacritic.com using scrapy and conducting natural language processing (NLP), sentiment and numerical data analysis together with data visualization using Pandas.

## Data Scraped 
Two separate spiders are implemented to avoid scraping duplicated information for each movie. Spider 1 scraped the first layer along the list of 'Best Movies of All Time',  features including the following:

* Movies titles
* Movies genre
* Distributor
* Release date
* Metascore and userscore
* Number of positive, mixed, negative reviews

Spider 2 goes deeper and scraped each movie’s individual reviews with the following features:

* Critic’s Name
* Media Name
* Critic Individual Score
* Review Date
* Review Content

The dataset can be found [here][dataset].

## About Me

Hanxiao(Mia)Zhang
[@Blogs](https://nycdatascience.com/blog/student-works/metacritic-exploring-critic-movie-reviews/)
[@LinkedIn](https://www.linkedin.com/in/zhanghanxiao/) 
miazhx2013@gmail.com

<!-- Markdown link & img dfn's -->
[Metacritic]: https://www.metacritic.com/
[dataset]: https://www.kaggle.com/miazhx/metacritic-movie-reviews
[blog]: https://nycdatascience.com/blog/student-works/metacritic-exploring-critic-movie-reviews/
