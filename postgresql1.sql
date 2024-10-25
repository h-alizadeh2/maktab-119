CREATE TYPE status as enum('ACTIVE','COMPLETED','CANCELED'); 

drop table project;
CREATE TABLE project(
	project_id serial primary key,
	name text not null,
	start_date TIMESTAMP,
	end_date TIMESTAMP,
	project_status status
);

select * from project;

CREATE TABLE task1(
	id serial primary key,
	title text not null,
	description text not null,
	due_date TIMESTAMP
);

select * from task;


CREATE TABLE Employee(
	id serial primary key,
	name text not null,
	role text not null,
	hired_date TIMESTAMP
);

select * from Employee;

CREATE TABLE skils(
	id serial primary key,
	name text not null,
	level text not null
	
);

select * from Skils;

drop table table1;
CREATE TABLE table1(
	id serial primary key,
	parent_id int,
	CONSTRAINT fk_project
	foreign key(parent_id) references project(project_id)
	
);
select * from table1;