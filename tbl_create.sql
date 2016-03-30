create database if not exists ISP;
USE ISP;
drop table if exists machine2isp;
CREATE TABLE machine2isp(
	machine_id integer primary key,
	country varchar(12),
	isp varchar(128) 
);
