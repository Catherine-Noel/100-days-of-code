import tkinter as tk
from tkinter import ttk
from tkinter import *

# Get inputs from the text box
def get_bill():
	userInput = bill_input.get()
	return int(userInput)


# Get the selected list box value
def get_tip():
	itemSelected = tip_input.curselection()
	print(itemSelected)
	if itemSelected == (0,):
		return 10
	elif itemSelected == (1,):
		return 15
	elif itemSelected == (2,):
		return 20
	else:
		print('Error')


# Get input from the text box
def get_people():
	userInput = people_input.get()
	return int(userInput)

# Button is clicked
def btnClickFunction():
    pay_amount = float((get_bill() * get_tip() / 100 ) + get_bill()) / get_people()
    rounded_pay_amount = round(pay_amount, 2)
    print(f'Each person should pay: ${rounded_pay_amount}0')
    print(get_bill(), get_tip(), get_people())
	# Create a label
    Label(root, text=f'Each person should pay: ${rounded_pay_amount}', bg='#EEDFCC', font=('arial', 14, 'normal')).place(x=15, y=376)

#Main Window
root = Tk()
root.geometry('350x450')
root.configure(background='#EEDFCC')
root.title('Tip Calculator')

# Input boxes
bill_input=Entry(root)
bill_input.place(x=78, y=86)
people_input=Entry(root)
people_input.place(x=78, y=276)

# Labels
Label(root, text='Total of Bill:', bg='#EEDFCC', font=('arial', 14, 'normal')).place(x=58, y=56)
Label(root, text='Tip %', bg='#EEDFCC', font=('arial', 14, 'normal')).place(x=128, y=116)
Label(root, text='Number of People:', bg='#EEDFCC', font=('arial', 14, 'normal')).place(x=68, y=246)

# Listbox
tip_input=Listbox(root, bg='#EEDFCC', font=('arial', 14, 'normal'), width=0, height=0)
tip_input.insert('0', '10')
tip_input.insert('1', '15')
tip_input.insert('2', '20')
tip_input.place(x=98, y=156)







# Submit Button
Button(root, text='GO!', bg='#EEDFCC', font=('arial', 14, 'normal'), command=btnClickFunction).place(x=168, y=316)



root.mainloop()