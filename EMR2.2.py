from tkinter import *

First = 0
Middle_I = 0
Last = 0
DOBmonth = 0
DOBday = 0
DOByear = 0
SSN1 = 0
SSN2 = 0
SSN3 = 0
Address = 0
Address2 = 0
ZIP = 0
Email = 0

#Don't think we will need this anymore, but TBD
def retrieve_input(*args):
    '''provides variable place for entry values to be placed in'''
    First = [firstname_input.get()]
    Last = [lastname_input.get()]
    DOBmonth =[DOBmonth_input.get()]
    DOBday = [DOBday_input.get()]
    DOByear = [DOByear_input.get()]
    SSN1 = SSN1_input.get()
    SSN2 = SSN2_input.get()
    SSN3 = SSN3_input.get()
    print("Patient Values:", First, Last, DOBmonth, DOBday, DOByear, SSN1, SSN2, SSN3)
    


def limitSize(*args):
    '''Limites size of each individual text box to our specified length'''
    first = First.get()
    if len(first) > 20: DOBmonth.set(first[:20])
    middle = Middle_I.get()
    if len(middle) > 1: DOBmonth.set(middle[:1])
    last = Last.get()
    if len(last) > 30: DOBmonth.set(last[:30])
    DOB_m = DOBmonth.get()
    if len(DOB_m) > 2: DOBmonth.set(DOB_m[:2])
    DOB_d = DOBday.get()
    if len(DOB_d) > 2: DOBday.set(DOB_d[:2])
    DOB_y = DOByear.get()
    if len(DOB_y) > 4: DOByear.set(DOB_y[:4])
    SSN_1 = SSN1.get()
    if len(SSN_1) > 3: SSN1.set(SSN_1[:3])
    SSN_2 = SSN2.get()
    if len(SSN_2) > 2: SSN2.set(SSN_2[:2])
    SSN_3 = SSN3.get()
    if len(SSN_3) > 4: SSN3.set(SSN_3[:4])
    

'''
Main container = demographic 
Subcontainers are defined below (demographic.XXX)
'''
demographic = Tk()
demographic.title("Demographic Information")
demographic.geometry("600x400+100+100")

demographic.main_container = Frame(demographic)
demographic.main_container.grid(column = 0, columnspan = 2, row = 0, rowspan = 2)

demographic.name_container = Frame(demographic.main_container)
demographic.name_container.pack(side = 'top')

demographic.DOB_container = Frame(demographic.main_container)
demographic.DOB_container.pack()

demographic.SSN_container = Frame(demographic.main_container)
demographic.SSN_container.pack()

demographic.address_container = Frame(demographic.main_container)
demographic.address_container.pack()

demographic.zip_container = Frame(demographic.main_container)
demographic.zip_container.pack()

demographic.email_container =Frame(demographic.main_container)
demographic.email_container.pack()


DOBmonth = StringVar()
DOBmonth.trace('w', limitSize)
DOBday = StringVar()
DOBday.trace('w', limitSize)
DOByear = StringVar()
DOByear.trace('w', limitSize)

SSN1 = StringVar()
SSN1.trace('w', limitSize)
SSN2 = StringVar()
SSN2.trace('w', limitSize)
SSN3 = StringVar()
SSN3.trace('w', limitSize)

#First name label and text entry box
firstname = Label(demographic.name_container, text = "First Name: ")
firstname.grid(column = 0, row = 0, padx=10)
firstname_input = Entry(demographic.name_container, width = 20, textvariable= First)
firstname_input.grid(column = 1, row = 0)

# Middle Initial Label and text entry box
middle_I = Label(demographic.name_container, text = "\tMiddle Inital: ")
middle_I.grid(column = 2, row = 0, padx=10)
middle_I_input = Entry(demographic.name_container, width = 5, textvariable = Middle_I)
middle_I_input.grid(column = 3, row = 0)

#Last name label and text entry box
lastname = Label(demographic.name_container, text = "\tLast Name: ")
lastname.grid(column = 4, row = 0, padx = 10)
lastname_input = Entry(demographic.name_container, width = 30, textvariable= Last)
lastname_input.grid(column = 5, row = 0)

#DOB label and text entry boxes
DOB = Label(demographic.DOB_container, text = "Birthdate: ").pack(side = LEFT)
DOBmonth_input = Entry(demographic.DOB_container, width=2, textvariable= DOBmonth)
DOBmonth_input.pack(side = LEFT)
DOBday_input = Entry(demographic.DOB_container, width = 2, textvariable= DOBday)
DOBday_input.pack(side = LEFT)
DOByear_input = Entry(demographic.DOB_container, width = 4, textvariable= DOByear)
DOByear_input.pack(side = LEFT)

#SSN label and text entry boxes
SSN = Label(demographic.SSN_container, text = "Social Security Number: ").pack(side = LEFT)
SSN1_input = Entry(demographic.SSN_container, width=3, textvariable= SSN1)
SSN1_input.pack(side="left")

SSN2_input = Entry(demographic.SSN_container, width=2, textvariable= SSN2)
SSN2_input.pack(side="left")
SSN3_input = Entry(demographic.SSN_container, width=4, textvariable= SSN3)
SSN3_input.pack(side="left")

#Address label and text entry boxes
address = Label(demographic.address_container, text = "Address")
address.grid(column = 0, row = 0, padx = 10) 

street_address1 = Entry(demographic.address_container, width= 40, textvariable= Address)
street_address1.grid(column = 1, row = 0)

street_address2 = Entry(demographic.address_container, width=40, textvariable= Address2)
street_address2.grid(column = 1, row = 1)

ZIP = Label(demographic.zip_container, text = "ZIP Code: ")
ZIP.grid(column = 0, row = 2, padx = 10)

zip_code = Entry(demographic.zip_container, width = 10, textvariable= ZIP)
zip_code.grid(column = 1, row = 2)

#state = Entry(demographic.address_container, width = 10, textvariable= "State")


email = Label(demographic.email_container, text = "Email: ")
email.grid(column = 0, row = 0, padx = 10)

email_input = Entry(demographic.email_container, width = 40, textvariable= Email)
email_input.grid(column = 1, row = 0)

# this is a comment

save = Button(demographic.main_container, width=5, text="Save", command=lambda: retrieve_input())
save.pack(side="bottom")

mainloop()
