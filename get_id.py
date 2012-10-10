import json
from pprint import pprint
import requests
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, Response
import subprocess
import simplejson
import os.path
import grooveshark
from secrets import *
def main():
	grooveshark.init()
	grooveshark.authenticate_user(YOUR_USERNAME, YOUR_PASSWORD)
	songIDs = []
	songdata = []
	url = "http://designers.mx/post/detail/Clemensposch/hope-love/1845/"
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
			if r.json != []:
				print "Found song: %s " % r.json['SongName']
				songIDs.append(r.json['SongID'])
				songdata.append(r.json)
		playlist = open('playlist_'+filename, 'w')
		playlist.write(simplejson.dumps(songdata, indent=4))
		playlist.close()
	json_data.close()
	if os.path.isfile('playlist_'+filename) == False:
		pass
	else:
		data = open('playlist_'+filename, 'r').read()
		# print data
		songdata = simplejson.loads(data)
		for item in songdata:
			songIDs.append(item['SongID'])
	print songIDs
	user_input = raw_input("Do you want to create a playlist on grooveshark? y/n ")
	if user_input == 'y':
		resp = grooveshark.api_call('createPlaylist', {'name':'Designs.MX %s %s' % (user, mix),'songIDs':songIDs})
		print resp
if __name__ == '__main__':
	main()
