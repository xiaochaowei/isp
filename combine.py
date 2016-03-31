import csv
import MySQLdb
app_name_list = ["chrome", "firefox", "flashplayer", "thunderbird"]
conn1 = MySQLdb.connect(user = "root", passwd = "19920930", db = "machine2isp")
cursor_isp = conn1.cursor()
conn2 = MySQLdb.connect(user = "root", passwd = "19920930", db = "machineInfo")
curosr_app= conn2.curosr()
INSERT_SQL = """ INSERT INTO machineInfo(machine_id, country, isp, p_value, app_name) values ({machine_id}, "{country}", "{isp}", {p_value}, "{app_name}" ) ;"""
QUERY_SQL = """ SELECT country, isp from machine2isp where machine_id = {machine_id} ;"""
def readPvalue(app_name):
	fid = open(app_name+ "_profiles.csv", 'w')
	reader = csv.reader(fid,delimiter=",", quotechar="|")
	for row in reader:
		machine_id = row[0]
		p_value = row[1]
		comment_sql = QUERY_SQL.format(machine_id = machine_id)
		cursor_isp.execute(comment_sql)
		data = cursor_isp.fetchall()
		for ins in data:
			country = ins[0]
			isp = ins[1]
			comment_sql = INSERT_SQL.format(\
				machine_id = machine_id, \
				country = country, \
				isp = isp, \
				p_value = p_value, \
				app_name = app_name)
			cursor_app.execute(comment_sql)
			conn2.commit()

def getISPList(app_name):
	QUERYISP_SQL = """SELECT distinct(isp) from machineInfo where app_name = "{app_name}" ;""" 
	comment_sql = QUERYISP_SQL.format(app_name = app_name)
	cursor_app.execute(comment_sql)
	rows = cursor_app.fetchall()
	isp_list = []
	for row in rows:
		isp_list.append(row[0])
	return isp_list

def getData(app_name, isp):
	#return all the p_value under this ISP and app_name
	QUERYP_SQL = """ SELECT p_value from machineInfo where app_name = "{app_name}" and isp = "{isp}" ; """
	comment_sql = QUERYP_SQL.format(app_name, isp)
	cursor_app.execute(comment_sql)
	rows = cursor_app.fetchall()
	p_value_list = []
	for row in rows:
		p_value = srow[0]
		p_value_list.append(p_value)
	return p_value_list

def run():
	app_name = app_name_list[0]
	readPvalue(app_name)
	isp_list = getISPList(app_name)
	for isp in isp_list:
		value_list = getData(app_name, isp)
		fid = open(app_name + "_" + isp)
		for p in value_list:
			fid.write(p)
		fid.close()


