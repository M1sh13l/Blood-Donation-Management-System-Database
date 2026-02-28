import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "M1sh13l",
    password = "M@sh13l_26q",
    database = "BDMS")

mycursor = mydb.cursor()

def menu():
  print("\n\nPlease select a task to do:")
  print("1- Add a donor member")
  print("2- Add a Recipient member")
  print("3- Add a phlebotomist member")
  print("4- Add a staff member")
  print("5- Add the blood test for the donor")
  print("6- Add a Blood donation Center")
  print("7- Add the Blood donation of the donor")
  print("8- Add the Blood condition of the donor")
  print("9- Add the health condition of the donor")
  print("10- Add the medical history of the donor")
  print("11- Register an appointment")
  print("12- The relation between the recipient and donor")
  print("13- Track the donor's progress")
  print("14- Show all donors")
  print("15- Show all recipient")
  print("16- Show all phlebotomist")
  print("17- Show all staff members")
  print("18- Show all blood tests")
  print("19- Show all Blood Donation Centers")
  print("20- Show all blood donations")
  print("21- Show all blood conditions")
  print("22- Show all health conditions")
  print("23- Show all medical histories")
  print("24- Show all registered appointments")
  print("25- Remove a donor")
  print("26- Remove a recipient")
  print("27- Remove a phlebotomist")
  print("28- Remove a staff member")
  print("29- Remove a Blood Donation Center")
  print("30- Search for a donor")
  print("31- Search for a recipient")
  print("32- Search for a phlebotomist")
  print("33- Search for a staff member")
  print("34- Search for a Blood Donation Center")
  print("35- Donors' Blood Type report")
  print("36- Phlebotomist collection report")
  print("37- Exit")

def addDonor():
  print("Please enter the new donor details below")
  dID = input("Donor's ID: ")
  dfname = input("First Name: ")
  dlname = input("Last Name: ")
  dgender = input("Gender (F/M): ")
  dDOB = input("Date of birth (YYYY-MM-DD): ")
  dBloodType = input("Blood Type: ")
  dAddress = input("Address: ")
  dPhoneNumber = input("Phone Number: ")
  dEmail = input("Email: ")
  dDonationHistory = input("Donation History(if they have): ")
  sqlInsert = "INSERT INTO donor VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  val = (dID, dfname, dlname, dDOB, dgender, dBloodType, dAddress, dPhoneNumber, dEmail, dDonationHistory)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The donor has been added successfully!!")

def addRecipient():
  print("Please enter the new recipient details below")
  rID = input("Recipient ID: ")
  rfname = input("First Name: ")
  rlname = input("Last Name: ")
  rgender = input("Gender: ")
  rDOB = input("Date of birth (YYYY-MM-DD): ")
  rAddress = input("Address: ")
  rPhoneNumber = input("Phone Number: ")
  rEmail = input("Email: ")
  sqlInsert = "INSERT INTO recipient VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
  val = (rID, rfname, rlname, rDOB, rgender, rAddress, rPhoneNumber, rEmail)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The recipient has been added successfully!!")

def addPhlebotomist():
  print("Please enter the new phlebotomist details below")
  pID = input("Phlebotomist ID: ")
  pfname = input("First Name: ")
  plname = input("Last Name: ")
  pgender = input("Gender: ")
  pDOB = input("Date of birth (YYYY-MM-DD): ")
  pAddress = input("Address: ")
  pPhoneNumber = input("Phone Number: ")
  pEmail = input("Email: ")
  pCID= input("Blood Donation Center ID: ")
  sqlInsert = "INSERT INTO phlebotomist VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  val = (pID, pfname, plname, pDOB, pgender, pAddress, pPhoneNumber, pEmail, pCID)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The phelbotomist has been added successfully!!")

def addStaff():
  print("Please enter the new staff member details below")
  sID = input("Staff ID: ")
  sname = input("Name: ")
  sDOB = input("Date of birth (YYYY-MM-DD): ")
  sAddress = input("Address: ")
  sPhoneNumber = input("Phone Number: ")
  sEmail = input("Email: ")
  sRole = input("Role/position: ")
  sCID = input("Blood Donation Center ID: ")
  sqlInsert = "INSERT INTO staff VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
  val = (sID, sname, sDOB, sAddress, sPhoneNumber, sEmail, sRole, sCID)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The staff has been added successfully!!")

def addBloodTest():
  print("Please enter the new Blood Test details below")
  TID = input("Blood Test ID: ")
  tname = input("Date of Blood test: ")
  tlocation = input("Blood Type: ")
  tDID = input("Donor's ID: ")
  sqlInsert = "INSERT INTO bloodtest VALUES(%s,%s,%s,%s)"
  val = (TID, tname, tlocation, tDID)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The Blood Test has been added successfully!!")

def addBlood_Donation_Center():
  print("Please enter the new Blood Donation Center details below")
  cID = input("Blood Donation Center ID: ")
  cname = input("Name of the Center: ")
  clocation = input("Center's location: ")
  cDID = input("Donor's ID: ")
  sqlInsert = "INSERT INTO blood_donation_center VALUES(%s,%s,%s,%s)"
  val = (cID, cname, clocation, cDID)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The Center has been added successfully!!")

def addBloodDonation():
  print("Please enter the new blood donation details below")
  donationID = input("Blood DonationcID: ")
  dstart_time = input("Start time of the donation: ")
  dend_time = input("End Time of the donation: ")
  ddate = input("Date of donation: ")
  dquantity = input("Blood quantity donated: ")
  dDID = input("Donor ID: ")
  dCID = input("Center ID: ")
  dTID = input("Test ID: ")
  sqlInsert = "INSERT INTO blooddonation VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
  val = (donationID, dstart_time, dend_time, ddate, dquantity, dDID, dCID, dTID)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The blood donation has been added successfully!!")

def addBloodConidition():
  print("Please enter the new Blood Condition details below")
  TID = input("Test ID: ")
  bloodCondition = input("Blood condition: ")
  sqlInsert = "INSERT INTO bloodcondition VALUES(%s,%s)"
  val = (TID, bloodCondition)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The blood condition has been added successfully!!")

def addhealthcondition():
  print("Please enter the new health condition details below")
  hDID = input("Donor ID: ")
  healthCondition = input("Health condition: ")
  sqlInsert = "INSERT INTO healthcondition VALUES(%s,%s)"
  val = (hDID, healthCondition)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The health condition has been added successfully!!")

def addmedicalhistory():
  print("Please enter the new medical histroy details below")
  mRID = input("Recipient ID: ")
  medicalhistory = input("Medical History for recipient: ")
  sqlInsert = "INSERT INTO medicalhistory VALUES(%s,%s)"
  val = (mRID, medicalhistory)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The health condition has been added successfully!!")

def addRegister_appointment():
  print("Please enter the new registeration details below")
  aSID = input("Staff member ID: ")
  aDID = input("Donor ID: ")
  appointment_Time = input("Appointment time: ")
  appointment_date= input("Appointment date (YYYY-MM-DD): ")
  sqlInsert = "INSERT INTO register_appointment VALUES(%s,%s,%s,%s)"
  val = (aSID, aDID, appointment_Time, appointment_date)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The Center has been added successfully!!")

def addRelation():
  print("Please enter the new relation details below")
  rRID = input("Recipient ID: ")
  rDID = input("Donor ID: ")
  type_of_relation = input("Type of relation: ")
  sqlInsert = "INSERT INTO related VALUES(%s,%s,%s)"
  val = (rRID, rDID, type_of_relation)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The Center has been added successfully!!")

def addTrack():
  print("Please enter the new relation details below")
  tPID = input("Phlebotomist ID: ")
  tTID = input("Test ID: ")
  tDID= input("Donor ID ")
  sqlInsert = "INSERT INTO track VALUES(%s,%s,%s)"
  val = (tPID, tTID, tDID)
  mycursor = mydb.cursor()
  mycursor.execute(sqlInsert, val)
  mydb.commit()
  print("The Center has been added successfully!!")

def allDonor():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM donor")
  myresult = mycursor.fetchall()
  print('Donor ID' + '\t\t' + 'First Name' + '\t\t' + 'Last Name' + '\t\t' + 'Gender' + '\t\t' + 'DOB' + '\t\t' + 'Blood Type' + '\t\t' + 'Address' + '\t\t'  + 'Phone Number' + '\t\t' + 'Email' + '\t\t' + 'Donation History')
  print('--------' + '\t\t' + '----------' + '\t\t' + '---------' + '\t\t' + '------' + '\t\t' + '----'+ '\t\t' + '----------' + '\t\t' + '--------' + '\t\t' + '------------' + '\t\t' + '------' + '\t\t' + '---------------')
  for x in myresult:
    x9 = x[9] if(x[9]) else 'Unknown'
    x9 = x[9] if(x[9]) else 'Unknown'
    print(x[0] + '\t\t' + x[1] + ' ' + x[2] + '\t\t' + x[3] +  ' ' + str(x[4]) + '\t\t' + x[5] + ' ' + x[6] + '\t\t' + x[7] + ' ' + x[8] + '\t\t' + str(x9))

def allrecipient():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM recipient")
  myresult = mycursor.fetchall()
  print('Recipient ID' + '\t\t' + 'First Name' + '\t\t' + 'Last Name' + '\t\t' + 'Gender' + '\t\t' + 'DOB' + '\t\t' + 'Address' + '\t\t'  + 'Phone Number' + '\t\t' + 'Email')
  print('------------' + '\t\t' + '----------' + '\t\t' + '---------' + '\t\t' + '------' + '\t\t' + '---'+ '\t\t' + '---------' + '\t\t' + '------------' + '\t\t' + '-----')
  for x in myresult:
    x7 = x[7] if(x[7]) else 'Unknown'
    x7 = x[7] if(x[7]) else 'Unknown'
    print(x[0] + '\t\t' + x[1] + ' ' + x[2] + '\t\t' + x[3] +  ' ' + str(x[4]) + '\t\t' + x[5] + ' ' + x[6] + '\t\t' + str(x7))

def allphlebotomist():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM phlebotomist")
  myresult = mycursor.fetchall()
  print('phlebotomist ID' + '\t\t' + 'First Name' + '\t\t' + 'Last Name' + '\t\t' + 'Gender' + '\t\t' + 'DOB' + '\t\t' + 'Address' + '\t\t'  + 'Phone Number' + '\t\t' + 'Email' + '\t\t' + 'pCID')
  print('---------------' + '\t\t' + '----------' + '\t\t' + '---------' + '\t\t' + '------' + '\t\t' + '---'+ '\t\t' + '---------' + '\t\t' + '------------' + '\t\t' + '-----' + '\t\t' + '-----')
  for x in myresult:
    x8 = x[8] if(x[8]) else 'Unknown'
    x8 = x[8] if(x[8]) else 'Unknown'
    print(x[0] + '\t\t' + x[1] + ' ' + x[2] + '\t\t' + x[3] +  ' ' + str(x[4]) + '\t\t' + x[5] + ' ' + x[6] + '\t\t' + x[7] + ' ' + str(x8))

def allstaff():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM staff")
  myresult = mycursor.fetchall()
  print('staff ID' + '\t\t' + 'Name' + '\t\t' + 'DOB' + '\t\t' + 'Address' + '\t\t'  + 'Phone Number' + '\t\t' + 'Email'  + '\t\t' + 'role'+ '\t\t' + 'sCID')
  print('--------' + '\t\t' + '----' + '\t\t' + '---' + '\t\t' + '--------'+ '\t\t' + '-------------' + '\t\t' + '------' + '\t\t' + '-----' + '\t\t' + '-----')
  for x in myresult:
    x7 = x[7] if(x[7]) else 'Unknown'
    x7 = x[7] if(x[7]) else 'Unknown'
    print(x[0] + '\t\t' + x[1] + ' ' + str(x[2]) + '\t\t' + x[3] +  ' ' + x[4] + '\t\t' + x[5] + ' ' + x[6] + '\t\t' + str(x7))

def allbloodTests():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM bloodtest")
  myresult = mycursor.fetchall()
  print('Test ID' + '\t\t' + 'Date' + '\t\t' + 'Blood Type' + '\t\t' + 'bDID')
  print('-------' + '\t\t' + '----' + '\t\t' + '----------' + '\t\t' + '----')
  for x in myresult:
    x3 = x[3] if(x[3]) else 'Unknown'
    x3 = x[3] if(x[3]) else 'Unknown'
    print(x[0] + '\t\t' + str(x[1]) + ' ' + x[2] + '\t\t' + x[3])

def allBloodDonationCenters():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM blood_donation_center")
  myresult = mycursor.fetchall()
  print('Center ID' + '\t\t' + 'Center Name' + '\t\t' + 'Location' + '\t\t' + 'cDID')
  print('---------' + '\t\t' + '-----------' + '\t\t' + '--------' + '\t\t' + '----')
  for x in myresult:
    x3 = x[3] if(x[3]) else 'Unknown'
    x3 = x[3] if(x[3]) else 'Unknown'
    print(x[0] + '\t\t' + str(x[1]) + ' ' + x[2] + '\t\t' + x[3])

def allBloodDonations():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM blooddonation")
  myresult = mycursor.fetchall()
  print('Donation ID' + '\t\t' + 'Start Time' + '\t\t' + 'End Time' + '\t\t' + 'Qunatity Blood' + '\t\t'  + 'Date' + '\t\t' + 'bDID'  + '\t\t' + 'bCID' + '\t\t' + 'bTID')
  print('-----------' + '\t\t' + '----------' + '\t\t' + '--------' + '\t\t' + '---------------' + '\t\t' + '----' + '\t\t' + '-----' + '\t\t' + '----' + '\t\t' + '-----')
  for x in myresult:
    x7 = x[7] if(x[7]) else 'Unknown'
    x7 = x[7] if(x[7]) else 'Unknown'
    print(x[0] + '\t\t' + x[1] + ' ' + x[2] + '\t\t' + str(x[3]) +  ' ' + str(x[4]) + '\t\t' + x[5] + ' ' + x[6] + '\t\t' + str(x7))

def allBloodConditions():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM bloodcondition")
  myresult = mycursor.fetchall()
  print('TID' + '\t\t' + 'Blood Condition')
  print('------' + '\t\t' + '-------------')
  for x in myresult:
    x1 = x[1] if(x[1]) else 'Unknown'
    x1 = x[1] if(x[1]) else 'Unknown'
    print(x[0] + '\t\t' + x[1])

def allHealthConditions():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM healthcondition")
  myresult = mycursor.fetchall()
  print('DID' + '\t\t' + 'Health Condition')
  print('------' + '\t\t' + '-------------')
  for x in myresult:
    x1 = x[1] if(x[1]) else 'Unknown'
    x1 = x[1] if(x[1]) else 'Unknown'
    print(x[0] + '\t\t' + x[1]+ ' ')

def allMedicalHistories():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM medicalhistory")
  myresult = mycursor.fetchall()
  print('RID' + '\t\t' + 'Medical History')
  print('------' + '\t\t' + '-------------')
  for x in myresult:
    x1 = x[1] if(x[1]) else 'Unknown'
    x1 = x[1] if(x[1]) else 'Unknown'
    print(x[0] + '\t\t' + x[1]+ ' ')

def allRegisterations():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM register_appointment")
  myresult = mycursor.fetchall()
  print('rSID' + '\t\t' + 'rDID' + '\t\t' + 'Appointment Time' + '\t\t' + 'Appointment Date')
  print('----' + '\t\t' + '----' + '\t\t' + '----------------' + '\t\t' + '----------------')
  for x in myresult:
    x3 = x[3] if(x[3]) else 'Unknown'
    x3 = x[3] if(x[3]) else 'Unknown'
    print(x[0] + '\t\t' + str(x[1]) + ' ' + x[2] + '\t\t' + x[3])

def delDonor():
  did = input("Please enter the Donor ID: ")
  sqlsearch = "SELECT * FROM donor WHERE DonorID = \'" + did + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no donor with this ID.")
  else:
    sqldelete = "DELETE FROM donor WHERE DonorID = \'" + did + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("The donor has been deleted successfully!!")

def delrecipient():
  rid = input("Please enter the Recipient ID: ")
  sqlsearch = "SELECT * FROM recipient WHERE recipientID = \'" + rid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no recipient with this ID.")
  else:
    sqldelete = "DELETE FROM recipient WHERE recipientID = \'" + rid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("The recipient has been deleted successfully!!")

def delphlebotomist():
  pid = input("Please enter the phlebotomist ID: ")
  sqlsearch = "SELECT * FROM phlebotomist WHERE phlebotomistID = \'" + pid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no phlebotomist with this ID.")
  else:
    sqldelete = "DELETE FROM phlebotomist WHERE phlebotomistID = \'" + pid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("The phlebotomist has been deleted successfully!!")

def delstaffMemeber():
  did = input("Please enter the staff ID: ")
  sqlsearch = "SELECT * FROM staff WHERE staffID = \'" + did + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no staff member with this ID.")
  else:
    sqldelete = "DELETE FROM staff WHERE staffID = \'" + did + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("The staff has been deleted successfully!!")

def delBlood_Donation_Center():
  bid = input("Please enter the Blood Donation Center ID: ")
  sqlsearch = "SELECT * FROM blood_donation_center WHERE CenterID = \'" + bid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no Center with this ID.")
  else:
    sqldelete = "DELETE FROM blood_donation_center WHERE CenterID = \'" + bid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("The blood donation center has been deleted successfully!!")

def finddonor():
  did = input("Please enter the donor ID: ")
  sqlsearch = "SELECT * FROM donor WHERE donorID = \'" + did + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no donor with this ID.")
  else:
    print("The details of the donor are: ")
    print("Donor ID: " + myresult[0])
    print("First Name: " + myresult[1])
    print("Last Name: " + myresult[2])
    print("Gender: " + myresult[3])
    print("Date of Birth: " + str(myresult[4]))
    print("Blood Type: " + myresult[5])
    print("Address: " + myresult[6])
    print("Phone Number: " + myresult[7])
    print("Email: " + myresult[8])
    print("Donation History: " + myresult[9])

def findrecipient():
  rid = input("Please enter the Recipient ID: ")
  sqlsearch = "SELECT * FROM recipient WHERE RecipientID = \'" + rid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no recipient with this ID.")
  else:
    print("The details of the recipient are: ")
    print("Recipient ID: " + myresult[0])
    print("First Name: " + myresult[1])
    print("Last Name: " + myresult[2])
    print("Gender: " + myresult[3])
    print("Date of Birth: " + str(myresult[4]))
    print("Address: " + myresult[5])
    print("Phone Number: " + myresult[6])
    print("Email: " + myresult[7])

def findphlebotomist():
  pid = input("Please enter the Phlebotomist ID: ")
  sqlsearch = "SELECT * FROM phlebotomist WHERE phlebotomistID = \'" + pid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no phlebotomist with this ID.")
  else:
    print("The details of the phlebotomist are: ")
    print("Phlebotomist ID: " + myresult[0])
    print("First Name: " + myresult[1])
    print("Last Name: " + myresult[2])
    print("Gender: " + myresult[3])
    print("Date of Birth: " + str(myresult[4]))
    print("Address: " + myresult[5])
    print("Phone Number: " + myresult[6])
    print("Email: " + myresult[7])
    print("Center ID: " + myresult[8])

def findstaff():
  sid = input("Please enter the staff ID: ")
  sqlsearch = "SELECT * FROM staff WHERE staffID = \'" + sid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no staff with this ID.")
  else:
    print("The details of the staff are: ")
    print("Staff ID: " + myresult[0])
    print("Name: " + myresult[1])
    print("Date of Birth: " + str(myresult[2]))
    print("Address: " + myresult[3])
    print("Phone Number: " + myresult[4])
    print("Email: " + myresult[5])
    print("Role: " + myresult[6])
    print("Center ID: " + myresult[7])

def findCenter():
  cid = input("Please enter the Center ID: ")
  sqlsearch = "SELECT * FROM Blood_donation_Center WHERE centerID = \'" + cid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Center with this ID.")
  else:
    print("The details of the Center are: ")
    print("Center ID: " + myresult[0])
    print("Center Name: " + myresult[1])
    print("Location: " + myresult[2])
    print("Donor ID: " + myresult[3])

def CenterReport():
  cid = input("Please enter the Center ID: ")
  sqlsearch = "SELECT * FROM blood_donation_center WHERE CenterID = \'" + cid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Center with this ID.")
  else:
    print("The blood  types donated in " + myresult[1] + "," + myresult[2] + " did so far are: ")
    sqlsearch = "SELECT donor.fname, donor.lname, blood_donation_center.cname, blood_donation_center.location, donor.bloodtype, blooddonation.quantityblood FROM blooddonation JOIN donor ON blooddonation.DID = donor.donorid JOIN blood_donation_center ON blooddonation.CID = blood_donation_center.CenterID WHERE CenterID = \'" + cid + "\'"
    mycursor.execute(sqlsearch)
    myresult = mycursor.fetchall()
    print('First Name' + '\t\t' + 'Last Name' + '\t\t' + 'Center Name' + '\t\t' + 'Location' + '\t\t' + 'Blood Type' + '\t\t' + 'Quantity of blood')
    print('----------' + '\t\t' + '---------' + '\t\t' + '-----------' + '\t\t' + '--------' + '\t\t' + '----------' + '\t\t' + '-----------------')
    for x in myresult:
      print(x[0] + '\t\t' + x[1] + ' ' + x[2] + '\t\t' + x[3] +  ' ' + x[4] + '\t\t' + str(x[5]))

def PhlebotomistReport():
  pid = input("Please enter the Phlbotomist ID: ")
  sqlsearch = "SELECT * FROM phlebotomist WHERE phlebotomistID = \'" + pid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Center with this ID.")
  else:
    print("The phlebotomist: " + myresult[1] + "," + myresult[2] + " collect so far : ")
    sqlsearch = "SELECT phlebotomist.fname, phlebotomist.lname, blood_donation_center.cname, blood_donation_center.location, donor.bloodtype, blooddonation.date FROM blooddonation JOIN donor ON blooddonation.DID = donor.donorid JOIN blood_donation_center ON blooddonation.CID = blood_donation_center.CenterID JOIN phlebotomist ON phlebotomist.CID = blood_donation_center.CenterID WHERE phlebotomistID = \'" + pid + "\'"
    mycursor.execute(sqlsearch)
    myresult = mycursor.fetchall()
    print('First Name' + '\t\t' + 'Last Name' + '\t\t' + 'Center Name' + '\t\t' + 'Location' + '\t\t' + 'Blood Type' + '\t\t' + 'Date of Donation')
    print('----------' + '\t\t' + '---------' + '\t\t' + '-----------' + '\t\t' + '--------' + '\t\t' + '----------' + '\t\t' + '----------------')
    for x in myresult:
      print(x[0] + '\t\t' + x[1] + ' ' + x[2] + '\t\t' + x[3] +  ' ' + x[4] + '\t\t' + str(x[5]))

def main():
  key = '0'
  print("\t\t\t Welcome to the Blood Donation Management System!")
  while key != '37':
    menu()
    key = input("Choose: ")
    
    if key == '1':
      addDonor()
    elif key == '2':
      addRecipient()
    elif key == '3':
      addPhlebotomist()
    elif key == '4':
      addStaff()
    elif key == '5':
      addBloodTest()
    elif key == '6':
      addBlood_Donation_Center()
    elif key == '7':
      addBloodDonation()
    elif key == '8':
      addBloodConidition()
    elif key == '9':
      addhealthcondition()
    elif key == '10':
      addmedicalhistory()
    elif key == '11':
      addRegister_appointment()
    elif key == '12':
      addRelation()
    elif key == '13':
      addTrack()
    elif key == '14':
      allDonor()
    elif key == '15':
      allrecipient()
    elif key == '16':
      allphlebotomist()
    elif key == '17':
      allstaff()
    elif key == '18':
      allbloodTests()
    elif key == '19':
      allBloodDonationCenters()
    elif key == '20':
      allBloodDonations()
    elif key == '21':
      allBloodConditions()
    elif key == '22':
      allHealthConditions()
    elif key == '23':
      allMedicalHistories()
    elif key == '24':
      allRegisterations()
    elif key == '25':
      delDonor()
    elif key == '26':
      delrecipient()
    elif key == '27':
      delphlebotomist()
    elif key == '28':
      delstaffMemeber()
    elif key == '29':
      delBlood_Donation_Center()
    elif key == '30':
      finddonor()
    elif key == '31':
      findrecipient()
    elif key == '32':
      findphlebotomist()
    elif key == '33':
      findstaff()
    elif key == '34':
      findCenter()
    elif key == '35':
      CenterReport()
    elif key =='36':
      PhlebotomistReport()
    elif key == '37':
      {
      print("\n\nThank you for using our system. Bye!"),
      exit()
      }
    else:
      print("Select a number from 0 to 37")

main()
