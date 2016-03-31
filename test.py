import sys
import csv
import MySQLdb
import lcs
conn = MySQLdb.connect(user = "root", passwd = "19920930", db = "ISP")

cursor = conn.cursor()
INSERT_SQL = """ INSERT INTO machine2isp(machine_id, country,isp) values ({machine_id}, "{country}", "{isp}"); """
UPDATE_SQL = """UPDATE machine2isp set isp = "{newisp}" where machine_id = {machine_id} and isp = "{isp}"; """ 
fid = open("/home/xiaocw/data/machine_isp.csv",'r')
print "load data"
reader = csv.reader(fid,delimiter=",", quotechar="|")
print "load success"
machineList = {}
flag = 1
eps = 0.7
for row in reader:
	if flag == 1:
		flag = flag + 1
		continue
	print flag
	flag = flag+ 1
	machine_id = row[0]
	isp = row[2]
	country = row[1]
	if isp == "":
		continue
	if machineList.has_key(machine_id):
		if isp in machineList[machine_id]:
			continue	
		else:
			index = -1
			max_sim = -1
			for isp_idx in range(0, len(machineList[machine_id])):
				isp_sub = machineList[machine_id][isp_idx]
				common_len = lcs.lcs(isp, isp_sub)
				sim = float(common_len) / max(len(isp), len(isp_sub))
				#print sim
				#print isp_sub, isp
				if sim > eps and max_sim < sim:
					index = isp_idx
					max_sim = sim
			if index != -1:
				#update
				if len(isp) < len(machineList[machine_id][index]):
					   	machineList[machine_id][index] = isp
						comment_sql = UPDATE_SQL.format(newisp = isp, machine_id = machine_id,  isp = machineList[machine_id][index])
						cursor.execute(comment_sql)
						conn.commit()
				else:
					continue
			else:
				machineList[machine_id].append(isp)
				comment_sql = INSERT_SQL.format(machine_id = machine_id, country = country, isp = isp)
				cursor.execute(comment_sql)
				conn.commit()
	else:
		machineList[machine_id] = []
		machineList[machine_id].append(isp) 
		comment_sql = INSERT_SQL.format(machine_id = machine_id, country = country, isp = isp)
		cursor.execute(comment_sql)	
		conn.commit()
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
