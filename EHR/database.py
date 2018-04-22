import pandas as pd
import numpy as np
# import new_patient
# import search_patient



df = pd.read_excel("database.xlsx")

def check_SSN_dont_exist_database(SSN):
	SSN = int(SSN)
	if SSN in df["SSN"].values.tolist():
		return False
	else:
		return True




def add_patient(ls_patient_info):
	global df
	new_patient_SSN = ls_patient_info[2]
	# convert to df

	temp_array = np.asarray(ls_patient_info)
	temp_array = temp_array.reshape(1, len(ls_patient_info))

	temp = pd.DataFrame(temp_array, columns = list(df))
	

	# check if SSN exist
	if new_patient_SSN in df["SSN"].values.tolist():
		print("Patient already on the database")
		######
		# Return error message
		return
	else:
		df = df.append(temp, ignore_index = True)
		#print(df)
		df.to_excel("database.xlsx")
		df = pd.read_excel("database.xlsx")
		# frames = [df, temp]
		# result = pd.concat(frames, axis = 0)
	return



def obtain_patient_info(searched_patient_SSN):
	global df
	patient_info = df.loc[df.loc[:, "SSN"] == searched_patient_SSN, :].values.tolist()[0]
	# convert to string


	# convert nan values to ''
	for i, data in enumerate(patient_info):
		# Only works for float type
		if type(data) == type(1.2):
			if np.isnan(data):
				patient_info[i] = ''

	return patient_info




def update_info_db(ls_patient_info, SSN):
	global df

	SSN = int(SSN)

	temp_array = np.asarray(ls_patient_info)
	temp_array = temp_array.reshape(1, len(ls_patient_info))

	df.loc[df.loc[:, "SSN"] == SSN, :] = temp_array

	df.to_excel("database.xlsx")
	df = pd.read_excel("database.xlsx")
	return

# buiild the other tables using the index in df as patient id

# print(obtain_patient_info(int("1234")))
# print(type(obtain_patient_info(int("1234"))[3]))

# update_info_db(["Mario", "B", 123, "1999-2-26", "London"], 123)

