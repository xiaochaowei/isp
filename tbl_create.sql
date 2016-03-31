create database if not exists ISP;
USE ISP;
drop table if exists machine2isp;
CREATE TABLE machine2isp(
	id integer primary key atuo_increment,
	machine_id integer,
	country varchar(12),
	isp varchar(128) 
);
