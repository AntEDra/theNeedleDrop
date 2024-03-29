# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class TheneedledropPipeline:

	def __init__(self):
		self.create_connetion()
		self.create_table()

	def create_connetion(self):
		self.conn = sqlite3.connect("fantanoScores.db")
		self.curr = self.conn.cursor()

	def create_table(self):

		self.curr.execute("""DROP TABLE IF EXISTS reviews_tb""")		

		self.curr.execute("""create table reviews_tb(
								url text,
								date text,
								artist text,
								album text,
								name text,
								score integer,
								tags text)""")

	def process_item(self, item, spider):

		self.store_db(item)
		return item

	def store_db(self,item):

		self.curr.execute("""insert into reviews_tb values (?,?,?,?,?,?,?)""",(
    		item['url'],
    		item['date'],
    		item['artist'],
    		item['album'],
    		item['name'],
    		item['score'],
    		item['tags']
    		))
		self.conn.commit()
