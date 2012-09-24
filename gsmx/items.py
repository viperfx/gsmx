# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class gsMixItem(Item):
    # define the fields for your item here like:
    title = Field()
    artist = Field()
    query = Field()
class gsMix(gsMixItem):
    name = Field()

    def __str__(self):
        return "Mix: name=%s url=%s" % (self.get('name'), self.get('title'))