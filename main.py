import pymysql
import sys
import getpass
from datetime import date
import datetime
def Excellence():
	q1="select * from Agent order by NUM_of_Kills Desc"
	cursor.execute(q1)
	data=cursor.fetchall()
	string1= 'FIRST  PLACE GOES TO-------> ' + data[0][1]
	string2= 'SECOND PLACE GOES TO-------> ' + data[1][1]
	string3= 'THIRD  PLACE GOES TO-------> ' + data[2][1]
	string4= 'FOURTH PLACE GOES TO-------> ' + data[3][1]
	string5= 'FIFTH  PLACE GOES TO-------> ' + data[4][1]
	print("*******REPORT ON AGENT EXCELLENCE*******")
	print(string1)
	print(string2)
	print(string3)
	print(string4)
	print(string5)
	print("__________________________________________________________________")

def PROJECT_agents_of_Team():
	name='x123'
	print("ENTER THE ID OF THE TEAM : ")
	print("DON'T WORRY ADMIN. YOU CAN ALWAYS ENTER TEAM NAME AS IT IS UNIQUE :).IF YOU DON'T KNOW ID, PRESS 'SKIP' IN THE ID FIELD")
	id=input("TEAM_ID : ")
	if(id=='skip' or id=='Skip'or id=='SKIP'):
		name=input('PLEASE ENTER TEAM NAME : ')
	if(name!='x123'):
		q1="""select Team_id from Team where name = '%s';""" %(name)
		cursor.execute(q1)
		data=cursor.fetchall()
		if(len(data)==0):
			print("CAN'T FIND A TEAM WITH NAME " + name)
			print("______________________________________________________________________________________________________________________")
			return
		id=data[0][0]
	else:
		q3="select name from Team where Team_id='" + str(id) + "';"
		cursor.execute(q3)
		name=cursor.fetchone()
		if(name==None):
			print("INVALID ID")
			print("______________________________________________________________________________________________________________________")
			return
		name=name[0]
	q2="select * from Agent where Team_id='" + str(id) +"';"
	cursor.execute(q2)
	records=cursor.fetchall()
	if(len(records)==0):
		print("SORRY TEAM " + name + " IS EMPTY")
		print("______________________________________________________________________________________________________________________")
		return
	print("AGENT DETAILS BELONGING TO THE TEAM " + name + "...")
	for record in records:
		print(record[1] + " WITH AN ID " +str(record[0]) )
	print("______________________________________________________________________________________________________________________")
	
def AGE_REPORT():
	threshold= input("ENTER THE AGE. WE WOULD SHOW THE LIST OF AGENTS ABOVE THAT AGE : \n" )
	q1="select Agent.id, Agent.name, Agent_age.age from Agent JOIN Agent_age ON Agent.DOB=Agent_age.agent_DOB where age > " + threshold + " order by age Desc;"
	cursor.execute(q1)
	data=cursor.fetchall()
	if(len(data)==0):
		print("OOPS! NO ONE IN THE AGENCY IS THAT OLD...LOL :)")
		print("______________________________________________________________________________________________________________________")
		return
	for row in data:
		print(row[1] + " WiTH ID " + str(row[0]) + " IS " + str(row[2]) + " YEARS OLD")
		print(" ")
	print("______________________________________________________________________________________________________________________")

def Agregate():
	q1="select Avg(NUM_of_Kills) from Agent;"
	cursor.execute(q1)
	data=cursor.fetchone()
	print("ON AN AVERAGE AN AGENT KILLS " + str(data[0]) + " MEMBERS")
	print("______________________________________________________________________________________________________________________")

def Delete_an_operation():
	oid=input("ENTER THE ID OF THE OPERATION\n ")
	q1="select * from Operation where id=" + str(oid) + ";"
	cursor.execute(q1)
	data=cursor.fetchone()
	if(data==None):
		print("OPERATION DOES NOT EXIST") 
		print("______________________________________________________________________________________________________________________")
		return
	q2="delete from Works_on where o_id=" + str(oid) +";"
	cursor.execute(q2)
	q3="delete from Operation where id=" +str(oid) +";"
	cursor.execute(q3)
	connection.commit()
	print("DELETED.....")
	print("______________________________________________________________________________________________________________________")


def Update_Encounters():
	id=input("ENTER THE ID OF THE AGENT TO UPDATE HIS KILLS: ")
	q1="select * from Agent where id= " + id + ";"
	try:
		cursor.execute(q1)
	except:
		print("INVALID AGENT ID")
		return
	data=cursor.fetchone()
	if(data==None):
		print("INVALID AGENT ID")
		print("______________________________________________________________________________________________________________________")
		return
	x=input("ENTER THE NUMBER OF KILLS THE AGENT DID IN THE RECENT OPERATION: ")
	q2="update Agent set Num_of_Kills = Num_of_Kills+" + x + " where id=" + id +";"
	cursor.execute(q2)
	connection.commit()
	print("UPDATED.....YEEYA!!!!")
	print("______________________________________________________________________________________________________________________")

def Update_Operation():
	id=input("ENTER OPERATION ID: ")
	status=input("ENTER THE STATUS UPDATE: ")
	q1="select * from Operation where id=" + id + ";"
	cursor.execute(q1)
	data=cursor.fetchone()
	if (data==None):
		print("INVALID OPERATION ID" )
		print("______________________________________________________________________________________________________________________")
		return
	q2="Update Operation set status='" + status +"' where id=" + id + ";"
	cursor.execute(q2)
	connection.commit()
	print("UPDATED....YEEYA!!!!!")
	print("______________________________________________________________________________________________________________________")

def Analysis_Operation():
	oid=input("ENTER OPERATION ID : ")
	q1="select * from Operation where id=" + oid + ";"
	try:
		cursor.execute(q1)
	except:
		print(Exception)
		return
	data=cursor.fetchone()
	if (data==None):
		print("INVALID OPERATION ID" )
		print("______________________________________________________________________________________________________________________")
		return
	q2="select * from Operation where id=" + oid+ ";"
	cursor.execute(q2)
	data=cursor.fetchone()
	status=data[2]
	oname=data[1]

	q3="select * from Works_on where o_id=" + oid+ ";"
	cursor.execute(q3)
	data=cursor.fetchone()
	if(data==None):
		print("OOPS No WORK IS DONE ON THE OPERATION")
		print("______________________________________________________________________________________________________________________")
		return
	c_id=data[0]
	v_name=data[2]
	t_id=data[3]
	q4="select * from Criminal where id='" + str(c_id) +"';"
	cursor.execute(q4)
	data=cursor.fetchone()
	c_name=data[1]
	q5="select * from Agent where Team_id='" + str(t_id) +"';"
	cursor.execute(q5)
	records=cursor.fetchall()
	if(len(records)==0):
		print("SORRY TEAM " + str(t_id) + " IS EMPTY")
		print("______________________________________________________________________________________________________________________")
		return
	agent_name=list()
	agent_id=list()

	for record in records:
		agent_name.append(record[1])
		agent_id.append(record[0])

	print("\t \t \t*****REPORT ON OPERATION " + oname + "*****" )
	print(" ")
	print("THIS  OPERATION WAS PLANNED FOR THE CRIMINAL " + c_name +"\n")
	print("WITH AGENTS\n")
	print( agent_name[0] +" WITH ID " + str(agent_id[0]) + ","+  agent_name[1] +" WITH ID " + str(agent_id[1]) + " and "+ agent_name[2] +" WITH ID " + str(agent_id[2]))
	print("The OPERATION STATUS IS " + status)
	print("______________________________________________________________________________________________________________________")

def Search():
	sub=input("ENTER THE STRING YOU WANT TO SEARCH IN CRIMINAL DATABASE:")
	q1="Select * from Criminal where name like '%" + sub +"%';"
	cursor.execute(q1)
	data=cursor.fetchall()
	if(len(data)==0):
		print("SORRY! NO MATCH FOUND....")
		print("________________________________")
		return

	print("LIST OF CRIMINALS MATCHED")
	for row in data:
		print("THE NAME IS " +row[1] + " WITH ID " +str(row[0]))
		print(" ")
def Update_EXP():
	id=input("ENTER THE AGENT ID: ")
	q1="select DOJ,is_alive,is_working from Agent where id="+ id+";"
	try:
		cursor.execute(q1)
	except:
		print("PLEASE ENTER AN INTEGER FOR ID")
		return
	data=cursor.fetchone()
	if(data==None):
		print("INVALID AGENT ID")
	DOJ=str(data[0])
	is_alive=data[1]
	is_working=data[2]
	DOJ=DOJ.split('-')
	DOJ=int(DOJ[0])
	q2="Select curdate();"
	cursor.execute(q2)
	data=cursor.fetchone()
	Year=str(data[0])
	Year=Year.split('-')
	Year=int(Year[0])
	exp=Year-DOJ
	if(is_alive and is_working):
		q2="Update Agent set experience_in_Years=" + str(exp) + " where id=" + id +";"
		cursor.execute(q2)
		print("UPDATED......")
		connection.commit()

def Update_alive_Working():
	id=input("ENTER THE AGENT ID: ")
	q1="select * from Agent where id="+ id+";"
	try:
		cursor.execute(q1)
	except:
		print("PLEASE ENTER AN INTEGER FOR ID")
		return
	data=cursor.fetchall()
	if(len(data)==0):
		print("INVALID AGENT ID")
		return
	w=str(0)
	a=str(1)
	
	alive=input("IS THE AGENT ALIVE? (Y/N)")
	if(alive!='Y'  and alive!='N'):
		print("WRONG ENTRY ACESS DENIED\n")
		return
	if(alive=='N'):
		a=str(0)
	if(a=='1'):
		working=input("IS THE AGENT WORKING? (Y/N)")
		if(working!='Y' and working!='N'):
			print("WRONG ENTRY ACESS DENIED\n")
			return
		
		if(working=='N'):
			w=str(0)
	
	

	q2="update Agent set is_working=" + w + " where id=" + id + ";"
	q3="update Agent set is_alive=" + a + " where id=" + id + ";"

	cursor.execute(q2)
	cursor.execute(q3)
	connection.commit()
	print("UPDATED.....")
def create_agent():
    print("\n\n\t\tRECRUTING AN AGENT KINDLY ENTER THE DETAILS OF AGENT\n\n")
    Name = str (input("ENTER NAME :"))
    Gender = str (input ("ENTER GENDER (M/F) : "))
    if Gender[0] == "M":
        Gender = "male"
    else :
        Gender = "female"
    DOB = str (input ("DATE OF BIRTH (YYYY-MM-DD) : "))
    year,month,day = DOB.split('-')
    try:
        datetime.datetime(int(year),int(month),int(day))
    except:
        print("XXXXXXX INVALID DATE XXXXXXXXXX ")
        return
    StreeNum = str (input ("STREET NO : "))
    ApartmentNum = str (input ( "APARTMENT NO :"))
    DoorNum = str ( input ("DOOR NO : ") )
    City = str (input ("CITY : "))
    State = str (input ("STATE : "))
    Pincode = int (input ("PINCODE ( < 6 ) : "))
    Phone=[]
    Num_phone = int (input ("COUNT OF PHONE NUMBERS NEEDED TO BE ENTERED (PHONE NUMBERS CAN BE MANY) : "))
    for i in range(1,Num_phone+1,1):
        Phone.append(int ( input ("PHONE NUMBER - " + str(i) + " ( < 10 ) : ") ))
    #Phone = int ( input ("PHONE : "))
    print("\t\tDETAILS OF FAMILY")
    Family_name = str ( input ("ENTER NAME OF A FAMILY MEMBER : "))
    Family_relation = str ( input ("RELATION OF MEMBER TO AGENT : "))
    Family_gender = str ( input ("GENDER OF FAMILY MEMEBER (M/F) : "))
    if Family_gender[0] == 'M' :
        Family_gender = "male"
    else:
        Family_gender = "female"
    Today = date.today()
    #print(str(DOB))
    Age = Today.year - int (DOB.split('-')[0]) #Calulating Age 
    insert_agent_in_Age = """ insert into Agent_age values ('%s',%d)""" %(DOB,Age)
    try:
        cursor.execute(insert_agent_in_Age)
        connection.commit()
    except:
        duplicate = 1
        #connection.rollback()
        #print("\t\tERROR IN DETAILS PLEASE TRY AGAIN - 1 ")
        #return

    insert_agent_in_agent =  """ insert into Agent (name,sex,DOB,DOJ,Num_of_Kills,experience_in_Years,is_alive,Mentor_id,street_num,apartment_num,door_num,city_or_town,state,pincode,is_working) values ('%s','%s','%s','%s',0,0,1,NULL,'%s','%s','%s','%s','%s',%d,1) ;""" %(Name,Gender,DOB,Today,StreeNum,ApartmentNum,DoorNum,City,State,Pincode)
    try:
        cursor.execute(insert_agent_in_agent)
        connection.commit()
    except:
        connection.rollback()
        print("\t\tERROR IN DETAILS PLEASE TRY AGAIN - 2")
        return
    cursor.execute("select MAX(id) from Agent;")
    ID = cursor.fetchone()[0]
    for i in range(1,Num_phone+1,1):
        insert_agent_in_phone = """ insert into Agent_phone values (%d,%d)"""  % (Phone[i-1],ID)
        try:
            cursor.execute(insert_agent_in_phone)
            connection.commit()
        except:
            connection.rollback()
            print("\t\tERROR IN DETAILS PLEASE TRY AGAIN - 3")
            return
    insert_agent_in_Family = """ insert into Family values ('%s','%s','%s',%d)""" %(Family_name,Family_relation,Family_gender,ID)
    try:
        cursor.execute(insert_agent_in_Family)
        connection.commit()
    except:
        connection.rollback()
        print("\t\tERROR IN DETAILS PLEASE TRY AGAIN - 4")
        return
    print ("\n\n\t\t AGENT DETAILS INSERTION SUCCESSFUL   ")

def create_team():
    print("\n\n\t\t CREATING A TEAM KINDLY ENTER THE BELOW DETAILS\n\n")
    Tname = str ( input ("TEAM NAME : "))
    No = 3
    ID = []
    for i in range(1,No+1,1):
        ID.append( int ( input ('ENTER ID OF AGENT-' + str(i) + ' : ' ) ))
    insert_team = "insert into Team (name) values ('"  +Tname+"')"  
    #print(insert_team)
    try:
        cursor.execute(insert_team)
        connection.commit()
    except:
        connection.rollback()
        print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")
        return
    cursor.execute("select Max(Team_id) from Team;")
    TID = cursor.fetchone()[0]
    for i in range(1,No+1,1):
        try:
            cursor.execute("update Agent set Team_id = " + str(TID) + " where id = " + str(ID[i-1]) + ";")
            connection.commit()
        except:
            connection.rollback()
            print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")
            return
    print("\n\n\t\tTEAM CREATION SUCCESFUL")

def create_criminal():
    print("\n\n\t\t CRIMINAL ENTRY KINDLY ENTER THE BELOW DETAILS\n\n")
    Cname = str (input ("CRIMINAL NAME : "))
    Cage = int (input( "CRIMINAL APROX AGE : "))
    Num = int ( input("NUMBER OF VICTIMS AFFECTED : "))
    Vname = []
    Crimefield = []
    N_aff = []
    for i in range(1,Num+1,1):
        Vname.append(str (input("ENTER THE NAME OF THE VICTIM-" + str(i) +" : " )))
        N_aff.append( int ( input ("COUNT OF CRIMEFIELDS VICTIM-" + str(i) +" HAS BEEN AFFECTED : ")))
        Crimefield.append([])
        for j in range(1,N_aff[i-1]+1,1):
            Crimefield[i-1].append( str (input("ENTER THE CRIMEFIELD-" +str(j)+ " AT WHICH VICTIM-" + str(i) +  " AFFECTED : ")))
    
    insert_criminal = "insert into Criminal (name,is_alive,Age_in_years) values('"+str(Cname)+"',1,"+str(Cage)+");"
    try:
        cursor.execute(insert_criminal)
        connection.commit()
    except:
        connection.rollback()
        print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")
        return
    cursor.execute("select Max(id) from Criminal;")
    CID = cursor.fetchone()[0]
    for i in range(1,Num+1,1):
        try:
            cursor.execute("insert into Victim values ('" + str(Vname[i-1]) + "'," +    str(CID)  +");")
            connection.commit()
        except:
            connection.rollback()
            print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")
            return
    for i in range(1,Num+1,1):
        for j in range(1,N_aff[i-1]+1,1):
            try:
                cursor.execute("insert into Crimefield values ('"+str(CID)+ "','" + str(Vname[i-1]) + "','" + str(Crimefield[i-1][j-1])  + "');")
                connection.commit()
            except:
                connection.rollback()
                print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")
                return
    print("\n\n\t\tCRIMINAL ENTRY SUCCESSFUL")     



def create_operation():
    print("\n\n\t\t CREATING AN OPERATION KINDLY ENTER THE BELOW DETAILS\n\n")
    Oname = str (input("NAME OF THE OPERATION : "))
    Today = date.today()
    status = "RUNNING"
    insert_operation = "insert into Operation  (name,status,Doc) values ('"+ str(Oname) + "','" + str(status) + "','"  +str(Today) + "');"
    try:
        cursor.execute(insert_operation)
        connection.commit()
    except:
        connection.rollback()
        print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")
        return
    cursor.execute( " select Max(id) from Operation;")
    OID = cursor.fetchone()[0]
    OCID = int (input("ID OF TARGET CRIMINAL : "))
    OTID = int (input("ID OF TEAM : "))
    try:
        Nvic = cursor.execute("select name from Victim where criminal_id = " + str(OCID) + ";")
        Obj = cursor.fetchall()
        connection.commit()
    except:
        connection.rollback()
        print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")
        return

    OVname = []
    for i in range(1,Nvic+1,1):
        OVname.append(Obj[i-1][0])
    for i in range(1,Nvic+1,1):
        try:
            cursor.execute("insert into Works_on values (" + str(OCID) + "," + str(OID)  + ",'" + str(OVname[i-1]) + "'," + str(OTID) + ");")
            connection.commit()
        except:
            connection.rollback()
            print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")
            return
    print("\n\n\t\t OPERATION CREATION SUCCESSFUL")

def update_mentor_id():
    print("\n\n\t\tUPDATING MENTOR ID")
    AID = int(input("ENTER AGENT ID : "))
    MID = int ( input ("ENTER MENTOR ID OF AGENT : "))
    try:
        cursor.execute("update Agent set Mentor_id = " + str(MID) + " where id = " + str(AID)  + " ;")
        connection.commit()
    except:
        connection.rollback()
        print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")
        return

def update_live_criminal():
    print("\n\n\t\tUPDATING CRIMINAL ALIVE STATUS")
    CUID = int ( input("ENTER ID OF CRIMINAL : "))
    IS = str ( input ("IS CRIMINAL ALIVE (Y/N) : "))
    yes=1
    if IS == "N":
        yes = 0
    try:
        cursor.execute("update Criminal set is_alive = " + str(yes) +" where id = "  +str (CUID)  + " ;") 
        connection.commit()
    except:
        connection.rollback()
        print("\t\tERROR IN DETAILS PLEASE TRY AGAIN")

try:
    Username = input("ENTER USERNAME : ")
    Password = getpass.getpass(prompt = "ENTER PASSWORD : ")
    Chances=3
    while Password != 'ENTER_YOUR_PASSWORD' or Username != 'root':#please change the password and username here.
        print("\n    USERNAME OR PASWORD IS INCORRECT")
        Chances-=1
        if Chances != 0:
            print("\n\t\tLAST %d CHANCES LEFT" %(Chances))
        else:
            print("\n\t\tSESSION EXPIRED")
            sys.exit()
        Username = input("ENTER USERNAME : ")
        Password = getpass.getpass(prompt = "ENTER PASSWORD : ")
    
    connection = pymysql.connect(host = '127.0.0.1', user = Username, password = Password, db = 'agency', port=3306)#please make port changes here
    cursor = connection.cursor()
    while(1):
        print("\n\n\t\t\t AGENCY MANAGMENT SYSTEM")
        print('\n\n\nSELECT A GATEWAY\n\n')
        print("1.RECRUTE AN AGENT")
        print("2.CREATE A TEAM")
        print("3.CRIMINAL ENTRY")
        print("4.CREATE AN OPERATION")
        print("5.UPDATE MENTOR-ID")
        print("6.UPDATE CRIMINAL ALIVE STATUS")
        print("7.RETRIVE TOP 5 AGENTS")
        print("8.RETRIVE TEAM AGENTS")
        print("9.AGE ANALYSIS")
        print("10.AGENT AVERAGE ENCOUNTERS")
        print("11.ABORT OPERATION")
        print("12.UPDATE ENCOUNTERS")
        print("13.UPDATE OPERATION STATUS")
        print("14.OPERATION ANALYSIS")
        print("15.SEARCH CRIMINAL")
        print("16.UPDATE EXPERIENCE")
        print("17.UPDATE AGENT STATUS")
        print("18.LOGOUT FROM THE SESSION")
        index= int (input("\n\nTYPE THE NUMBER OF SELECTED GATEWAY : "))
        if index == 1:
            create_agent()
        elif index == 2:
            create_team()
        elif index == 3:
            create_criminal()
        elif index == 4:
            create_operation()
        elif index == 5:
            update_mentor_id()
        elif index == 6:
            update_live_criminal()
        elif index == 7:
            Excellence()
        elif index == 8:
            PROJECT_agents_of_Team()
        elif index == 9:
            AGE_REPORT()
        elif index == 10 : 
            Agregate()
        elif index == 11  :
            Delete_an_operation()
        elif index == 12 :
            Update_Encounters()
        elif index == 13: 
            Update_Operation()
        elif index == 14 : 
            Analysis_Operation()
        elif index == 15:
            Search()
        elif index == 16: 
            Update_EXP()
        elif index == 17: 
            Update_alive_Working()
        else:         
            sys.exit()
    
except Exception as E:
    connection.rollback()
    print("EXECEPTION OCCURED", E)
connection.close()