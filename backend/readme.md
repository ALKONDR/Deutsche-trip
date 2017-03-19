<h2> Backend interfaces </h2>

Everything is now at `http://127.0.0.1:5000/`
* `/api/deutsche` - authorise to Deutsche Bank API
* `/api/deutsche/transactions/YYYYMMDD/YYYYMMDD` - JSON of user's transactions and sum of their amounts. Dates are optional. 
* `/api/instagram` - authorise to Instagram API
* `/api/instagram/photos/YYYYMMDD/YYYYMMDD` - get photos from Instagram during specified period. Due to sandbox API, only last 20 photos are available.
* `/api/status` - get JSON of API statuses:
* `/api/countries` - list of countries
* `/api/clear_session` - clears session (temporary solution of token expiration)
* `/api/flickr_get_photos/Country/Season` - get photos for future trips
* `/api/get_photos_any/Country/YYYYMMDD/YYYYMMDD` - get photos no matter which dates these are. It will be either instagram for past trips or flickr photos for future ones.

In case of problems with `flickrapi`, follow <a href="https://github.com/sybrenstuvel/flickrapi/issues/75">this</a> link.
