import MySQLdb



db = MySQLdb.connect("121.40.72.237","prodadmin","s60vv47ng","fortunemarket_rd" )


cursor = db.cursor()


cursor.execute("SELECT VERSION()")


data = cursor.fetchone()

print "Database version : %s " % data


db.close()