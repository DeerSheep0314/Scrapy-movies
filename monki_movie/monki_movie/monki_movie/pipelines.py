# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
from pymongo import MongoClient

from settings import mongo_host, mongo_port, mongo_db_name, mongo_db_collection

class MonkiMoviePipeline:
    def __init__(self):
        host = mongo_host
        port = mongo_port
        db_name = mongo_db_name
        sheet_name = mongo_db_collection
        client = MongoClient("mongodb://www.neohugh.art:27017/")
        client.monki.authenticate("monki", "monki", mechanism='SCRAM-SHA-1')
        db = client[db_name]
        self.post = db[sheet_name]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
