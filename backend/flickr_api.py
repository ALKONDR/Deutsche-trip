import flickr_api

flickr_api.set_keys(api_key = 'aa33a635b788c9cd400e1abf49e1df30',
					api_secret = '360d6e96a8737d66')


w = Walker(Photo.search, tags="switzerland")
for photo in w:
    print(photo.title)
