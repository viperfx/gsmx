import json
from pprint import pprint
import requests
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, Response
import subprocess
import simplejson
import os.path
def main():
	"""
	#########
	Sample output
	#########
	Kill+For+Love+Chromatics
	{u'SongID': 33463149, u'Url': u'http://tinysong.com/MW2S', u'ArtistName': u'Chromatics', u'AlbumName': u'Kill for Love', u'AlbumID': 7161817, u'ArtistID': 20984, u'SongName': u'Kill For Love'}
	I+Wanted+You+To+Feel+The+Same+The+Radio+Dept.
	{u'SongID': 35362351, u'Url': u'http://tinysong.com/10VYn', u'ArtistName': u'The Radio Dept.', u'AlbumName': u'Pet Grief', u'AlbumID': 1264393, u'ArtistID': 404316, u'SongName': u'I Wanted You to Feel the Same'}
	Inch+of+Dust+Future+Islands
	{u'SongID': 25822722, u'Url': u'http://tinysong.com/HF8P', u'ArtistName': u'Future Islands', u'AlbumName': u'In Evening Air', u'AlbumID': 4380400, u'ArtistID': 698851, u'SongName': u'Inch Of Dust'}
	Soft+Washed+Out
	{u'SongID': 31337051, u'Url': u'http://tinysong.com/HOgN', u'ArtistName': u'Washed Out', u'AlbumName': u'Within and Without', u'AlbumID': 6141745, u'ArtistID': 1187703, u'SongName': u'Soft'}
	Daniel+Bat+For+Lashes
	{u'SongID': 31786679, u'Url': u'http://tinysong.com/Of6h', u'ArtistName': u'Bat for Lashes', u'AlbumName': u'Last Night (Original Motion Picture Soundtrack)', u'AlbumID': 6623112, u'ArtistID': 404087, u'SongName': u'Daniel'}
	Abby+Tanlines
	{u'SongID': 35530078, u'Url': u'http://tinysong.com/13SLK', u'ArtistName': u'Tanlines', u'AlbumName': u'Mixed Emotions///eastvillageclub.tumblr.com', u'AlbumID': 7809227, u'ArtistID': 1159528, u'SongName': u'Abby'}
	Ceremony+[Alternate+12"+Version]+New+Order
	{u'SongID': 25940369, u'Url': u'http://tinysong.com/vT9L', u'ArtistName': u'New Order', u'AlbumName': u"Movement (Collector's Edition)", u'AlbumID': 3359329, u'ArtistID': 595, u'SongName': u'Ceremony [Alternate 12" Version]'}
	Passage+Exitmusic
	{u'SongID': 36236530, u'Url': u'http://tinysong.com/17A1g', u'ArtistName': u'Exitmusic', u'AlbumName': u'Passage', u'AlbumID': 7573719, u'ArtistID': 1667162, u'SongName': u'The Sea'}
	So+Glad+To+See+You+Hot+Chip
	{u'SongID': 9015011, u'Url': u'http://tinysong.com/iD7O', u'ArtistName': u'Hot Chip', u'AlbumName': u'The Warning', u'AlbumID': 2784856, u'ArtistID': 3821, u'SongName': u'So Glad to See You'}
	+A+Glorious+Time+Team+Ghost
	{u'SongID': 33940368, u'Url': u'http://tinysong.com/14BBv', u'ArtistName': u'Team Ghost', u'AlbumName': u'We All Shine', u'AlbumID': 7323507, u'ArtistID': 1462940, u'SongName': u'A Glorious Time'}
	"""
	url = "http://designers.mx/post/detail/futureMe/f-a-l-l/1728/"
	user = url.split("/")[-4]
	mix = url.split("/")[-3]
	mix_id = url.split("/")[-2]
	filename = user+'_'+mix+'_'+mix_id+'.json'
	# check if playlist has been parsed already
	if os.path.isfile(filename) == False:
   		proc = subprocess.Popen("scrapy crawl gsmx -a url=%s -o %s -t json" % (url, filename), shell=True)
		return_code = proc.wait()
	# Open json data to get the search queries for tinysong api
	json_data = open(filename)
	data = json.load(json_data)
	# if playlist not created already, Iterate through the json file and request the API with the formed query
	if os.path.isfile('playlist_'+filename) == False:
		for item in data:
			query = item['query']
			r = requests.get('http://tinysong.com/b/%s?format=json&key=0fc107bfb325fdb787d837b406d80d04' % (query))
			playlist = open('playlist_'+filename, 'a')
			load = simplejson.loads(r.text)
			playlist.write(simplejson.dumps(load, indent=4, sort_keys=True))
	json_data.close()
	if os.path.isfile('playlist_'+filename) == False:
		playlist.close()
	else:
		print(open('playlist_'+filename, 'r').read())


if __name__ == '__main__':
	main()