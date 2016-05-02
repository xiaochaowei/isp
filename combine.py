import csv
import MySQLdb
app_name_list = ["chrome", "firefox", "flashplayer", "thunderbird"]
conn = MySQLdb.connect(user = "root", passwd = "19920930", db = "ISP")
cursor = conn.cursor()
INSERT_SQL = """ INSERT INTO machineInfo(machine_id, country, isp, p_value, app_name) values ({machine_id}, "{country}", "{isp}", {p_value}, "{app_name}" ) ;"""
QUERY_SQL = """ SELECT country, isp from machine2isp where machine_id = {machine_id} ;"""
def readPvalue(app_name):
	fid = open(app_name+ "_profiles.csv", 'r')
	reader = csv.reader(fid,delimiter=",", quotechar="|")
	#for unit test
#	flag = 0 
	for row in reader:
#		if flag == 20:
#			break
#		flag = flag + 1 
		machine_id = row[0]
		p_value = row[1]
		comment_sql = QUERY_SQL.format(machine_id = machine_id)
		cursor.execute(comment_sql)
		data = cursor.fetchall()
		print len(data)
		for ins in data:
			country = ins[0]
			isp = ins[1]
			comment_sql = INSERT_SQL.format(\
				machine_id = machine_id, \
				country = country, \
				isp = isp, \
				p_value = p_value, \
				app_name = app_name)
			cursor.execute(comment_sql)
			conn.commit()

def getISPList(app_name):
	QUERYISP_SQL = """SELECT distinct(isp) from machineInfo where app_name = "{app_name}" ;""" 
	comment_sql = QUERYISP_SQL.format(app_name = app_name)
	cursor.execute(comment_sql)
	rows = cursor.fetchall()
	isp_list = []
	for row in rows:
		isp_list.append(row[0])
	return isp_list

def getData(app_name, isp):
	#return all the p_value under this ISP and app_name
	QUERYP_SQL = """ SELECT p_value from machineInfo where app_name = "{app_name}" and isp = "{isp}" ; """
	comment_sql = QUERYP_SQL.format(app_name = app_name, isp = isp)
	cursor.execute(comment_sql)
	rows = cursor.fetchall()
	p_value_list = []
	for row in rows:
		p_value = row[0]
		p_value_list.append(p_value)
	return p_value_list
def run():
	for app_name in app_name_list:
		readPvalue(app_name)
	#	isp_list = getISPList(app_name)
	#	for isp in isp_list:
	#		value_list = getData(app_name, isp)
	#		fid = open("data/" + app_name + "_" + isp,'w')
	#		for p in value_list:
	#			fid.write(p)
	#		fid.close()
run()
conn.close()
