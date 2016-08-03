import pyodbc

try:
	conn = pyodbc.connect('DRIVER={SQL Server};SERVER=kapytest1.database.windows.net,1433', user='kapygroup', password='Kapykapy1234', database='databaseTest1')
	cursor=conn.cursor()
	sql ="INSERT INTO dbo.newsTest2(title,newsdate, newstime, source, origURL, description,category) VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s')"%('a','','11','22','33','56f4a56s4fdsa46','politics')

	try:
		# Execute the  SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		conn.commit()
		print 'success insert data1'
	except:
		# Rollback in case there is any error
		conn.rollback()
		print "failed insert data1"

	sql ="INSERT INTO dbo.newsTest2(title,newsdate, newstime, source, origURL, description,category) VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s')"%('a','','121','232','333','56f4a56s34fdsa46','politics')

	try:
		# Execute the  SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		conn.commit()
		print 'success insert data2'
	except:
		# Rollback in case there is any error
		conn.rollback()
		print "failed insert data2"
	sql ="INSERT INTO dbo.newsTest2(title,newsdate, newstime, source, origURL, description,category) VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s')"%('aa','','121','232','333','56f4a56s34fdsa46','politics')

	try:
		# Execute the  SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		conn.commit()
		print 'success insert data2'
	except:
		# Rollback in case there is any error
		conn.rollback()
		print "failed insert data2"

	conn.close()

except:
	print "connection failed2"
