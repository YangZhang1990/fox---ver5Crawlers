import pyodbc
from newsItem import *


def insertRow(newsItems):
	try:
		conn = pyodbc.connect('DRIVER={SQL Server};SERVER=kapytest1.database.windows.net,1433', user='kapygroup', password='Kapykapy1234', database='databaseTest1')
		cursor=conn.cursor()
		for news in newsItems:
			# Prepare SQL query to INSERT a record into the database.

			sql ="INSERT INTO dbo.newsTest(uniqueName,newsTitle,newsdate, newstime, source, origURL, description,category) VALUES (?,?,?,?,?,?,?,?)"

			try:
				# Execute the  SQL command
				cursor.execute(sql,(news.title,news.complete_title,news.date,news.time,news.source_name,news.origin_url,news.description,news.category))
				# Commit your changes in the database
				conn.commit()
				print 'success insert data'
			except:
				# Rollback in case there is any error
				conn.rollback()
				print "failed insert data"

		conn.close()
		print 'insertion finish'

	except:
		print "connection failed2"
