import pandas as pd
import numpy as np
from datetime import datetime 
# import new_patient
# import search_patient



df = pd.read_excel("patient_db.xlsx")
vitals = pd.read_excel("vitals_db.xlsx")
prescriptions = pd.read_excel("prescriptions_db.xlsx")
drugs = pd.read_excel("drugs_db.xlsx")



def check_SSN_dont_exist_database(SSN):
	global df
	SSN = int(SSN)
	if SSN in df["SSN"].values.tolist():
		return False
	else:
		return True


# print(check_SSN_dont_exist_database(123412341))

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
		df.to_excel("patient_db.xlsx")
		# It is not requiered to read agian the file just written
		df = pd.read_excel("patient_db.xlsx")
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

	df.to_excel("patient_db.xlsx")
	df = pd.read_excel("patient_db.xlsx")
	return

# buiild the other tables using the index in df as patient id

# print(obtain_patient_info(int("1234")))
# print(type(obtain_patient_info(int("1234"))[3]))

# update_info_db(["Mario", "B", 123, "1999-2-26", "London"], 123)




def add_vitals_to_db(dict_vitals):
	'''
	Expected dictionary like the following
	dict_vitals = {"patient_id":1, "heart rate":90, "sbp":140, "dbp":75, "date":datetime.now()}

	'''

	global vitals

	# Retrieve the last index used and add 1 to it
	last_index = vitals.tail(1).index.tolist()[0] + 1
	# convert the integer into a Int64Index type
	last_index = pd.Index([last_index])

	temp = pd.DataFrame(data=dict_vitals, index = last_index)
	# Melt the df
	temp = pd.melt(temp, id_vars=["patient_id", "date"], var_name="vital_type")
	# print(temp)
	col_order = ["patient_id", "vital_type", "value",  "date"]
	temp = temp[col_order]
	# Merge with vitals db
	vitals = pd.merge(vitals, temp, how="outer")
	# Store the df in the db
	vitals.to_excel("vitals_db.xlsx")
	return

def obtain_patient_id(SSN):
	global df
	# SSN is stored as integer
	SSN = int(SSN)
	patient_row = df.loc[:, "SSN"] == SSN
	return df.loc[patient_row, :].index.tolist()[0]


def obtain_vitals(SSN):
	'''
	It returns the last five vitals added to the db, as a list of lists.
	The last list is the columns names
	'''
	global vitals
	vitals_ls = []
	SSN = int(SSN)
	patient_id = obtain_patient_id(SSN)
	patient_rows = vitals.loc[:, "patient_id"] == patient_id
	temp = vitals.loc[patient_rows, :]
	# Pivot the obtained df
	temp = temp.drop("patient_id", axis=1)
	temp = temp.pivot(index="date", columns="vital_type", values="value")
	# Convert index into column
	temp.reset_index(level=0, inplace=True)
	# Sort descending
	temp = temp.sort_values(by=["date"], ascending=False)

	# Sort column order
	col_order = ["heart rate", "sbp", "dbp", "date"]
	temp = temp[col_order]
	# Convert temp into a list of list and append it
	vitals_ls = temp.values.tolist()
	# Replace nan values for empty string
	for i, ls in enumerate(vitals_ls):
		for e, item in enumerate(ls):
			if type(item) == type(1.2):
				if np.isnan(item):
					vitals_ls[i][e] = ''


	# append the names of the columns
	vitals_ls.append(list(temp))

	
	return vitals_ls


# print(obtain_vitals(123456789))
# print(obtain_patient_id(123456789))


def obtain_prescriptions(SSN):
	'''
	It returns the last ten prescriptions added to the db, as a list of lists.
	The last list is the columns names
	'''
	global prescriptions, drugs
	presciption_ls = []
	SSN = int(SSN)
	patient_id = obtain_patient_id(SSN)
	patient_rows = prescriptions.loc[:, "patient_id"] == patient_id
	temp = prescriptions.loc[patient_rows, :]
	# Sort descending
	temp = temp.sort_values(by=["date"], ascending=False)
	# Only the last 10
	temp = temp.head(10)
	# Left join with drug db
	temp = temp.join(drugs, on="drug_id", how="left", rsuffix='_temp')
	# Drop drug id columns
	temp = temp.drop(["drug_id", "drug_id_temp"], axis=1)
	# Order the columns
	col_order = ['patient_id','drug_name', 'signa', 'dispense', 'refill', 'date']
	temp = temp[col_order]

	# Rename the columns
	temp = temp.rename(index=str, columns={"drug_name":"Drug Name", "singa":"Directions"})

	# Convert temp into a list of list and append it
	presciption_ls = temp.values.tolist()
	# append the names of the columns
	presciption_ls.append(list(temp))

	return presciption_ls

# print(obtain_prescriptions(123456789))

def add_prescription_to_db(dict_prescription):
	'''
	it take a list and add prescription to the db
	dict example = {"patient_id":1, "drug_id":37, "signa":"1 pill",
	"dispense":90, "refill":"No", "date": datetime.now()}
	'''

	global prescriptions

	# Retrieve the last index used and add 1 to it
	last_index = prescriptions.tail(1).index.tolist()[0] + 1
	# convert the integer into a Int64Index type
	last_index = pd.Index([last_index])

	temp = pd.DataFrame(data=dict_prescription, index = last_index)

	# print(temp)
	col_order = ["patient_id", "drug_id", "signa", "dispense", "refill", "date"]
	temp = temp[col_order]
	# Merge with vitals db
	prescriptions = pd.merge(prescriptions, temp, how="outer")
	# Store the df in the db
	prescriptions.to_excel("prescriptions_db.xlsx")
	return


# add_prescription_to_db({"patient_id":1, "drug_id":37, "signa":"1 pill",
# 	"dispense":90, "refill":"No", "date": datetime.now()})


def search_by_drug_name(drug_name):
	'''
	it takes a drug names, search for it in the drugs bd and return a list of
	list with match. Max output is limite to top 10 results
	Example:
	search_drug("ZYPREXA")
	>>> [['ZYPREXA (OLANZAPINE)', 37], ['ZYPREXA ZYDIS (OLANZAPINE)', 39], ['ZYPREXA RELPREVV (OLANZAPINE PAMOATE)', 52]]

	'''

	global drugs
	drug_ls = []

	# Search for the drug
	drug_rows = drugs.loc[:, "drug_name"].str.contains(drug_name, case=False)
	df_match = drugs.loc[drug_rows,:]
	# Convert to list of list, limit the output to ten results
	drug_ls = df_match.head(10).values.tolist()

	return drug_ls



# print(search_by_drug_name("ZYPREXA"))
# print(search_by_drug_name("13456"))

def search_by_drug_id(drug_id):
	'''
	it takes a drug id, search for it in the drugs bd and returns the drug name
	Example:
	search_by_drug_id(37)
	>>> ZYPREXA (OLANZAPINE)

	'''

	global drugs
	drug_id = int(drug_id)
	drug_name = ''

	# Search for the drug
	drug_row = drugs.loc[:, "drug_id"] == drug_id
	drug_name = drugs.loc[drug_row,: "drug_name"].values.tolist()[0][0]


	return drug_name

# print(search_by_drug_id(37))
# dict_vitals = {"patient_id":1, "vital_type":"heart rate", "value":90, "date":datetime.now()}

# dict_vitals = {"patient_id":1, "heart rate":90, "sbp":140, "dbp":75, "date":datetime.now()}



# print(vitals.info())
# print(temp.info())



# print(dict_vitals)




# ls = [1,2,3,4]

# # Write the list to the file
# f = open("test.txt", 'w')
# for item in ls:
# 	f.write(str(item))
# 	f.write('|')
# f.close()


# # Read the file to a list
# f = open("patient_data.txt", 'r')
# ls1 = f.read().split("\n")
# f.close()
# #ls1 = ls1[:len(ls1)-1]
# #print(ls1)

# good_ls = []
# for i in ls1:
# 	good_ls.append(i.split("\t"))

# print(good_ls)





# print("string"+"\nstring")



# print("\t".join(["CIALIS\n", "one pill", "30", "no refill", "2015-05-03"]))









