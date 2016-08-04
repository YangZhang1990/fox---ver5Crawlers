import urllib
import urllib2
from general import *
import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
from newsSpider import newsSpider

class urlSpider:
	# Class variables shared among all instances

	#project_name =''
	project_name=''
	base_url= ''
	domain_name = ''
	queue_file =''
	crawled_file =''
	queue = set()
	crawled = set()

	def __init__(self,project_name,base_url,domain_name):
		urlSpider.project_name= project_name
		urlSpider.base_url= base_url
		urlSpider.domain_name = domain_name
		urlSpider.queue_file = urlSpider.project_name + '/queue.txt'
		urlSpider.crawled_file = urlSpider.project_name + '/crawled.txt'
		self.boot()
		self.crawl_page_urls('First Spider',urlSpider.base_url)

	@staticmethod
	def boot():
		create_project_dir(urlSpider.project_name)
		create_data_files(urlSpider.project_name,urlSpider.base_url)
		urlSpider.queue = file_to_set(urlSpider.queue_file)
		urlSpider.crawled = file_to_set(urlSpider.crawled_file)

	@staticmethod
	def crawl_page_urls(thread_name, page_url):
		#while len(urlSpider.crawled)<=1000:
			if page_url not in urlSpider.crawled:
				print(thread_name+ ' now crawling '+page_url)
				print('Queue: '+ str(len(urlSpider.queue)) + '| Crawled :'+str(len(urlSpider.crawled)))
				if len(urlSpider.crawled)<=10000:
					urlSpider.add_links_to_queue(urlSpider.find_links(page_url))
					urlSpider.queue.remove(page_url)
					urlSpider.crawled.add(page_url)
					urlSpider.update_files()
				else:
					print 'start crawl news items'
					newsSpider('fox')


	@staticmethod
	def find_links(base_url):
		try:
			r= requests.get(base_url)
			soup = BeautifulSoup(r.content,"lxml")
			original_links = soup.find_all('a')
			links=set()
			for link in original_links:
				full_url = urljoin(base_url,link.get('href'))
				#url_name=link.text
				#print full_url
				links.add(full_url)
		except:
			print('Error: can not crawl page')
			return set()
		return links

	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in urlSpider.queue:
				continue
			if url in urlSpider.crawled:
				continue
			if urlSpider.domain_name not in url:
				continue
			#if 'careers.foxnews' or 'radio.foxnews' or 'shop.foxnews' or 'on-air' or 'weather.blogs' in url:
				#print url
				#continue
			#if 'advertise' or 'help' or 'latino.foxnews' or 'live.foxnews' in url:
				#print url
				#continue
			if 'shop.foxnews' in url:
				#print url
				continue
			if 'live.foxnews' in url:
				#print url
				continue
			if 'careers.foxnews' in url:
				#print url
				continue
			if 'radio.foxnews' in url:
				#print url
				continue
			if 'help' in url:
				#print url
				continue
			if 'video.foxnews' in url:
				#print url
				continue
			if 'video.latino' in url:
				#print url
				continue
			if 'latino.foxnews' in url:
				#print url
				continue
			if 'nation.foxnews' in url:
				#print url
				continue
			if 'com/on-air' in url:
				#print url
				continue
			if 'print' in url:
				#print url
				continue
			urlSpider.queue.add(url)

	@staticmethod
	def update_files():
		set_to_file(urlSpider.queue,urlSpider.queue_file)
		set_to_file(urlSpider.crawled,urlSpider.crawled_file)



