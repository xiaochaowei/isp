import MySQLdb
#isp_list = ["ROAD RUNNER HOLDCO LL", "COMCAST CABLE COMMUNICATIONS IN","OPENVISION TECHNOLOGIES INC", "EU-Z", "VERIZON INTERNET SERVICES IN","AT&T INTERNET SERVICE"]
SELECT_SQL = """SELECT p_value from machineInfo where isp = "{isp}" ;"""
conn = MySQLdb.connect(user = "root", passwd = "19920930", db = "ISP")
cursor = conn.cursor()
ISP_LIST_SQL = """ SELECT count(isp), isp from machineInfo group by isp having count(isp) between {num1} AND {num2} ; """
comment_sql = ISP_LIST_SQL.format(num1 = 100, num2= 120)
cursor.execute(comment_sql)
rows = cursor.fetchall()
isp_list = []
for row in rows:
	isp_list.append(row[1])
 
for i in range(0,len(isp_list)):
	isp_name = isp_list[i]
	file_name = isp_name.split(' ')[0]
	comment_sql = SELECT_SQL.format(isp = isp_name)
	cursor.execute(comment_sql)
	rows = cursor.fetchall()
	fid = open('data/'+file_name, 'w')
	for row in rows:
		fid.write(str(row[0]) + '\n')
	fid.close()

