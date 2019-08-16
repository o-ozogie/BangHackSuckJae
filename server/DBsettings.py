import pymysql

conn=pymysql.connect(host='localhost',user='root',password='variable',db='minitweet',charset='utf8')
curs=conn.cursor(pymysql.cursors.DictCursor)
