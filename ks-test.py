import MySQLdb
threshold = 50 
conn = MySQLdb.connect(user = "root", passwd = "19920930", db = "ISP")
cursor = conn.cursor()
ISP_LIST_QUERY  = "SELECT distinct(isp) from machineInfo; "
cursor.execute(ISP_LIST_QUERY)
isp_list = []
rows = cursor.fetchall()
for row in rows:
	isp_list.append(row[0])

QUERY_SQL = """SELECT p_value from machineInfo where isp ="{isp}"; """
p_list = []
valid_isp = []
for isp in isp_list:
	comment_sql = QUERY_SQL.format(isp = isp)
	cursor.execute(comment_sql)
	p_values = []
	rows = cursor.fetchall()
	for row in rows:
		p_values.append(row[0])
	if len(p_values) < threshold:
		continue 
	p_list.append(p_values)
	valid_isp.append(isp)
#for save data 
fid = open('isp_value.txt', 'w')
for vals in p_list:
	fid.write(','.join(str(tmp) for tmp in vals))
	fid.write('\n')
fid.close()
fid = open("valid_isp",'w') 
for isp in valid_isp:
	fid.write(isp)
	fid.write('\n')
fid.close()
from scipy import stats
p_value_list = []
fid = open('result.txt', 'w')
for val1 in range(0,len(p_list)):
	tmp_list = []
	for val2 in range(0, len(p_list)):
		print val1, val2
		tmp = stats.ks_2samp(p_list[val1], p_list[val2])		
		p = tmp[1]
		tmp_list.append(p)
	p_value_list.append(tmp_list)
	fid.write(','.join(str(tmp) for tmp in tmp_list))
	fid.write('\n')
fid.close()

