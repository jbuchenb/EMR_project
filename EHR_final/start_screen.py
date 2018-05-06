from tkinter import *
from tkinter import messagebox
from datetime import datetime 
#import time
# import new_patient
# import search_patient
from database import (check_SSN_dont_exist_database, add_patient, obtain_patient_info, update_info_db,
search_by_drug_name, obtain_patient_id, search_by_drug_id, add_prescription_to_db,
obtain_prescriptions, obtain_vitals, add_vitals_to_db)


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
search_drug_screen = 0
drug_searchResult_screen = 0
new_prescription_screen = 0
view_prescription_screen = 0
msg_newPrescription_screen = 0
view_vitals_screen = 0
new_vitals_screen = 0
msg_newVitals_screen = 0

#########
# Inputs var
#########
# Patient info
firstName_usr = 0
lastName_usr = 0
SSN_usr = 0
DOB_usr = 0
city_usr = 0
# Prescription
drug_name_usr = 0
drug_id_usr = 0
#
signa_usr = 0
dispense_usr = 0
refill_usr = 0
prescription_date_usr = 0

# Vitals
heart_rate_usr = 0
sbp_usr = 0
dbp_usr = 0



# This variable only sotre integers
searched_patient_SSN = 0

searched_drug_id = 0
searched_drug_name = 0

drug_ls = []



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


	txt_1 = Label(start_screen, text="Please choose on one of the following options", fg=font_color, 
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


	txt_1 = Label(new_patient_screen, text="Please input patients information", fg=font_color, 
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

	# Export to globa enviroment
	# global firstName_usr, lastName_usr, SSN_usr, DOB_usr, city_usr

	new_patient_screen.mainloop()





def create_searchPatient_screen():
	global search_patient_screen
	search_patient_screen = Tk()
	search_patient_screen.title("Search patient")
	search_patient_screen.geometry("600x300")
	
	global SSN_usr

	SSN_usr = StringVar()

	txt_1 = Label(search_patient_screen, text="Please input patients SSN to search", fg=font_color, 
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
	patient_home_screen.title("Patient home scree")	
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
	 command=closePatientHome_open_viewPrescription, width=14, height=2).grid(row=4, column=0)
	
	button_add_prescription = Button(patient_home_screen, fg=font_color, text="Add prescription",
	 command=closePatienthome_open_searchDrug, width=14, height=2).grid(row=4, column=1)

	button_view_vitals = Button(patient_home_screen, fg=font_color, text="View vitals",
	 command=closePatientHome_open_viewVitals, width=14, height=2).grid(row=5, column=0)
	
	button_add_vitals = Button(patient_home_screen, fg=font_color, text="Add vitals",
	 command=closePatientHome_open_newVitals, width=14, height=2).grid(row=5, column=1)

	button_edit = Button(patient_home_screen, fg=font_color, text="Edit information",
	 command=closePatientHome_open_editPatientInfo, width=14, height=2).grid(row=6, column=0)

	
	button_cancel = Button(patient_home_screen, fg=font_color, text="Cancel", 
		command=closePatientHome_open_searchPatient, width=14, height=2).grid(row=6, column=1)


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



	txt_1 = Label(edit_patient_info_screen, text="Please update patients information", fg=font_color, 
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
	# Populate with infomration stored in the databe
	input_SSN.insert(END, patient_SSN)
	input_SSN.grid(row=5, column=1)   

	txt_DOB = Label(edit_patient_info_screen, text="Date of birth (2012-5-21):", bg=back_color, fg=font_color).grid(row=6, column=0)
	input_DOB = Entry(edit_patient_info_screen, textvariable=DOB_usr, highlightbackground=back_color)
	# Populate with infomration stored in the databe
	input_DOB.insert(END, patient_dob)
	input_DOB.grid(row=6, column=1)   

	txt_city = Label(edit_patient_info_screen, text="City:", bg=back_color, fg=font_color).grid(row=7, column=0)
	input_city = Entry(edit_patient_info_screen, textvariable=city_usr, highlightbackground=back_color)
	# Populate with infomration stored in the databe
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



def create_searchDrug_screen():
	global search_drug_screen
	search_drug_screen = Tk()
	search_drug_screen.title("Search drug")
	search_drug_screen.geometry("600x300")
	
	global drug_name_usr

	drug_name_usr = StringVar()

	txt_1 = Label(search_drug_screen, text="Please input drug name\nfor the prescription", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0)


	txt_1_3 = Label(search_drug_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=2, column=0)


	txt_drug = Label(search_drug_screen, text="Drug name:", bg=back_color, fg=font_color).grid(row=3, column=0)
	input_drug = Entry(search_drug_screen, textvariable=drug_name_usr, highlightbackground=back_color).grid(row=3, column=1) 

	txt_2 = Label(search_drug_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=4, column=0)

	#######
	# Buttons
	#######

	button_search = Button(search_drug_screen, fg=font_color, text="Search drug", command=search_drug, width=12, height=2).grid(row=9, column=0)
	button_cancel = Button(search_drug_screen, fg=font_color, text="Cancel", command=closeSearchDrug_open_patientHome, width=6, height=2).grid(row=9, column=1)


	search_drug_screen.mainloop()


def create_drugSearchResult_screen(drug_ls):
	global drug_searchResult_screen
	global drug_id_usr
	# global drug_ls

	drug_searchResult_screen = Tk()
	drug_searchResult_screen.title("Search result")
	drug_searchResult_screen.geometry("650x400")

	drug_id_usr = IntVar()

	txt_1 = Label(drug_searchResult_screen, text="Please select one of the following drugs", fg=font_color, 
					font=("Helvetica", 20),
					bg=back_color).grid(row=1, column=0, sticky=W)

	txt_1_3 = Label(drug_searchResult_screen, text="", fg=font_color, 
					font=("Helvetica", 26),
					bg=back_color).grid(row=2, column=0)


	# Build a list of  radio buttons
	for i, drug in enumerate(drug_ls):
		input_rad_drug = Radiobutton(drug_searchResult_screen, text=drug[0], value=drug[1], variable=drug_id_usr,
							fg=font_color).grid(column=0, sticky=W)

	txt_1_4 = Label(drug_searchResult_screen, text="", fg=font_color, 
					font=("Helvetica", 26),
					bg=back_color).grid(row=13, column=0)

	button_search = Button(drug_searchResult_screen, fg=font_color, text="Use drug", command=select_drug, width=12, height=2).grid(row=14, column=0, sticky=W)
	button_cancel = Button(drug_searchResult_screen, fg=font_color, text="Cancel", command=closeDrugSearchResult_open_searchDrug, width=6, height=2).grid(row = 14, column=1, sticky=W)



	drug_searchResult_screen.mainloop()


def create_newPrescription_screen():
	global new_prescription_screen

	global searched_drug_id, searched_drug_name, searched_patient_SSN, signa_usr, dispense_usr, refill_usr, prescription_date_usr
	
	new_prescription_screen = Tk()
	new_prescription_screen.title("New prescription")
	new_prescription_screen.geometry("600x300")



	patient_id = obtain_patient_id(searched_patient_SSN)
	searched_drug_id = searched_drug_id
	signa_usr = StringVar()
	dispense_usr = StringVar()
	refill_usr = StringVar()
	prescription_date_usr = datetime.now()


	txt_1 = Label(new_patient_screen, text="Please input prescription information", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0)


	txt_1_3 = Label(new_patient_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=2, column=0)
	
	txt_drug_name = Label(new_patient_screen, text=searched_drug_name, bg=back_color, fg=font_color, font=("Helvetica", 16)).grid(row=3, sticky=W)

	txt_signa = Label(new_patient_screen, text="Directions (e.g., One pill a day):", bg=back_color, fg=font_color).grid(row=4, column=0)
	input_signa = Entry(new_patient_screen, textvariable=signa_usr, highlightbackground=back_color).grid(row=4, column=1) 

	txt_dispense = Label(new_patient_screen, text="Dispense: (e.g., 30)", bg=back_color, fg=font_color).grid(row=5, column=0)
	input_dispense = Entry(new_patient_screen, textvariable=dispense_usr, highlightbackground=back_color).grid(row=5, column=1) 

	txt_refill = Label(new_patient_screen, text="Refill (e.g., One year):", bg=back_color, fg=font_color).grid(row=6, column=0)
	input_refill = Entry(new_patient_screen, textvariable=refill_usr, highlightbackground=back_color).grid(row=6, column=1) 




	button_add = Button(new_patient_screen, fg=font_color, text="Add prescription", command=add_prescription, width=13, height=2).grid(row=14, column=0)
	button_cancel = Button(new_patient_screen, fg=font_color, text="Cancel", command=closeNewPrescription_open_searchDrug, width=6, height=2).grid(row = 14, column=1)



	new_prescription_screen.mainloop()
	


def create_msg_newPrescription_created_screen(dict_prescription):

	global msg_newPrescription_screen

	global searched_drug_name

	msg_newPrescription_screen = Tk()
	msg_newPrescription_screen.geometry("500x300")
	msg_newPrescription_screen.title("Prescription created")
	message = ("Prescription created with the following information:\n\n" + 
	searched_drug_name + "\n" +
	"Directions: " + dict_prescription["signa"] + "\n" +
	"Dispense: " + str(dict_prescription["dispense"]) + "\n" +
	"Refill: " +dict_prescription["refill"] + "\n" +
	"Date: " +str(dict_prescription["date"].strftime("%m-%d-%Y")) + "\n" +
	 "\n\nDo you want to create another prescription?")
	Label(msg_newPrescription_screen, text=message, fg=font_color, 
						font=("Helvetica", 14),
						bg=back_color).grid(row=1, sticky=W)

	Label(msg_newPrescription_screen, text="", fg=font_color, 
						font=("Helvetica", 14),
						bg=back_color).grid(row=2, column=0)
	Button(msg_newPrescription_screen,text="Yes", command=closeMsgNewPrescription_open_searchDrug,fg=font_color, width=8, height=2).grid(row=3, column=0)
	Button(msg_newPrescription_screen,text="No", command=closeMsgNewPrescription_open_patientHome,fg=font_color, width=8, height=2).grid(row=3, column=1)

	msg_newPrescription_screen.mainloop()
	return




def create_viewPrescription_screen():
	global view_prescription_screen

	global searched_patient_SSN

	prescription_ls = obtain_prescriptions(searched_patient_SSN)
	col_names = prescription_ls.pop()
	col_names = col_names[1:]
	col_names[1] = "Directions" 

	view_prescription_screen = Tk()
	view_prescription_screen.title("Prescriptions")
	view_prescription_screen.geometry("700x500")

	txt_1 = Label(view_prescription_screen, text="The last ten prescriptions are:", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0, sticky=W)


	txt_1_3 = Label(view_prescription_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=2, column=0)

	txt_1_4 = Label(view_prescription_screen, text="\t".join(col_names).upper(), fg=font_color, 
						font=("Helvetica", 16),
						bg=back_color).grid(row=3, column=0, sticky=W)

	


	for prescription in prescription_ls:
		# Remove patient id
		prescription = prescription[1:]
		# Add a new tab to direction for formating
		prescription[1] = "\t\t\t" + prescription[1]
		# Convert dispense to string
		prescription[2] = str(prescription[2])

		# Conver datetime to str in american format
		prescription[4] = prescription[4].strftime("%m-%d-%Y")
		
		drug = Label(view_prescription_screen, text=prescription[0].strip(), fg=font_color, 
						font=("Helvetica", 12),
						bg=back_color).grid(column=0,sticky=W)

		# Join all in one string
		message = "\t\t".join(prescription[1:])
		prescription = Label(view_prescription_screen, text=message, fg=font_color, 
						font=("Helvetica", 12),
						bg=back_color).grid(column=0,sticky=W)

	Button(view_prescription_screen,text="Go back", command=closeViewPrescription_open_patientHome,fg=font_color, width=8, height=2).grid()
	view_prescription_screen.mainloop()

	return



def create_viewVitals_screen():
	global view_vitals_screen

	global searched_patient_SSN

	vitals_ls = obtain_vitals(searched_patient_SSN)
	# print(vitals_ls)
	col_names = vitals_ls.pop()
	#col_names = col_names[1:]
	#col_names[1] = "Directions" 

	view_vitals_screen = Tk()
	view_vitals_screen.title("Prescriptions")
	view_vitals_screen.geometry("500x500")

	txt_1 = Label(view_vitals_screen, text="The last ten vitals records are:", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0, sticky=W)


	txt_1_3 = Label(view_vitals_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=2, column=0)

	txt_1_4 = Label(view_vitals_screen, text="\t".join(col_names).upper(), fg=font_color, 
						font=("Helvetica", 16),
						bg=back_color).grid(row=3, column=0, sticky=W)

	
# col_order = ["heart rate", "sbp", "dbp", "date"]

	for vital in vitals_ls:
		# Add a new tab to direction for formating
		# prescription[1] = "\t\t\t" + prescription[1]
		# Convert dispense to string
		vital[0] = str(vital[0])
		vital[1] = str(vital[1])
		vital[2] = str(vital[2])

		# Conver datetime to str in american format only if it is a datetime
		if vital[3] != '': 
			vital[3] = vital[3].strftime("%m-%d-%Y %H:%M:%S")
		else:
			vital[3] == ''
		
		# drug = Label(view_vitals_screen, text=prescription[0].strip(), fg=font_color, 
		# 				font=("Helvetica", 12),
		# 				bg=back_color).grid(column=0,sticky=W)

		# Join all in one string
		message = "\t\t".join(vital)
		vital = Label(view_vitals_screen, text=message, fg=font_color, 
						font=("Helvetica", 12),
						bg=back_color).grid(column=0)

	Button(view_vitals_screen,text="Go back", command=closeViewVitals_open_patientHome,fg=font_color, width=8, height=2).grid()
	view_vitals_screen.mainloop()

	return



def create_newVitals_screen():
	global new_vitals_screen


	new_vitals_screen = Tk()
	new_vitals_screen.title("New vitals")
	new_vitals_screen.geometry("600x300")

	global heart_rate_usr, sbp_usr, dbp_usr, searched_patient_SSN

	heart_rate_usr = StringVar()
	sbp_usr = StringVar()
	dbp_usr = StringVar()



	txt_1 = Label(new_vitals_screen, text="Please input patients vitals", fg=font_color, 
						font=("Helvetica", 20),
						bg=back_color).grid(row=1, column=0)


	txt_1_3 = Label(new_vitals_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=2, column=0)

	txt_heart_rate = Label(new_vitals_screen, text="Heart rate:", bg=back_color, fg=font_color).grid(row=3, column=0)
	input_heart_rate = Entry(new_vitals_screen, textvariable=heart_rate_usr, highlightbackground=back_color).grid(row=3, column=1) 

	txt_sbp = Label(new_vitals_screen, text="Sistolic BP:", bg=back_color, fg=font_color).grid(row=4, column=0)
	input_sbp = Entry(new_vitals_screen, textvariable=sbp_usr, highlightbackground=back_color).grid(row=4, column=1) 

	txt_dbp = Label(new_vitals_screen, text="Diastolic BP:", bg=back_color, fg=font_color).grid(row=5, column=0)
	input_dbp = Entry(new_vitals_screen, textvariable=dbp_usr, highlightbackground=back_color).grid(row=5, column=1) 

	txt_1_3 = Label(new_vitals_screen, text="", fg=font_color, 
						font=("Helvetica", 26),
						bg=back_color).grid(row=8, column=0)

	#######
	# Buttons
	#######
	button_add = Button(new_vitals_screen, fg=font_color, text="Add vitals", command=add_new_vitals, width=12, height=2).grid(row=9, column=0)
	button_cancel = Button(new_vitals_screen, fg=font_color, text="Cancel", command=closeNewVitals_open_patientHome, width=12, height=2).grid(row=9, column=1)


	new_vitals_screen.mainloop()

	return

def create_msg_newVitals_created_screen(dict_vitals):

	global msg_newVitals_screen

	
	msg_newVitals_screen = Tk()
	msg_newVitals_screen.geometry("500x300")
	msg_newVitals_screen.title("Vitals created")
	message = ("Vitals created with the following information:\n\n" + 
	"Heart rate: " + str(dict_vitals["heart rate"]) + "\n" +
	"Sistolic BP: " + str(dict_vitals["sbp"]) + "\n" +
	"Diastolic BP: " + str(dict_vitals["dbp"]) + "\n" +
	"Date: " + str(dict_vitals["date"].strftime("%m-%d-%Y %H:%M:%S")) + "\n" +
	 "\n\nDo you want to add another vitals?")
	Label(msg_newVitals_screen, text=message, fg=font_color, 
						font=("Helvetica", 14),
						bg=back_color).grid(row=1, sticky=W)

	Label(msg_newVitals_screen, text="", fg=font_color, 
						font=("Helvetica", 14),
						bg=back_color).grid(row=2, column=0)
	Button(msg_newVitals_screen,text="Yes", command=closeMsgNewVitals_open_NewVitals,fg=font_color, width=8, height=2).grid(row=3, column=0)
	Button(msg_newVitals_screen,text="No", command=closeMsgNewVitals_open_patientHome,fg=font_color, width=8, height=2).grid(row=3, column=1)

	msg_newVitals_screen.mainloop()

	return



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

def closePatienthome_open_searchDrug():
	patient_home_screen.destroy()
	create_searchDrug_screen()

def closeSearchDrug_open_patientHome():
	search_drug_screen.destroy()
	create_patientHome_screen()

def closeDrugSearchResult_open_searchDrug():
	drug_searchResult_screen.destroy()
	create_searchDrug_screen()

def closeViewPrescription_open_patientHome():
	view_prescription_screen.destroy()
	create_patientHome_screen()

def closePatientHome_open_viewPrescription():
	patient_home_screen.destroy()
	create_viewPrescription_screen()

def closePatientHome_open_viewVitals():
	patient_home_screen.destroy()
	create_viewVitals_screen()

def closePatientHome_open_newVitals():
	patient_home_screen.destroy()
	create_newVitals_screen()

def closeViewVitals_open_patientHome():
	view_vitals_screen.destroy()
	create_patientHome_screen()


def closeNewVitals_open_patientHome():
	new_vitals_screen.destroy()
	create_patientHome_screen()

def closeMsgNewVitals_open_patientHome():
	msg_newVitals_screen.destroy()
	create_patientHome_screen()

def closeMsgNewVitals_open_NewVitals():
	msg_newVitals_screen.destroy()
	create_newVitals_screen()


def closeNewPrescription_open_searchDrug():
	# Reset global variables to start a new drug selection
	global searched_drug_id, searched_drug_name, signa_usr, dispense_usr, refill_usr, prescription_date_usr
	searched_drug_id = 0
	searched_drug_name = 0
	signa_usr = 0
	dispense_usr = 0
	refill_usr = 0
	prescription_date_usr = 0


	new_prescription_screen.destroy()
	create_searchDrug_screen()

def closeMsgNewPrescription_open_searchDrug():
	global msg_newPrescription_screen

	# Reset global variables
	global searched_drug_id, searched_drug_name, signa_usr, dispense_usr, refill_usr, prescription_date_usr
	searched_drug_id = 0
	searched_drug_name = 0
	signa_usr = 0
	dispense_usr = 0
	refill_usr = 0
	prescription_date_usr = 0

	msg_newPrescription_screen.destroy()
	create_searchDrug_screen()
	

def closeMsgNewPrescription_open_patientHome():
	global msg_newPrescription_screen

	# Reset global variables
	global searched_drug_id, searched_drug_name, signa_usr, dispense_usr, refill_usr, prescription_date_usr
	searched_drug_id = 0
	searched_drug_name = 0
	signa_usr = 0
	dispense_usr = 0
	refill_usr = 0
	prescription_date_usr = 0

	msg_newPrescription_screen.destroy()
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
		messagebox.showinfo("Error", "The introduced SSN doesn't exist in the database. Please first create the patient.")
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

def search_drug():
	global search_drug_screen
	global drug_name_usr
	# global drug_ls
	drug_name = drug_name_usr.get().strip()

	# Check user input before open next screen
	if drug_name == '':
		messagebox.showinfo("Error", "The introduced drug is empty, please introduce at least four characters")
		return
	elif len(drug_name) < 4:
		messagebox.showinfo("Error", "The introduced drug must be at least four characters")
		return
	else:
		drug_ls = search_by_drug_name(drug_name)
		if drug_ls == []:
			messagebox.showinfo("Error", "The introduced drug is not in the database, please use another")
			return
		else:
			search_drug_screen.destroy()
			create_drugSearchResult_screen(drug_ls)
			return

	# search  for words that match

def select_drug():
	global drug_searchResult_screen
	global drug_id_usr

	global searched_drug_id, searched_drug_name

	searched_drug_id = drug_id_usr.get()

	if searched_drug_id == 0:
		messagebox.showinfo("Error", "It is required that you select one drug in order to continue")
		return
	else:
		drug_searchResult_screen.destroy()
		searched_drug_name = search_by_drug_id(searched_drug_id)
		create_newPrescription_screen()
		return

def add_prescription():
	global new_prescription_screen

	global searched_drug_id, searched_drug_name, signa_usr, dispense_usr, refill_usr, searched_patient_SSN


	patient_id = obtain_patient_id(searched_patient_SSN)
	signa = signa_usr.get().strip()
	dispense = dispense_usr.get().strip()
	refill = refill_usr.get().strip()
	date = datetime.now()



	# validations
	if signa == '':
		messagebox.showinfo("Error", "It is required that Signa is not empty in order to continue")
		return
	elif len(signa) < 4:
		messagebox.showinfo("Error", "It is required that Signa contains four or more characters in order to continue")
		return
	elif refill == '':
		messagebox.showinfo("Error", "It is required that Refill is not empty in order to continue")
		return
	elif len(refill) < 2:
		messagebox.showinfo("Error", "It is required that Refill contains two or more characters in order to continue")
		return
	elif dispense == '':
		messagebox.showinfo("Error", "It is required that Dispense is not empty in order to continue")
		return
	elif not dispense.isdigit():
		messagebox.showinfo("Error", "It is required that Dispense must be a number in order to continue")
		return
	elif int(dispense) < 0:
		messagebox.showinfo("Error", "It is required that Dispense is a positive number greater than 0 in order to continue")
		return
	else:
		dispense = int(dispense)

		dict_prescription = {"patient_id":patient_id, "drug_id":searched_drug_id, "signa":signa,
		"dispense":dispense, "refill":refill, "date":date}

		add_prescription_to_db(dict_prescription)
		new_prescription_screen.destroy()
		create_msg_newPrescription_created_screen(dict_prescription)
		return




def add_new_vitals():
	global new_vitals_screen

	global heart_rate_usr, sbp_usr, dbp_usr, searched_patient_SSN
	
	patient_id = obtain_patient_id(searched_patient_SSN)
	heart_rate = heart_rate_usr.get().strip()
	sbp = sbp_usr.get().strip()
	dbp = dbp_usr.get().strip()
	date = datetime.now()

	# validations
	if heart_rate == "":
		messagebox.showinfo("Error", "It is required that heart rate is not empty in order to continue")
		return
	elif not heart_rate.isdigit():
		messagebox.showinfo("Error", "It is required that heart rate must be a number in order to continue")
		return
	elif int(heart_rate) >= 1000:
		messagebox.showinfo("Error", "It is required that heart rate must be less than 1000 in order to continue")
		return
	if sbp == "":
		messagebox.showinfo("Error", "It is required that Sistolic BP is not empty in order to continue")
		return
	elif not sbp.isdigit():
		messagebox.showinfo("Error", "It is required that Sistolic BP must be a number in order to continue")
		return
	elif int(sbp) >= 1000:
		messagebox.showinfo("Error", "It is required that Sistolic BP must be less than 1000 in order to continue")
		return
	if dbp == "":
		messagebox.showinfo("Error", "It is required that Diastolic BP is not empty in order to continue")
		return
	elif not dbp.isdigit():
		messagebox.showinfo("Error", "It is required that Diastolic BP must be a number in order to continue")
		return
	elif int(dbp) >= 1000:
		messagebox.showinfo("Error", "It is required that Diastolic BP must be less than 1000 in order to continue")
		return
	else:
		heart_rate = int(heart_rate)
		sbp = int(sbp)
		dbp = int(dbp)

		dict_vitals = {"patient_id":patient_id, "heart rate":heart_rate, "sbp":sbp, "dbp":dbp, "date":date}

		# Store in the db
		add_vitals_to_db(dict_vitals)
		new_vitals_screen.destroy()
		create_msg_newVitals_created_screen(dict_vitals)

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
		messagebox.showinfo("Error", "The introduced SSN must contains 9 digits.")
		return True

	# Check dob is valid date and format
	elif invalid_date(DOB):
		messagebox.showinfo("Error", "The introduced Date of birth must be in the format YYYY-MM-DD.")
		return True
	# Check dob is not a future date
	elif datetime.now() < datetime.strptime(DOB, "%Y-%m-%d"):
		messagebox.showinfo("Error", "The introduced Date of birth is a future date.")
		return True

	# Cannot be grater than 140)
	elif current_age(DOB) > 140:
		messagebox.showinfo("Error", "The introduced Date of birth returns a calculated age over 140 years.\nPlease correct the date.")
		return True
	return False
	



##########
# Program
##########

create_start_screen()




