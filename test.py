import MySQLdb
conn = MySQLdb.connect(user = "root", passwd = "19920930", db = "isp")
cursor = conn.cursor()
INSERT_SQL = """ INSERT INTO machine2isp(machine_id, country,isp) values ({machine_id}, "{country}", "{isp}"); """
fid = open("machine_isp.csv",'r')
print "load data"
# data = fid.read()
# print "load success"
# fid.close()
# data_list = data.split('\n')
for line in fid:
	tmp = line.split(',')
	if type(tmp[0]) == type(""):
		continue
	print tmp
	machine_id = tmp[0]
	country = tmp[1]
	isp = tmp[2]
	print isp
	comment_sql = INSERT_SQL.format(machine_id = machine_id, country = country, isp = isp)
	cursor.execute(comment_sql)
conn.commit()