# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
 
from scrapy.conf import settings
# from scrapy.exceptions import DropItem
# import logging

class PlantomjstestPipeline(object):
    def __init__(self):
        self.server = settings['MONGODB_SERVER']
        self.port = settings['MONGODB_PORT']
        self.db = settings['MONGODB_DB']
        self.col = settings['MONGODB_COLLECTION']

        connection = pymongo.MongoClient(self.server,self.port)
        db = connection[self.db]

        self.collection = db[self.col]

    
    def process_item(self, item, spider):
        # valid = True
        # for data in item:
        #     if not data:
        #         valid = False
        #         raise DropItem("Missing {0}!".format(data))
        # if valid:
        #     self.collection.insert(dict(item))
        #     logging.log(msg="Question added to MongoDB database!", level=logging.DEBUG, spider=spider)
        self.collection.insert(item)
        return item
