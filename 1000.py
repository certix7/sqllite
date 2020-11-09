import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="stars")
cursor = connection.cursor()
# Query for creating table
ArtistTableSql = """
CREATE TABLE sites (  id INT (11) NOT NULL AUTO_INCREMENT ,
	link VARCHAR(255) NOT NULL ,
	PRIMARY KEY(id))"""

cursor.execute(ArtistTableSql)

#-----------------------------------------------------------------


def add(arg=""):
	#
#database connection
	connection = pymysql.connect(host="localhost", user="root", passwd="", database="stars")
	cursor = connection.cursor()

	# queries for inserting values

	files='data.txt'
	count=1
	with open(files,"r") as wordlist_file:
			for line in wordlist_file:
				test_url = line.strip()
				count+=1
				print(count)
				#add(test_url)

				insert1 = "INSERT INTO sites(link) VALUES('{0}' );".format(test_url)

				#executing the quires
				cursor.execute(insert1)


				#commiting the connection then closing it.
				connection.commit()



	connection.close()


add("")
