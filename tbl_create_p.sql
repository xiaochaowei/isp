USE ISP;
drop table if exists machineInfo;
CREATE TABLE machineInfo(
	id integer primary key auto_increment,
	machine_id integer,
	country varchar(12),
	isp varchar(128),
	p_value FLOAT(20,10),
	app_name varchar(32)
);
