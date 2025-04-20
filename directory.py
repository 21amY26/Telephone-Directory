from dotenv import load_dotenv
import os
import mysql.connector as mycon
from prettytable import PrettyTable, from_db_cursor

load_dotenv()
password=os.getenv("MYSQL_PASSWORD")
mc=mycon.connect(user='root',host='localhost',password=password)
c=mc.cursor()
c.execute('''create database if not exists phonebook''')
c.execute('''use phonebook''')
print()

x='WELCOME TO THE PHONEBOOK'
print(x.center(80,'~'))
print('Login to Access Phonebook'.center(81))

def login():
   while True:
      username=input('Please enter username:     ')
      password=input('Please enter password:     ')
      if username=='USER' and password=='IamUser21@tel':
         print('LOGIN SUCCESSFUL! HELLO USER!')
         break
      elif username=='ADMIN' and password=='IamAdmin21@tel':
         print('LOGIN SUCCESSFUL! HELLO ADMIN!')
         break
      else:
         print('Invalid login. TRY AGAIN!')
   return username
user=login()
c.execute('''show tables''')
check=c.fetchall()
if ('tel_dir',) not in check:
   c.execute('''create table tel_dir(NAME varchar(30) NOT NULL, PHONE_NUMBER bigint PRIMARY KEY, ADDRESS varchar(500) NOT NULL,CITY_NAME varchar(20) NOT NULL, PINCODE int(6) NOT NULL)''')
   #inserting phonebook records
   c.execute('''insert into tel_dir values ('Amisha Singh',8830106271,'C-50, Hyderabad Estate, Nepeansea Road','South Bombay',400036)''')
   c.execute('''insert into tel_dir values ('Abhay Raj Singh',7304704593,'12-Delta Seawoods Residency, Seawoods','Navi Mumbai',400706)''')
   c.execute('''insert into tel_dir values ('Aditya Gupta',8097757368,'F-702, Nebula CHS, Gomti Nagar','Lucknow',226010)''')
   c.execute('''insert into tel_dir values ('Advait Satpute',9004226796,'H-26, Blueridge Apartments, Hinjewadi Phase 1','Pune',411057)''')
   c.execute('''insert into tel_dir values ('Adwita Singh',7021820697,'H-109, Sreeji Heights, Opp. Zudio, Kharghar Sec-19','Navi Mumbai',410210)''')
   c.execute('''insert into tel_dir values ('Adyan Shaikh',9004330748,'Werna 206, Balaji Ltd, Kokapet, K V Rangareddy','Hyderabad',500075)''')
   c.execute('''insert into tel_dir values ('Anika Gupta',9082479753,'Iris-503, Kesar Harmony, Kharghar Sec-6','Navi Mumbai',410210)''')
   c.execute('''insert into tel_dir values ('Ansh Rajpurohit',9653406629,'G-908, Willow Villas','Lucknow',226001)''')
   c.execute('''insert into tel_dir values ('Arnav Bhate',8219328838,'A-2306, Ishaan Apartments','Nagpur',440001)''')
   c.execute('''insert into tel_dir values ('Aryan Sahu',8104628644,'A-1306, Palm Beach Residency, Palm Beach Road, Nerul(W)','Navi Mumbai',400076)''')
   c.execute('''insert into tel_dir values ('Ashwin Thakur',9831799209,'K-22, Orbit Kanishka, Girwa','Udaipur',313001)''')
   c.execute('''insert into tel_dir values ('Asmita Pillai',9867120874,'E-901, Luxuria Apartments, Near Lulu Mall NH Bypass','Trivandrum',605036)''')
   c.execute('''insert into tel_dir values ('Atharva Krishnan',8928974389,'PRS Lakeville Bungalow, Ullor Road','Akkulam',695011)''')
   c.execute('''insert into tel_dir values ('Bhooomi Singh',7021045172,'2301-Alpha, Brij Hari Apartments, Drummond Rd','Prayagraj',211001)''')
   c.execute('''insert into tel_dir values ('Bhoomika Sinha',8169723787,'90-B, Nice Apce Apartments, Karond Bypass Rd','Bhopal',462001)''')
   c.execute('''insert into tel_dir values ('Dhanush Shetty',7506490234,'F-2404 WEST, Sunrise Residency, Near ICICI Bank Sujathanagar','Vishakapatnam',530007)''')
   c.execute('''insert into tel_dir values ('Dhruv Joshi',8196737757,'B-101, Sai Niva Chs, Ulwe Sec-19B','Navi Mumbai',410206)''')
   c.execute('''insert into tel_dir values ('Ishaan Pathare',7506410708,'Moana-A-1001, Drymond Residency, CBD Belapur','Navi Mumbai',400614)''')
   c.execute('''insert into tel_dir values ('Kecia Tamhane',8691853416,'D-809, Phoenix Halcyon, Near FNCC','Hyderabad',500027)''')
   c.execute('''insert into tel_dir values ('Kundan Maiti',9224122686,'30-L, Sree Balaji, Tollygunge','Kolkata',700015)''')
   c.execute('''insert into tel_dir values ('Japsiftee Ahuja',9716189006,'76, Bawa Residence, Sector 22','Chandigarh',160022)''')
   c.execute('''insert into tel_dir values ('Manasvi Gawde',9967927744,'D-46, Millenium Towers, Sanpada Sec-19','Navi Mumbai',400705)''')                       
   c.execute('''insert into tel_dir values ('Mansee Rana',9833722195,'34A WEST, Shree Balaji WindPark, Sardar Patel Ring Rd','Amhedabad',380001)''')
   c.execute('''insert into tel_dir values ('Mrinali Charhate',8104158875,'C-801, Akshar Alvario, Nerul Sec-27','Navi Mumbai',400706)''')
   c.execute('''insert into tel_dir values ('Om Amar',7738011507,'C-34, Vasundhara Regency Apartment, Permanand Path','Patna',801505)''')
   c.execute('''insert into tel_dir values ('Pratham Deepak',8097642740,'B-907, Beryl Corale, Near Raysan Petrol Pump','Gandhinagar',382012)''')
   c.execute('''insert into tel_dir values ('Rahul Mourya',7738973147,'ORO Elements, Off Kursi Road','Lucknow',226001)''')
   c.execute('''insert into tel_dir values ('Samiksha Srivatsan',9653194254,'A-65, Ceebros Apartments, No.17, Besant Rd','Chennai',600001)''')
   c.execute('''insert into tel_dir values ('Shloak Maheshwari',7506039855,'2A, Aparna Prem, 2, Mahatma Gandhi Rd','Agra',223007)''')


print()
print("Welcome to THE PHONEBOOK!")
print()

c.execute('''select * from tel_dir''')
s=c.fetchall()
pb=[]
for i in s:
   l=list(i)
   pb.append(l)
   
def add(pb):
   print("Please enter the following details : ")
   print(" ")
   list1=[]
   for j in range(5):
      if j==0:
         while True:
            cnf=input("Enter contact's FIRST name: ")
            cnl=input("Enter contact's LAST name: ")
            leaf=cnf+cnl
            if not leaf.isalpha():
               print('Invalid Entry!')
            else:
               break
         cname=cnf+' '+cnl
         name=cname.title()
         list1.append(name)
      if j==1:
         while True:
            number=input("Enter the ten-digit phone number : ")
            if not number.isnumeric():
               print('Please enter numerical value!')
            if len(number)!=10:
               print('The entered number does not contain 10 digits!')
            if number.isnumeric() and len(number)==10:
               number=int(number)
               c.execute('''select count(*) from tel_dir where phone_number={}'''.format(number))
               res=c.fetchall()
               if res>[(0,)]:
                  print('This phone number already exists in this directory')
               else:
                  break
         list1.append(number)            
      if j==2:
         while True:
            adr=input("Enter the address: ")
            if adr=='' or adr==' ':
               print('Please fill address field.')
            else:
               break             
         list1.append(adr)
      if j==3:
         while True:
            city=input("Enter City Name: ")
            if not city.isalpha():
               print('Invalid Entry.')
            else:
               break
         City=city.title()
         list1.append(City)
      if j==4:
         while True:
            pin=input("Enter six-digit pincode: ")
            if not pin.isnumeric():
               print('Invalid Entry!')
            elif len(pin)!=6:
               print('Pincode must contain 6 digits!')
            else:
               break
         pincode=int(pin)
         list1.append(pincode)
   pb.append(list1)
   rec=tuple(list1)
   s.append(rec)
   print(rec,'is added to PHONEBOOK')
   s1="insert into tel_dir values('{}',{},'{}','{}',{})".format(name,number,adr,City,pincode)
   c.execute(s1)
   return pb

def search():
   sch=input('Enter search criteria:\n\t\t\
      1) NAME\n\t\t\
      2) PHONE NUMBER\n\t\t\
      3) ADDRESS\n\t\t\
      4) CITY NAME\n\t\t\
      5) PINCODE\n\
      Please enter (1/2/3/4/5): ')
   sl=[]
   if sch=='1':
      sf=input('Please enter name of contact: ')
      sfn=sf.title()
      sql1=c.execute('''select count(*) from tel_dir where name like "%{}%"'''.format(sfn))
      sql2=c.fetchall()
      if sql2==[(0,)]:
         print('The contact does not exist in PHONEBOOK')
      if sql2>[(0,)]:
         c.execute('''select * from tel_dir where name like "%{}%"'''.format(sfn))
         chercher=from_db_cursor(c)
         print(chercher)
         
   elif sch=='2':
      while True:
         sf=input("Please enter the contact's number: ")
         if not sf.isnumeric():
            print('Please enter numerical value')
         elif len(sf)!=10:
            print('Please enter 10 digit number')
         else:
            break
      sfn=int(sf)
      sql1=c.execute('''select count(*) from tel_dir where phone_number={}'''.format(sfn))
      sql2=c.fetchall()
      if sql2==[(0,)]:
         print('The contact does not exist in PHONEBOOK')
      if sql2>[(0,)]:
         c.execute('''select * from tel_dir where phone_number={}'''.format(sfn))
         chercher=from_db_cursor(c)
         print(chercher)
         
   elif sch=='3':
      sf=str(input("Please enter the contact's Address: "))
      sfn=sf.title()
      sql1=c.execute('''select count(*) from tel_dir where address like "%{}%"'''.format(sfn))
      sql2=c.fetchall()
      if sql2==[(0,)]:
         print('The contact does not exist in PHONEBOOK')
      if sql2>[(0,)]:
         c.execute('''select * from tel_dir where address like "%{}%"'''.format(sfn))
         chercher=from_db_cursor(c)
         print(chercher)
         
   elif sch=='4':
      sf=input("Please enter the contact's City_Name: ")
      sfn=sf.title()
      sql1=c.execute('''select count(*) from tel_dir where City_Name like "%{}%"'''.format(sfn))
      sql2=c.fetchall()
      if sql2==[(0,)]:
         print('The contact does not exist in PHONEBOOK')
      if sql2>[(0,)]:
         c.execute('''select * from tel_dir where city_name like "%{}%"'''.format(sfn))
         chercher=from_db_cursor(c)
         print(chercher)
         
   elif sch=='5':
      while True:
         sf=input("Please enter the contact's pincode: ")
         if not sf.isnumeric():
            print('Please enter numerical value')
         elif len(sf)!=6:
            print('Please enter 6 digit pincode')
         else:
            break
      sfn=int(sf)
      sql1=c.execute('''select count(*) from tel_dir where pincode={}'''.format(sfn))
      sql2=c.fetchall()
      if sql2==[(0,)]:
         print('The contact does not exist in PHONEBOOK')
      if sql2>[(0,)]:
         c.execute('''select * from tel_dir where pincode={}'''.format(sfn))
         chercher=from_db_cursor(c)
         print(chercher)
   else:
      print('Invalid Entry!')
      


def delete(pb):
   sch=input('Enter search criteria for deleting contact:\n\t\t\
      1) NAME\n\t\t\
      2) PHONE NUMBER\n\t\t\
      3) CITY NAME\n\t\t\
      4) PINCODE\n\
      Please enter (1/2/3/4): ')
   sl=[]
   if sch=='1':
      sf=input('Please enter name of contact: ')
      sfn=sf.title()
      sql1=c.execute('''select count(*) from tel_dir where name like "%{}%"'''.format(sfn))
      sql2=c.fetchall()
      if sql2==[(0,)]:
         print('The contact does not exist in PHONEBOOK')
      else:
         c.execute('''select * from tel_dir where name like "%{}%"'''.format(sfn))
         chercher=from_db_cursor(c)
         print(chercher)
         if sql2==[(1,)]:
            c.execute('''select * from tel_dir where name like "%{}%"'''.format(sfn))
            delt=c.fetchall()
            for i in delt:
               elm=list(i)
            voice=input('To stop deletion of above contact, enter "Stop"')
            v=voice.lower()
            if v=='stop':
               print('DELETION STOPPED...')
            else:
               print('DELETION SUCCESSFUL...')
               c.execute('''delete from tel_dir where name like "%{}%"'''.format(sfn))
               pb.remove(elm)
         if sql2>[(1,)]:
            print('There seems to be more than one contact with that name...')
            fr=input('If you would like to delete all contacts with that name, enter "ALL" or press the <Enter> key: ')
            frr=fr.lower()
            if frr=='all':
               c.execute('''select * from tel_dir where name like "%{}%"'''.format(sfn))
               delt=c.fetchall()
               for i in delt:
                  elm=list(i)
                  pb.remove(elm)
               c.execute('''delete from tel_dir where name like "%{}%"'''.format(sfn))
               print('DELETION SUCCESSFUL...')
            else:
               while True:
                  num=input('Please enter Phone number of contact you wish to delete: ')
                  if not num.isnumeric():
                     print('Please enter numerical value')
                  elif len(num)!=10:
                     print('Please enter 10 digit number')
                  else:
                     numb=int(num)
                     sql1=c.execute('''select count(*) from tel_dir where phone_number={}'''.format(numb))
                     sql2=c.fetchall()
                     if sql2==[(0,)]:
                        print('The contact does not exist in PHONEBOOK')
                     else:
                        break
               c.execute('''select * from tel_dir where phone_number={}'''.format(numb))
               chercher=from_db_cursor(c)
               print(chercher)
               c.execute('''select * from tel_dir where phone_number={}'''.format(numb))
               delt=c.fetchall()
               for i in delt:
                  elm=list(i)
               voice=input('To stop deletion of above contact, enter "Stop"')
               v=voice.lower()
               if v=='stop':
                  print('DELETION STOPPED...')
               else:
                  print('DELETION SUCCESSFUL...')
                  c.execute('''delete from tel_dir where phone_number={}'''.format(numb))
                  pb.remove(elm)

   elif sch=='2':
      sf=input("Please enter the contact's number: ")
      if not sf.isnumeric():
         print('Please enter numerical value')
      elif len(sf)!=10:
         print('Please enter 10 digit number')
      else:
         sfn=int(sf)
         sql1=c.execute('''select count(*) from tel_dir where phone_number={}'''.format(sfn))
         sql2=c.fetchall()
         if sql2==[(0,)]:
            print('The contact does not exist in PHONEBOOK')
         else:
            c.execute('''select * from tel_dir where phone_number={}'''.format(sfn))
            chercher=from_db_cursor(c)
            print(chercher)
            c.execute('''select * from tel_dir where phone_number={}'''.format(sfn))
            delt=c.fetchall()
            for i in delt:
               elm=list(i)
            voice=input('To stop deletion of above contact, enter "Stop"')
            v=voice.lower()
            if v=='stop':
               print('DELETION STOPPED...')
            else:
               print('DELETION SUCCESSFUL...')
               c.execute('''delete from tel_dir where phone_number={}'''.format(sfn))
               pb.remove(elm)
         
   elif sch=='3':
      sf=input("Please enter the contact's City_Name: ")
      sfn=sf.title()
      sql1=c.execute('''select count(*) from tel_dir where City_Name like "%{}%"'''.format(sfn))
      sql2=c.fetchall()
      if sql2==[(0,)]:
         print('The contact does not exist in PHONEBOOK')
      else:
         c.execute('''select * from tel_dir where city_name like "%{}%"'''.format(sfn))
         chercher=from_db_cursor(c)
         print(chercher)
         if sql2==[(1,)]:
            c.execute('''select * from tel_dir where city_name like "%{}%"'''.format(sfn))
            delt=c.fetchall()
            for i in delt:
               elm=list(i)
            voice=input('To stop deletion of above contact, enter "Stop"')
            v=voice.lower()
            if v=='stop':
               print('DELETION STOPPED...')
            else:
               print('DELETION SUCCESSFUL...')
               c.execute('''delete from tel_dir where city_name like "%{}%"'''.format(sfn))
               pb.remove(elm)
         if sql2>[(1,)]:
            print('There seems to be more than one contact with that City_Name...')
            fr=input('If you would like to delete all contacts with that City_Name, enter "ALL" or press the <Enter> key: ')
            frr=fr.lower()
            if frr=='all':
               c.execute('''select * from tel_dir where city_name like "%{}%"'''.format(sfn))
               delt=c.fetchall()
               for i in delt:
                  elm=list(i)
                  pb.remove(elm)
               c.execute('''delete from tel_dir where city_name like "%{}%"'''.format(sfn))
               print('DELETION SUCCESSFUL...')
            else:
               while True:
                  num=input('Please enter Phone number of contact you wish to delete: ')
                  if not num.isnumeric():
                     print('Please enter numerical value')
                  elif len(num)!=10:
                     print('Please enter 10 digit number')
                  else:
                     numb=int(num)
                     sql1=c.execute('''select count(*) from tel_dir where phone_number={}'''.format(numb))
                     sql2=c.fetchall()
                     if sql2==[(0,)]:
                        print('The contact does not exist in PHONEBOOK')
                     else:
                        break
               c.execute('''select * from tel_dir where phone_number={}'''.format(numb))
               chercher=from_db_cursor(c)
               print(chercher)
               c.execute('''select * from tel_dir where phone_number={}'''.format(numb))
               delt=c.fetchall()
               for i in delt:
                  elm=list(i)
               voice=input('To stop deletion of above contact, enter "Stop"')
               v=voice.lower()
               if v=='stop':
                  print('DELETION STOPPED...')
               else:
                  print('DELETION SUCCESSFUL...')
                  c.execute('''delete from tel_dir where phone_number={}'''.format(numb))
                  pb.remove(elm)
               
   elif sch=='4':
      sf=input("Please enter the contact's pincode: ")
      if not sf.isnumeric():
         print('Please enter numerical value')
      elif len(sf)!=6:
         print('Please enter 6 digit pincode')
      else:
         sfn=int(sf)
         sql1=c.execute('''select count(*) from tel_dir where pincode={}'''.format(sfn))
         sql2=c.fetchall()
         if sql2==[(0,)]:
            print('The contact does not exist in PHONEBOOK')
         else:
            c.execute('''select * from tel_dir where pincode={}'''.format(sfn))
            chercher=from_db_cursor(c)
            print(chercher)
            if sql2==[(1,)]:
               c.execute('''select * from tel_dir where pincode={}'''.format(sfn))
               delt=c.fetchall()
               for i in delt:
                  elm=list(i)
               voice=input('To stop deletion of above contact, enter "Stop"')
               v=voice.lower()
               if v=='stop':
                  print('DELETION STOPPED...')
               else:
                  print('DELETION SUCCESSFUL...')
                  c.execute('''delete from tel_dir where pincode={}'''.format(sfn))
                  pb.remove(elm)
            if sql2>[(1,)]:
               print('There seems to be more than one contact with that pincode...')
               fr=input('If you would like to delete all contacts with that pincode, enter "ALL" or press the <Enter> key: ')
               frr=fr.lower()
               if frr=='all':
                  c.execute('''select * from tel_dir where pincode={}'''.format(sfn))
                  delt=c.fetchall()
                  for i in delt:
                     elm=list(i)
                     pb.remove(elm)
                  c.execute('''delete from tel_dir where pincode={}'''.format(sfn))
                  print('DELETION SUCCESSFUL...')
               else:
                  while True:
                     num=input('Please enter Phone number of contact you wish to delete: ')
                     if not num.isnumeric():
                        print('Please enter numerical value')
                     elif len(num)!=10:
                        print('Please enter 10 digit number')
                     else:
                        numb=int(num)
                        sql1=c.execute('''select count(*) from tel_dir where phone_number={}'''.format(numb))
                        sql2=c.fetchall()
                        if sql2==[(0,)]:
                           print('The contact does not exist in PHONEBOOK')
                        else:
                           break
                  c.execute('''select * from tel_dir where phone_number={}'''.format(numb))
                  chercher=from_db_cursor(c)
                  print(chercher)
                  c.execute('''select * from tel_dir where phone_number={}'''.format(numb))
                  delt=c.fetchall()
                  for i in delt:
                     elm=list(i)
                  voice=input('To stop deletion of above contact, enter "Stop"')
                  v=voice.lower()
                  if v=='stop':
                     print('DELETION STOPPED...')
                  else:
                     print('DELETION SUCCESSFUL...')
                     c.execute('''delete from tel_dir where phone_number={}'''.format(numb))
                     pb.remove(elm)
   else:
      print('Invalid Entry!')
   return pb

def edit(pb):
   print('Enter Name and Phone Number of Contact you wish to edit: ')
   sf=input('Please enter name of contact: ')
   sfn=sf.title()
   while True:
      sfe=input("Please enter the contact's number: ")
      if not sfe.isnumeric():
         print('Please enter numerical value')
      elif len(sfe)!=10:
         print('Please enter 10 digit number')
      else:
         break
   num=int(sfe)
   sql1=c.execute('''select count(*) from tel_dir where phone_number={} and name like "%{}%"'''.format(num,sfn))
   sql2=c.fetchall()
   if sql2==[(0,)]:
      print('The contact does not exist in PHONEBOOK')
   else:
      c.execute('''select * from tel_dir where phone_number={} and name like "%{}%"'''.format(num,sfn))
      chercher=from_db_cursor(c)
      print(chercher)
      c.execute('''select * from tel_dir where phone_number={} and name like "%{}%"'''.format(num,sfn))
      edit=c.fetchall()
      for i in edit:
         elm=list(i)
      q=input('What would you like to edit?\n\t\t\
      1) NAME\n\t\t\
      2) PHONE NUMBER\n\t\t\
      3) ADDRESS\n\t\t\
      4) CITY NAME\n\t\t\
      5) PINCODE\n\
      Please enter (1/2/3/4/5): ')
      if q=='1':
         while True:
            cnf=input("Enter contact's FIRST name: ")
            cnl=input("Enter contact's LAST name: ")
            leaf=cnf+cnl
            if not leaf.isalpha():
               print('Invalid Entry!')
            else:
               break
         cname=cnf+' '+cnl
         name=cname.title()
         c.execute('''update tel_dir set name='{}' where name like "%{}%" and phone_number={}'''.format(name,sfn,num))
         for i in pb:
            if elm==i:
               i[0]=name
      if q=='2':
         while True:
            number=input("Enter the ten-digit phone number : ")
            if not number.isnumeric():
               print('Please enter numerical value!')
            if len(number)!=10:
               print('The entered number does not contain 10 digits!')
            if number.isnumeric() and len(number)==10:
               number=int(number)
               c.execute('''select count(*) from tel_dir where phone_number={}'''.format(number))
               res=c.fetchall()
               if res>[(0,)]:
                  print('This phone number already exists in this directory')
               else:
                  break
         c.execute('''update tel_dir set phone_number={} where name like "%{}%" and phone_number={}'''.format(number,sfn,num))
         for i in pb:
            if elm==i:
               i[1]=number            
      if q=='3':
         while True:
            adr=input("Enter the address: ")
            if adr=='' or adr==' ':
               print('Please fill address field.')
            else:
               break
         c.execute('''update tel_dir set address='{}' where name like "%{}%" and phone_number={}'''.format(adr,sfn,num))
         for i in pb:
            if elm==i:
               i[2]=adr
      if q=='4':
         while True:
            city=input("Enter City Name: ")
            if not city.isalpha():
               print('Invalid Entry.')
            else:
               City=city.title()
               break
         c.execute('''update tel_dir set city_name='{}' where name like "%{}%" and phone_number={}'''.format(City,sfn,num))
         for i in pb:
            if elm==i:
               i[3]=City
      if q=='5':
         while True:
            pin=input("Enter six-digit pincode: ")
            if not pin.isnumeric():
               print('Invalid Entry!')
            elif len(pin)!=6:
               print('Pincode must contain 6 digits!')
            else:
               break
         pincode=int(pin)
         c.execute('''update tel_dir set pincode={} where name like "%{}%" and phone_number={}'''.format(pincode,sfn,num))
         for i in pb:
            if elm==i:
               i[4]=pincode
   return pb
         
def exit_pb():
   print('\t\t\t\t\t\tThank you for using PHONEBOOK')
   print('')
   print('\t\t\t\t\t\tEXITING...')

def login_admin():
   print()
   c.execute('''select * from tel_dir order by name''')
   tab=from_db_cursor(c)
   print(tab)
   print()
   print('What would you like to do?\n\t\t\t\
   1) ADD A NEW CONTACT\n\t\t\t\
   2) EDIT AN EXISITING CONTACT\n\t\t\t\
   3) SEARCH FOR A CONTACT\n\t\t\t\
   4) DELETE A CONTACT\n\t\t\t\
   5) EXIT PHONEBOOK')
   choice=input('Please enter choice (1/2/3/4):\t')
   return choice

def login_user():
   print()
   c.execute('''select * from tel_dir order by name''')
   tab=from_db_cursor(c)
   print(tab)
   print()
   print('What would you like to do?\n\t\t\t\
   1) SEARCH FOR A CONTACT\n\t\t\t\
   2) GIVE FEEDBACK\n\t\t\t\
   3) EXIT PHONEBOOK')
   choice=input('Please enter choice (1/2/3):\t')
   return choice

elf=1
if user=='ADMIN':
   while elf in range(100):
      ch = login_admin()
      c.execute('''select * from tel_dir''')
      s=c.fetchall()
      pb=[]
      for i in s:
         l=list(i)
         pb.append(l)
      if ch == '1':
         pb = add(pb)
      elif ch == '2':
         pb = edit(pb)
      elif ch == '3':
         h = search()
      elif ch == '4':
         pb = delete(pb)
      elif ch == '5':
         pb = exit_pb()
         break
      else:
         print('Invalid Choice')
if user=='USER':
   while elf in range(100):
      ch = login_user()
      c.execute('''select * from tel_dir''')
      s=c.fetchall()
      pb=[]
      for i in s:
         l=list(i)
         pb.append(l)
      if ch == '1':
         h = search()
      elif ch == '2':
         print()
         print('For any queries or feedback, please contact:-\n\t\t\
         Phone number: 1231231231\n\t\t\
         EmailId: abc@gmail.com')
         print()
      elif ch == '3':
         pb = exit_pb()
         break
      else:
         print('Invalid Choice')

mc.commit()
mc.close()
