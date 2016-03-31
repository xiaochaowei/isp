import sys
import csv
import MySQLdb
import lcs
#conn = MySQLdb.connect(user = "root", passwd = "19920930", db = "ISP")

#cursor = conn.cursor()
INSERT_SQL = """ INSERT INTO machine2isp(machine_id, country,isp) values ({machine_id}, "{country}", "{isp}"); """
UPDATE_SQL = """UPDATE machine2isp set isp = {isp} where id = {id}; """ 
fid = open("/home/xiaocw/data/machine_isp.csv",'r')
print "load data"
#data = fid.read()
reader = csv.reader(fid,delimiter=",", quotechar="|")
print "load success"
machineList = {}
flag = 1
eps = 0.7
for row in reader:
	if flag == 1:
		flag = flag + 1
		continue
	flag = flag+ 1
	#tmp = data_list[i].split(',')
	machine_id = row[0]
	isp = row[2]
	country = row[1]
	if machineList.has_key(machine_id):
		if machineList[machine_id].find(isp) != -1:
			continue	
		else:	
			for isp_sub in machineList[machine_id]:
				common_len = lcs(isp, machineList[machine_id]）
				if float(common_len) / max(len(isp), len(machineList[machine_id])) > eps:
					if len(isp) < len(machineList[machine_id]):
						comment_sql = UPDATE_SQL.format(id = id, isp = isp)
						cursor.execute(comment_sql)
			else:i
				comment_sql = INSERT_SQL(machine_id = machine_id, country = country, isp = isp)
				cursor.execute(comment_sql)	
			print row
			print "compare" 
			print machineList[machine_id]
		continue
	else:
		machineList[machine_id] = []
		machineList[machine_id].append(isp)	
#for line in fid:
#	tmp = line.split(',')
#	if type(tmp[0]) == type(""):
#		continue
#	print tmp
#	machine_id = tmp[0]
#	country = tmp[1]
#	isp = tmp[2]
#	print isp
#	comment_sql = INSERT_SQL.format(machine_id = machine_id, country = country, isp = isp)
#	cursor.execute(comment_sql)
#	print "line:",i,len(data_list)
fid.close()
#conn.commit()
