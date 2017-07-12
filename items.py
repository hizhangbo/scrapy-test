# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlantomjstestItem(scrapy.Item):
    _id = scrapy.Field()             # id
    user = scrapy.Field()            # 微博发送者
    status = scrapy.Field()          # 微博内容
    created_at = scrapy.Field()      # 微博发送者
    device = scrapy.Field()          # 发送设备
    reposts_count = scrapy.Field()   # 转发数
    comments_count = scrapy.Field()  # 评论数
    attitudes_count = scrapy.Field() # 点赞数
    search_text = scrapy.Field()     # 搜索文本
    url = scrapy.Field()             # 微博地址
