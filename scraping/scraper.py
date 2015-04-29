import lxml
from lxml import html
import requests

'''
link dump:
http://www.poemhunter.com/p/m/l.asp?p=1&l=top500
http://www.hwlongfellow.org/poems_front.php
http://www.poemhunter.com/top-100-poems/
'''

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

