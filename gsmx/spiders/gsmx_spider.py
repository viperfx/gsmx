from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, Response
from gsmx.items import gsMixItem, gsMix
import os
class GsmxSpider(BaseSpider):
    name = "gsmx"
    allowed_domains = ["designers.mx", "spotify.com"]
    # start_urls = [
    #     "http://designers.mx/post/detail/futureMe/f-a-l-l/1728/",
    # ]
    def start_requests(self):
        request = Request(self.url,
                                  callback=self.parse)
        
        return  [request]
    def parse(self, response):
        user = response.url.split("/")[-4]
        mix = response.url.split("/")[-3]
        mix_id = response.url.split("/")[-2]
        filename = user+'_'+mix+'_'+mix_id
        dir_name = os.path.abspath("gsmx/scraped/%s" % filename)
        hxs = HtmlXPathSelector(response)
        spotify_data = hxs.select('//div[@class="track-list-wrap"]/@data-spotify-url').extract()
        page_title = hxs.select('//title/text()').extract()
    # Sample - https://embed.spotify.com/?uri=spotify:user:123512974:playlist:6lLLYkjRdusoZGDsDJAKjy
        spotify_url = spotify_data[0]
        response = Request(spotify_url, callback=self.get_playlist)
        response.meta['dir'] = dir_name
	response.meta['title'] = page_title
        return response
    def get_playlist(self, response):
    	dir_name = response.meta['dir']
        open(dir_name, 'wb+').write(response.body)
        hxs = HtmlXPathSelector(response)
        playlist = hxs.select('//ul[@id="content"]/li')
        playlist_data = []
        for song in playlist:
        	item = gsMix()
        	item['name'] = response.meta['title'][0]
        	item['title'] = song.select('ul/li[2]/text()').extract()[0][3:]
        	item['artist'] = song.select('ul/li[3]/text()').extract()[0]
        	item['query'] = (item['title']+' '+item['artist']).replace(" ", "+")
        	playlist_data.append(item)
       	return playlist_data
        # print response.body