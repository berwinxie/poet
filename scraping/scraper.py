import lxml
from lxml import html
import requests

links = {
			'poetryfoundation':'http://www.poetryfoundation.org/poem/',	
			
		}

def scrape():
	for site, url in links.iteritems():
		print 'scraping', site, 'at url', url
		
'''
input: takes in sitename for parsing info and data to parse

return: dictionary of {'poemname':'poem'}
'''
def parse(site):
	print 'parsing' 

