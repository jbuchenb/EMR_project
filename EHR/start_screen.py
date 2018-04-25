from tkinter import *
from tkinter import messagebox
from datetime import datetime 
# import new_patient
# import search_patient
from database import check_SSN_dont_exist_database, add_patient, obtain_patient_info, update_info_db


#########
# Style var
#########
back_color = "white"
font_color = "grey"
grey_color = "#e5e5e5"

#########
# Screen var
#########
start_screen = 0
msg_newPatient_screen = 0
msg_updatedPatientInfo_screen = 0
new_patient_screen = 0
search_patient_screen = 0
patient_home_screen = 0
edit_patient_info_screen = 0

#########
# Inputs var
#########
firstName_usr = 0
lastName_usr = 0
SSN_usr = 0
DOB_usr = 0
city_usr = 0

# This variable only stores integers
searched_patient_SSN = 0



########################
# Screen generators
########################

def create_start_screen():
	global start_screen, new_patient_screen
	# This block new patient screen
	#new_patient_screen = 0
	#new_patient_screen.destroy()
	start_screen = Tk()
	start_screen.title("EHR")
	start_screen.geometry("600x200")


	txt_1 = Label(start_screen, text="Please choose one of the following options:", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0)

	txt_1 = Label(start_screen, text="    ", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=2, column=0)

	#######
	# Buttons
	#######
	button_print = Button(start_screen, fg=font_color, text="Create new patient", 
		command=closeStart_open_newPatient, width=16, height=2).grid(row=3, column=0)
	button_print = Button(start_screen, fg=font_color, text="Search patient", 
		command=closeStart_open_SearchPatient, width=12, height=2).grid(row=3, column=1)

	start_screen.mainloop()



def create_msg_newPatient_created_scree(patient_info):
	global msg_newPatient_screen, new_patient_screen
	new_patient_screen.destroy()
	msg_newPatient_screen = Tk()
	msg_newPatient_screen.geometry("400x180")
	msg_newPatient_screen.title("Patient created")
	message = ("Patient created with the following information:\n" + " ".join(patient_info) +
	 "\n\nDo you want to create another patient?")
	Label(msg_newPatient_screen, text=message, fg=font_color, 
						font=("Helvetica", 14),
						bg=back_color).grid(row=1, column=0)

	Label(msg_newPatient_screen, text="", fg=font_color, 
						font=("Helvetica", 14),
						bg=back_color).grid(row=2, column=0)
	Button(msg_newPatient_screen,text="Yes", command=closeMessage_open_newPatient,fg=font_color, width=8, height=2).grid(row=3, column=0)
	Button(msg_newPatient_screen,text="No", command=closeMessage_open_startScreen,
		fg=font_color, width=8, height=2).grid(row=3, column=1)

	msg_newPatient_screen.mainloop()



def create_msg_Patient_updated_screen(patient_info):
	global msg_updatedPatientInfo_screen, edit_patient_info_screen
	edit_patient_info_screen.destroy()
	msg_updatedPatientInfo_screen = Tk()
	msg_updatedPatientInfo_screen.geometry("400x180")
	msg_updatedPatientInfo_screen.title("Patient created")
	message = ("Patient's data updated with the following information:\n" + " ".join(patient_info))
	Label(msg_updatedPatientInfo_screen, text=message, fg=font_color, 
						font=("Helvetica", 14),
						bg=back_color).grid(row=1, column=0)

	Label(msg_updatedPatientInfo_screen, text="", fg=font_color, 
						font=("Helvetica", 14),
						bg=back_color).grid(row=2, column=0)
	Button(msg_updatedPatientInfo_screen,text="Ok", command=closeMessageUpdate_open_patientHome,fg=font_color, width=8, height=2).grid(row=3, column=0)

	msg_updatedPatientInfo_screen.mainloop()




def create_new_patient_screen():
	global new_patient_screen, start_screen, msg_newPatient_screen


	new_patient_screen = Tk()
	new_patient_screen.title("New patient")
	new_patient_screen.geometry("600x300")

	global firstName_usr, lastName_usr, SSN_usr, DOB_usr, city_usr

	# This fix when multiple windows are openend
	# firstName_usr = StringVar(new_patient_screen)
	# lastName_usr = StringVar(new_patient_screen)
	# SSN_usr = StringVar(new_patient_screen)
	# DOB_usr = StringVar(new_patient_screen)
	# city_usr = StringVar(new_patient_screen)
	firstName_usr = StringVar()
	lastName_usr = StringVar()
	SSN_usr = StringVar()
	DOB_usr = StringVar()
	city_usr = StringVar()


	txt_1 = Label(new_patient_screen, text="Please input patient's information", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0)


	txt_1_3 = Label(new_patient_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=2, column=0)

	txt_firstName = Label(new_patient_screen, text="First name:", bg=back_color, fg=font_color).grid(row=3, column=0)
	input_firstName = Entry(new_patient_screen, textvariable=firstName_usr, highlightbackground=back_color).grid(row=3, column=1) 

	txt_lastName = Label(new_patient_screen, text="Last name:", bg=back_color, fg=font_color).grid(row=4, column=0)
	input_lastName = Entry(new_patient_screen, textvariable=lastName_usr, highlightbackground=back_color).grid(row=4, column=1) 

	txt_SSN = Label(new_patient_screen, text="SSN:", bg=back_color, fg=font_color).grid(row=5, column=0)
	input_SSN = Entry(new_patient_screen, textvariable=SSN_usr, highlightbackground=back_color).grid(row=5, column=1) 

	txt_DOB = Label(new_patient_screen, text="Date of birth (2012-5-21):", bg=back_color, fg=font_color).grid(row=6, column=0)
	input_DOB = Entry(new_patient_screen, textvariable=DOB_usr, highlightbackground=back_color).grid(row=6, column=1) 

	txt_city = Label(new_patient_screen, text="City:", bg=back_color, fg=font_color).grid(row=7, column=0)
	input_city = Entry(new_patient_screen, textvariable=city_usr, highlightbackground=back_color).grid(row=7, column=1) 

	txt_1_3 = Label(new_patient_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=8, column=0)

	#######
	# Buttons
	#######
	button_print = Button(new_patient_screen, fg=font_color, text="Create patient", command=create_new_patient, width=12, height=2).grid(row=9, column=0)
	button_print = Button(new_patient_screen, fg=font_color, text="Cancel", command=closeNewPatient_open_start, width=12, height=2).grid(row=9, column=1)

	# Export to global enviroment
	# global firstName_usr, lastName_usr, SSN_usr, DOB_usr, city_usr

	new_patient_screen.mainloop()





def create_searchPatient_screen():
	global search_patient_screen
	search_patient_screen = Tk()
	search_patient_screen.title("Search patient")
	search_patient_screen.geometry("600x300")
	
	global SSN_usr

	SSN_usr = StringVar()

	txt_1 = Label(search_patient_screen, text="Please input patient's SSN to search", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0)


	txt_1_3 = Label(search_patient_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=2, column=0)


	txt_SSN = Label(search_patient_screen, text="SSN:", bg=back_color, fg=font_color).grid(row=3, column=0)
	input_SSN = Entry(search_patient_screen, textvariable=SSN_usr, highlightbackground=back_color).grid(row=3, column=1) 

	txt_2 = Label(search_patient_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=4, column=0)

	#######
	# Buttons
	#######

	button_search = Button(search_patient_screen, fg=font_color, text="Search patient", command=search_SSN, width=12, height=2).grid(row=9, column=0)
	button_cancel = Button(search_patient_screen, fg=font_color, text="Cancel", command=closeSearchPatient_open_start, width=6, height=2).grid(row=9, column=1)


	search_patient_screen.mainloop()



def create_patientHome_screen():
	global patient_home_screen

	global searched_patient_SSN

	patient_info = obtain_patient_info(int(searched_patient_SSN))
	patient_firstName = patient_info[0].capitalize()
	patient_lastName = patient_info[1].capitalize()
	patient_age = str(patient_info[3])


	patient_name_txt = "Patient: " + patient_firstName + " " + patient_lastName
	age_txt = "Age: " + str(current_age(patient_age)) + " years"


	patient_home_screen = Tk()
	patient_home_screen.title("Patient home screen")	
	patient_home_screen.geometry("600x300")

	txt_1 = Label(patient_home_screen, text=patient_name_txt, fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0)

	txt_2 = Label(patient_home_screen, text=age_txt, fg=font_color, 
						font=("Helvetica", 18),
						bg=back_color).grid(row=2, column=0)


	txt_1_3 = Label(patient_home_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=3, column=0)

	#######
	# Buttons
	#######

	button_view_prescriptions = Button(patient_home_screen, fg=font_color, text="View prescriptions",
	 command=not_working, width=14, height=2).grid(row=4, column=0)
	
	button_add_prescription = Button(patient_home_screen, fg=font_color, text="Add prescription",
	 command=not_working, width=14, height=2).grid(row=4, column=1)

	button_edit = Button(patient_home_screen, fg=font_color, text="Edit information",
	 command=closePatientHome_open_editPatientInfo, width=14, height=2).grid(row=5, column=0)

	
	button_cancel = Button(patient_home_screen, fg=font_color, text="Cancel", 
		command=closePatientHome_open_searchPatient, width=14, height=2).grid(row=5, column=1)


	patient_home_screen.mainloop()



def create_edit_patient_info_screen():
	global edit_patient_info_screen

	global searched_patient_SSN

	# Retireve information from the database to pre poluate the entry boxes
	patient_info = obtain_patient_info(int(searched_patient_SSN))
	patient_firstName = patient_info[0].capitalize()
	patient_lastName = patient_info[1].capitalize()
	patient_SSN = patient_info[2]
	patient_dob = str(patient_info[3])
	patient_city = patient_info[4]


	edit_patient_info_screen = Tk()
	edit_patient_info_screen.title("New patient")
	edit_patient_info_screen.geometry("600x300")



	global firstName_usr, lastName_usr, SSN_usr, DOB_usr, city_usr

	# Data that we are going to capture
	firstName_usr = StringVar()
	lastName_usr = StringVar()
	SSN_usr = StringVar()
	DOB_usr = StringVar()
	city_usr = StringVar()



	txt_1 = Label(edit_patient_info_screen, text="Please update patient's information", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0)


	txt_1_3 = Label(edit_patient_info_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=2, column=0)

	txt_firstName = Label(edit_patient_info_screen, text="First name:", bg=back_color, fg=font_color).grid(row=3, column=0)
	input_firstName = Entry(edit_patient_info_screen, textvariable=firstName_usr, highlightbackground=back_color)
	# Populate with infomration stored in the databe
	input_firstName.insert(END, patient_firstName)
	input_firstName.grid(row=3, column=1) 

	txt_lastName = Label(edit_patient_info_screen, text="Last name:", bg=back_color, fg=font_color).grid(row=4, column=0)
	input_lastName = Entry(edit_patient_info_screen, textvariable=lastName_usr, highlightbackground=back_color)
	# Populate with infomration stored in the databe
	input_lastName.insert(END, patient_lastName)
	input_lastName.grid(row=4, column=1)  

	txt_SSN = Label(edit_patient_info_screen, text="SSN:", bg=back_color, fg=font_color).grid(row=5, column=0)
	input_SSN = Entry(edit_patient_info_screen, textvariable=SSN_usr, highlightbackground=back_color)
	# Populate with information stored in the databe
	input_SSN.insert(END, patient_SSN)
	input_SSN.grid(row=5, column=1)   

	txt_DOB = Label(edit_patient_info_screen, text="Date of birth (2012-5-21):", bg=back_color, fg=font_color).grid(row=6, column=0)
	input_DOB = Entry(edit_patient_info_screen, textvariable=DOB_usr, highlightbackground=back_color)
	# Populate with information stored in the databe
	input_DOB.insert(END, patient_dob)
	input_DOB.grid(row=6, column=1)   

	txt_city = Label(edit_patient_info_screen, text="City:", bg=back_color, fg=font_color).grid(row=7, column=0)
	input_city = Entry(edit_patient_info_screen, textvariable=city_usr, highlightbackground=back_color)
	# Populate with information stored in the databe
	input_city.insert(END, patient_city)
	input_city.grid(row=7, column=1)   

	txt_1_3 = Label(edit_patient_info_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=8, column=0)

	#######
	# Buttons
	#######
	button_print = Button(edit_patient_info_screen, fg=font_color, text="Update patient", command=update_patient_info, width=12, height=2).grid(row=9, column=0)
	button_print = Button(edit_patient_info_screen, fg=font_color, text="Cancel", command=closeEditPatientInfo_open_patientHome, width=12, height=2).grid(row=9, column=1)


	edit_patient_info_screen.mainloop()







########################
# Transition between screens
########################
def closeMessage_open_startScreen():
	msg_newPatient_screen.destroy()
	create_start_screen()

def closeMessage_open_newPatient():
	msg_newPatient_screen.destroy()
	create_new_patient_screen()

def closeNewPatient_open_start():
	new_patient_screen.destroy()
	create_start_screen()

def closeStart_open_newPatient():
	start_screen.destroy()
	create_new_patient_screen()

def closeStart_open_SearchPatient():
	start_screen.destroy()
	create_searchPatient_screen()


def closeSearchPatient_open_start():
	search_patient_screen.destroy()
	create_start_screen()

def closePatientHome_open_searchPatient():
	patient_home_screen.destroy()
	create_searchPatient_screen()

def closePatientHome_open_editPatientInfo():
	patient_home_screen.destroy()
	create_edit_patient_info_screen()


def closeEditPatientInfo_open_patientHome():
	edit_patient_info_screen.destroy()
	create_patientHome_screen()

def closeMessageUpdate_open_patientHome():
	msg_updatedPatientInfo_screen.destroy()
	create_patientHome_screen()

########################
# Data processing
########################


def not_working():
	messagebox.showinfo("Not working", "Sorry, this function will work on the next version")
	return


def search_SSN():
	global search_patient_screen

	global SSN_usr, searched_patient_SSN
	searched_patient_SSN = SSN_usr.get()

	if not searched_patient_SSN.isdigit():
		messagebox.showinfo("Error", "The introduced SSN must contain only digits.")
		return

	elif check_SSN_dont_exist_database(searched_patient_SSN):
		messagebox.showinfo("Error", "The introduced SSN doesn't exist in the database. Please create a new patient.")
		return
	else:
		search_patient_screen.destroy()
		create_patientHome_screen()
	return


	
def create_new_patient():
	global new_patient_screen
	global firstName_usr, lastName_usr, SSN_usr, DOB_usr, city_usr
	patient_info = [firstName_usr.get(), lastName_usr.get(), SSN_usr.get(), 
	DOB_usr.get(), city_usr.get()]

	# Validate user input
	if invalid_PatientInfo(patient_info):
		return

	# Check if SSN exist in the db
	if check_SSN_dont_exist_database(SSN_usr.get()):
		add_patient(patient_info)
		create_msg_newPatient_created_scree(patient_info)
		return
	else:
		# return a message that SSN is not unique
		messagebox.showinfo("Error", "The introduced SSN already exist in the database")
		return


def update_patient_info():
	global edit_patient_info_screen

	global searched_patient_SSN

	global firstName_usr, lastName_usr, SSN_usr, DOB_usr, city_usr
	patient_info = [firstName_usr.get(), lastName_usr.get(), SSN_usr.get(), 
	DOB_usr.get(), city_usr.get()]

	if invalid_PatientInfo(patient_info):
		return


	# Check is SSN changed from what is stored in the database
	if SSN_usr.get() == searched_patient_SSN:
		update_info_db(patient_info, searched_patient_SSN)
		# Create message for update information
		create_msg_Patient_updated_screen(patient_info)
		
		return
	else:
		# Check if SSN exist in the db
		if check_SSN_dont_exist_database(SSN_usr.get()):
			update_info_db(patient_info, searched_patient_SSN)
			# update the value of the searched SSN to the new value
			searched_patient_SSN = SSN_usr.get()

			# Create message for update information
			create_msg_Patient_updated_screen(patient_info)
			return
		else:
			# return a message that SSN is not unique
			messagebox.showinfo("Error", "The introduced SSN already exist in the database")
			return


##########
# Validation functions
##########
def invalid_date(date):
	try:
		datetime.strptime(date, "%Y-%m-%d")
	except ValueError:
		return True
	return False


def current_age(dob):
	today = datetime.now()
	dob = datetime.strptime(dob, "%Y-%m-%d")
	years = today.year - dob.year
	if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
		years -= 1
	return years

def invalid_PatientInfo(patient_info_ls):
		# Check name is not empty
	firstName = patient_info_ls[0]
	lastName = patient_info_ls[1]
	SSN = patient_info_ls[2]
	DOB = patient_info_ls[3]


	if firstName.strip() == '':
		messagebox.showinfo("Error", "The introduced Fisrt name is empty, it is a required field.")	
		return True

	# Check last name is not empty
	elif lastName.strip() == '':
		messagebox.showinfo("Error", "The introduced Last name is empty, it is a required field.")
		return True

	# Check valid SSN
	elif not SSN.isdigit():
		messagebox.showinfo("Error", "The introduced SSN must contain only digits.")
		return True

	elif len(SSN) != 9:
		messagebox.showinfo("Error", "The introduced SSN must contain 9 digits.")
		return True

	# Check dob is valid date and format
	elif invalid_date(DOB):
		messagebox.showinfo("Error", "The introduced date of birth must be in the format YYYY-MM-DD.")
		return True
	# Check dob is not a future date
	elif datetime.now() < datetime.strptime(DOB, "%Y-%m-%d"):
		messagebox.showinfo("Error", "The introduced date of birth is a future date.")
		return True

	# Cannot be grater than 140)
	elif current_age(DOB) > 140:
		messagebox.showinfo("Error", "The introduced date of birth returns a calculated age over 140 years.\nPlease correct the date.")
		return True
	return False
	



##########
# Program
##########

create_start_screen()




