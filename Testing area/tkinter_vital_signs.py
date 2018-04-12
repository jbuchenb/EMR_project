from tkinter import *


# Creat a module 
# def open_ehr():
# 	ehr = Tk()
# 	ehr.geometry("500x600")
# 	txt_1 = Label(ehr, text="Congratulations, you did your first log in!!").grid(row=1)
# 	login_screen.destroy()
# 	ehr.mainloop()


def display_vital():
	r = Text(vitals_screen, fg=font_color,  width=40, height=15)
	r.insert(INSERT, "HR\tRR\tT\tSBP\tDBP\n")
	ls = [heart_rate_usr.get(), resp_rate_usr.get(), temperature_usr.get(), sistolic_bp_usr.get(), diastolic_bp_usr.get()]
	line =  "\t".join(ls)	
	r.insert(INSERT, line)
	r.grid(row=14,column=1)
	r.config(state=DISABLED) # Don't allow to edit the content


dynamic_patient = []
def display_radio_button_selection():
	for item in dynamic_patient:
		item.destroy()
	radio_button_txt = Text(vitals_screen, fg=font_color,  width=40, height=15)
	radio_button_txt.insert(INSERT, usr_patient_rad.get())
	radio_button_txt.grid()
	radio_button_txt.config(state=DISABLED) # Don't allow to edit the content
	dynamic_patient.append(radio_button_txt)



# Dynamics labels is required to capture the new created options and
# replace them with the new option that you want to show

dynamic_labels = []

patients = ["Juanito", "Pepito", "Pedrito"]

def create_labels():
	for item in dynamic_labels:
		item.destroy()

	label_temp = Label(vitals_screen, text="Please select from the following matchs:", bg=back_color, fg=font_color)
	label_temp.grid()
	dynamic_labels.append(label_temp)
	for patient in patients:
		input_rad_temp = Radiobutton(vitals_screen, text=patient, value=patient, variable=usr_patient_rad,
							fg=font_color)
		# dynamic_labels.append(label_temp)
		input_rad_temp.grid()
		dynamic_labels.append(input_rad_temp)
	button_display = Button(vitals_screen, fg=font_color, text="Display selection",
	 command=display_radio_button_selection, width=13, height=2).grid()







vitals_screen = Tk()
vitals_screen.title("Vitals signs")
vitals_screen.geometry("600x800")

back_color = "white"
font_color = "grey"
grey_color = "#e5e5e5"



heart_rate_usr = StringVar()
resp_rate_usr = StringVar()
temperature_usr = StringVar()
sistolic_bp_usr = StringVar()
diastolic_bp_usr = StringVar()

usr_patient_rad = StringVar()

txt_1_1 = Label(vitals_screen, text="	   ", fg=font_color, 
					font=("Helvetica", 26),
					bg=grey_color).grid(row=1, column=0)

txt_1 = Label(vitals_screen, text="Please input patients vitals", fg=font_color, 
					font=("Helvetica", 26),
					bg=grey_color).grid(row=1, column=1)


txt_1_2 = Label(vitals_screen, text="		", fg=font_color, 
					font=("Helvetica", 26),
					bg=grey_color).grid(row=1, column=2)

# txt_1_1 = Label(vitals_screen, text="", fg=font_color, 
# 					font=("Helvetica", 26),
# 					bg=grey_color).grid(row=1, col=2)

txt_1_3 = Label(vitals_screen, text="", fg=font_color, 
					font=("Helvetica", 26),
					bg=back_color).grid(row=2, column=0)

txt_heart_rate = Label(vitals_screen, text="Heart rate (HR):", bg=back_color, fg=font_color).grid(row=3, column=0)
input_heart_rate = Entry(vitals_screen, textvariable=heart_rate_usr, highlightbackground=back_color).grid(row=3, column=1) 

txt_resp_rate = Label(vitals_screen, text="Respiratory rate (RR):", bg=back_color, fg=font_color).grid(row=4, column=0)
input_resp_rate = Entry(vitals_screen, textvariable=resp_rate_usr, highlightbackground=back_color).grid(row=4, column=1) 

txt_tempearute = Label(vitals_screen, text="Temperature (T):", bg=back_color, fg=font_color).grid(row=5, column=0)
input_temperature = Entry(vitals_screen, textvariable=temperature_usr, highlightbackground=back_color).grid(row=5, column=1) 

txt_sistolic_bp = Label(vitals_screen, text="SBP:", bg=back_color, fg=font_color).grid(row=6, column=0)
input_sistolic_bp = Entry(vitals_screen, textvariable=sistolic_bp_usr, highlightbackground=back_color).grid(row=6, column=1) 

txt_diastolic_bp = Label(vitals_screen, text="DBP:", bg=back_color, fg=font_color).grid(row=7, column=0)
input_diastolic_bp = Entry(vitals_screen, textvariable=diastolic_bp_usr, highlightbackground=back_color).grid(row=7, column=1) 

space_1 = Label(vitals_screen).grid(row=8)

button_print = Button(vitals_screen, fg=font_color, text="Display vitals", command=display_vital, width=12, height=2).grid(row=9, column=0)
button_print = Button(vitals_screen, fg=font_color, text="Display options", command=create_labels, width=12, height=2).grid(row=9, column=1)

vitals_screen.mainloop()

