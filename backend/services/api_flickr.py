from flickrapi import FlickrAPI

FLICKR_PUBLIC = 'aa33a635b788c9cd400e1abf49e1df30'
FLICKR_SECRET = '360d6e96a8737d66'



def get_images(country,quantity):

	flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
	extras = 'url_c'
	get_country = flickr.photos.search(tags=country, per_page=quantity, sort='relevance', extras = extras,
										safe_search=1)
	photos = get_country['photos']
	return photos

from pprint import pprint
pprint(get_images('India', 4))