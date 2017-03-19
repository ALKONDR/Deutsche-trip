from flickrapi import FlickrAPI
import json

FLICKR_PUBLIC = 'aa33a635b788c9cd400e1abf49e1df30'
FLICKR_SECRET = json.load(open('secret.json'))['flickr']


def get_images(country, season, quantity):

	flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
	extras = ['url_c']
	get_country = flickr.photos.search(tags=country, text = season, per_page=50, sort='relevance', extras = extras,
										safe_search=1, privacy_filter = 1)
	photos = get_country['photos']['photo']

	n = 0
	images = []
	for p in photos:
		if 'url_c' in p:
			images.append({'photo_url': p['url_c']})
			n += 1
			if n == quantity:
				break

	return images