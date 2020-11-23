drop database agency;
create database agency;
use agency;

drop table if exists Agent;
drop table if exists Agent_phone;
drop table if exists Family;
drop table if exists Agent_age;
drop table if exists Team;
drop table if exists Operation;
drop table if exists Works_on;
drop table if exists Criminal;
drop table if exists Crimefield;
drop table if exists Victim;
#__________________________________________________________________________________________
CREATE TABLE Team ( Team_id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT , name varchar(50) NOT NULL);
insert into Team (name) values ('Uchiha');
insert into Team (name) values ('Senju');
insert into Team (name) values ('Sarutobi');
insert into Team (name) values ('Uzumaki');
insert into Team (name) values ('Huga');
insert into Team (name) values ('Nara');
#__________________________________________________________________________________________

CREATE TABLE Agent_age ( agent_DOB date  PRIMARY KEY NOT NULL, age int(3) );
insert into Agent_age values ('2000-01-01', 20);
insert into Agent_age values ('2000-02-01', 20);
insert into Agent_age values ('2001-02-01', 19);
insert into Agent_age values ('2002-04-01', 18);
insert into Agent_age values ('2003-04-01', 17);
insert into Agent_age values ('2013-04-01', 7);
insert into Agent_age values ('2015-04-01', 5);
#__________________________________________________________________________________________


CREATE TABLE Agent 
(
  id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name varchar(100) NOT NULL,
  sex varchar(7) NOT NULL,
  DOB date NOT NULL,
  FOREIGN KEY (DOB) REFERENCES Agent_age(agent_DOB),
  DOJ date NOT NULL,
  Team_id int(10),
  FOREIGN KEY (Team_id) REFERENCES Team (Team_id),
  Num_of_Kills int(3) NOT NULL,
  experience_in_Years int(2) NOT NULL,
  is_alive boolean NOT NUll,
  Mentor_id int(10),
  FOREIGN key (Mentor_id) REFERENCES Agent(id),
  street_num varchar(20),
  apartment_num varchar(20),
  door_num varchar(20),
  city_or_town varchar(50) NOT NULL,
  state varchar(50) NOT NULL,
  pincode int(6),
  is_working boolean NOT NULL
);
insert into Agent values (1, 'Madara', 'male', '2000-01-01', '2010-01-01', '1', '25','10',TRUE,NULL,'S001','A001','D001','Konoha','Land_of_fire','500032',TRUE);
insert into Agent values (2, 'Itachi', 'male', '2002-04-01', '2005-01-01', '1', '50','5',TRUE,'1','S001','A002','D002','Konoha','Land_of_fire','500032',TRUE);
insert into Agent values (3, 'Sasuke', 'male', '2002-04-01', '2010-04-01', '1', '10','14',TRUE,'2','S001','A002','D002','Konoha','Land_of_fire','500032',TRUE);
insert into Agent values (4, 'Naruto', 'male', '2003-04-01', '2010-04-01', '4', '100','15',TRUE,'2','S004','A002','D004','Konoha','Land_of_fire','500032',TRUE);
insert into Agent values (5, 'Boruto', 'male', '2013-04-01', '2016-04-01', '4', '11','17',TRUE,'1','S004','A002','D004','Konoha','Land_of_fire','500032',TRUE);
insert into Agent values (6, 'Himawari', 'female', '2015-04-01', '2016-04-01', '4', '11','17',TRUE,'5','S004','A002','D004','Konoha','Land_of_fire','500032',TRUE);
#_________________________________________________________________________________________________________________________________________________________________
CREATE TABLE Family
(
	name varchar(100) NOT NULL,
	relation varchar(100),
	sex varchar(7),
	agent_id int(10) NOT NULL,
	FOREIGN KEY (agent_id) REFERENCES Agent(id)
);
insert into Family values ('Indra', 'Ancestor', 'male', '1');
insert into Family values ('Shisui', 'Friend', 'male', '2');
insert into Family values ('Sakura', 'Wife', 'female', '3');
#_________________________________________________________________________

CREATE TABLE Agent_phone
(
	phone int(10) NOT NULL,
	agent_id int(10) NOT NULL,
	FOREIGN KEY (agent_id) REFERENCES Agent(id)
);
insert into Agent_phone values ('999111223','1');
insert into Agent_phone values ('999111224','2');
insert into Agent_phone values ('999111220','3');
#_____________________________________________________________________________


CREATE TABLE Operation
(
	id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(50) NOT NULL,
	status varchar(20) NOT NULL,
	Doc date NOT NULL
);
insert into Operation Values (1,'Claw-Rescue','Pending','2010-11-02');
insert into Operation Values (2,'Sasuke-rescue','Pending','2012-11-02');

#_______________________________________________________________________________


CREATE TABLE Criminal
(
	id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(50) NOT NULL,
	is_alive boolean NOT NULL,
	Age_in_years int(3) 
);
insert into Criminal values ('1', 'Kaguya Outsuki', '1','25');
insert into Criminal values ('2', 'Orochimaru', '1','50');
insert into Criminal values ('3', 'Kshinki', False,'60');
#___________________________________________

CREATE TABLE Victim
(
	name varchar(50) NOT NULL,
	criminal_id int(10) NOT NULL,
	FOREIGN KEY (criminal_id) REFERENCES Criminal(id),
	PRIMARY KEY (name, criminal_id)
);
insert into Victim values ('Sakura','2');
insert into Victim values ('Haguromo','1');
insert into Victim values ('Hamura','1');
insert into Victim values ('Boruto','3');

#__________________________________________________
CREATE TABLE Crimefield
(
	C_id int(10) NOT NULL,
	name varchar(50) NOT NULL,
	FOREIGN KEY (C_id) REFERENCES Victim(criminal_id),
	FOREIGN KEY (name) REFERENCES Victim(name),
	crimefield varchar(50) NOT NULL,
	PRIMARY KEY (C_id, name, crimefield)
);
insert into Crimefield values ('1','Haguromo',' Kaguya Tried to kill his son');
insert into Crimefield values ('1','Hamura',' Kaguya Tried to kill his son');
insert into Crimefield values ('2','Sakura','Manipulated Dark Sasuke');
insert into Crimefield values ('3','Boruto','Kshinki tried to extract tailbeast his Father');

#______________________________________________

CREATE TABLE Works_on
(
	c_id int(10) NOT NULL,
	o_id int(10) NOT NULL,
	v_name varchar(50) NOT NULL,
	t_id int(10) NOT NULL,
	FOREIGN KEY (c_id) REFERENCES Criminal(id),
	FOREIGN KEY (o_id) REFERENCES Operation(id),
	FOREIGN KEY (v_name) REFERENCES Victim(name),
	FOREIGN KEY (t_id) REFERENCES Team(Team_id)
);
insert into Works_on values ('2','2','Sakura','4');
insert into Works_on values ('3','1','Boruto','1');

#______________________________________________________________________________________________________________
