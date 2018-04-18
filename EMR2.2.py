from tkinter import *

First = 0
Middle_I = 0
Last = 0
DOBmonth = 0
DOBday = 0
DOByear = 0
Sex = 0
SSN1 = 0
SSN2 = 0
SSN3 = 0
Address1 = 0
Address2 = 0
ZIP = 0
Email = 0
Female = 'Female'
Male = 'Male'



def retrieve_input(*args):
    First = firstname_input.get()
    Middle_I = middle_I_input.get()
    Last = lastname_input.get()
    DOBmonth = DOBmonth_input.get()
    DOBday = DOBday_input.get()
    DOByear = DOByear_input.get()
    Sex = sex_choice.get()
    SSN1 = SSN1_input.get()
    SSN2 = SSN2_input.get()
    SSN3 = SSN3_input.get()
    Address1 = street_address1.get()
    Address2 = street_address2.get()
    ZIP = zip_code_input.get()
    Email = email_input.get()
    
    SSN = SSN1+SSN2+SSN3
    Address = Address1+Address2
    patient_info = [First, Middle_I, Last, Sex, DOBmonth, DOBday, DOByear, SSN, Address, ZIP, Email]
    print(patient_info)
    return patient_info
    


def limitSize(*args):
    first = First.get()
    if len(first) > 20: First.set(first[:20])
    middle = Middle_I.get()
    if len(middle) > 1: Middle_I.set(middle[:1])
    last = Last.get()
    if len(last) > 30: Last.set(last[:30])
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
    address1 = Address1.get()
    if len(address1) > 40: Address1.set(address1[:40])
    address2 = Address2.get()
    if len(address2) > 30: Address2.set(address2[:30])
    zip_ = ZIP.get()
    if len(zip_) > 5: ZIP.set(zip_[:5])
    emails = Email.get()
    if len(emails) > 40: Email.set(emails[:40])
    
    
#Creating Profile menu
main_window = Tk()
main_window.title("Main")
menu = Menu(main_window)
new_item = Menu(menu)
new_item.add_command(label='Patient Search')
new_item.add_separator()
new_item.add_command(label='Edit Profile')
new_item.add_separator()
new_item.add_command(label='Create New Profile')
menu.add_cascade(label='Profile', menu=new_item)
main_window.config(menu=menu)
main_window.mainloop()


#Demographic Info Window    
demographic = Tk()
demographic.title("Demographic Information")
demographic.geometry("600x400+100+100")

demographic.main_container = Frame(demographic)
demographic.main_container.grid(column = 0, columnspan = 2, row = 0, rowspan = 2)

demographic.name_container = Frame(demographic.main_container)
demographic.name_container.pack(side = 'top')

demographic.sex_container = Frame(demographic.main_container)
demographic.sex_container.pack()

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


First = StringVar()
First.trace('w', limitSize)
Middle_I = StringVar()
Middle_I.trace('w', limitSize)
Last = StringVar()
Last.trace('w', limitSize)
sex_choice = StringVar()
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
Address1 = StringVar()
Address1.trace('w', limitSize)
Address2 = StringVar()
Address2.trace('w', limitSize)
ZIP = StringVar()
ZIP.trace('w', limitSize)
Email = StringVar()
Email.trace('w', limitSize)


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

#Sex label and Radiobutton entry boxes
sex_label = Label(demographic.sex_container, text = "Sex: ").pack(side = LEFT)
sex_input1 = Radiobutton(demographic.sex_container,text='Female', width = 5, value= Female, variable = sex_choice)
sex_input1.pack(side = LEFT)
sex_input2 = Radiobutton(demographic.sex_container,text='Male', width = 5, value= Male, variable = sex_choice)
sex_input2.pack(side = LEFT)


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

street_address1 = Entry(demographic.address_container, width= 40, textvariable= Address1)
street_address1.grid(column = 1, row = 0)

street_address2 = Entry(demographic.address_container, width=40, textvariable= Address2)
street_address2.grid(column = 1, row = 1)

zip_code = Label(demographic.zip_container, text = "ZIP Code: ")
zip_code.grid(column = 0, row = 2, padx = 10)

zip_code_input = Entry(demographic.zip_container, width = 10, textvariable= ZIP)
zip_code_input.grid(column = 1, row = 2)

#state = Entry(demographic.address_container, width = 10, textvariable= "State")


email = Label(demographic.email_container, text = "Email: ")
email.grid(column = 0, row = 0, padx = 10)

email_input = Entry(demographic.email_container, width = 40, textvariable= Email)
email_input.grid(column = 1, row = 0)



save = Button(demographic.main_container, width=5, text="Save", command=lambda: retrieve_input())
save.pack(side="bottom")

mainloop()
