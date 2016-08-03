import urllib
import urllib2
from general import *
import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
from dataconnetTest3 import *
from newsItem import *
class newsSpider:



	def __init__(self):
		#newsSpider.category=category
		self.insertData()

	def find_PageItem(self,page_url):
		try:
			r= requests.get(page_url)
			soup = BeautifulSoup(r.content,'lxml')
			complete_title = soup.find('h1',{'itemprop':'headline'}).next
			title= complete_title.replace(' ','').replace("'","").replace('!','').replace(':','')[:49]
			print title
			timestamp=soup.find('time')
			if timestamp.has_attr('datetime'):
				date= timestamp['datetime'][:10]
				#print date
				time= timestamp['datetime'][11:19]
				#print time
			dateString=soup.find('time',{'itemprop':'datePublished'}).next.replace('\n','').replace(' ','')[9:]
			source_name= soup.find('div',{'itemprop':'sourceOrganization'}).find('a').next
			#print source_name
			origin_url=page_url
			#print origin_url
			if 'foxnews.com/politics' in origin_url:
				category = 'politics'
			elif 'foxnews.com/us' in origin_url:
				category = 'us'
			elif 'foxnews.com/opinion' in origin_url:
				category='opinion'
			elif 'foxnews.com/entertainment' in origin_url:
				category = 'entertainment'
			elif 'foxnews.com/tech' in origin_url:
				category='tech'
			elif 'foxnews.com/science' in origin_url:
				category = 'science'
			elif 'foxnews.com/health' in origin_url:
				category='health'
			elif 'foxnews.com/travel' in origin_url:
				category = 'travel'
			elif 'foxnews.com/world' in origin_url:
				category='world'
			elif 'foxnews.com/sports' in origin_url:
				category='sports'
			else:
				category='others'

			article_contents= soup.find('div',{'class':'article-text'}).find_all('p')
			description1=''
			for paragraph in article_contents:
				description1=description1+paragraph.text.replace("'",'')+'\n'
			#print description1
			#self, title,time,date,source_name,description,origin_url
			news = newsItem(title,complete_title,time,date,source_name,description1,origin_url,category)
			#insertRow(title,date,time,source_name,origin_url,description1)
			return news
		except:
			#pass
			print('skip this page')
			return None
	def crawl_urls(self,file_name):
		newsItems = []
		with open(file_name,'r') as f:
			for line in f:
				if 'print' or 'video' or 'latino' not in line:
					news= self.find_PageItem(line)

					if news is not None:
					#print news.title
					#print news.complete_title
					#print news.date
					#print news.time
					#print news.source_name
					#print news.origin_url
					#print news.description
					#print news.category
						newsItems.append(news)
				else:
					continue
		return newsItems
	def insertData(self):
		file_name='fox'+'/crawled.txt'
		newsItems=self.crawl_urls(file_name)
		print 'crawling finish'
		insertRow(newsItems)
		file_name='fox'+'/queue.txt'
		newsItems=self.crawl_urls(file_name)
		print 'crawling finish'
		insertRow(newsItems)

spider = newsSpider()
