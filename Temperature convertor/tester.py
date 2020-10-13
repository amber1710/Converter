from tkinter import *
#function to create a window
root = Tk()
root.geometry('550x300')
root.title("Conversions")
root.configure(background="turquoise")

#functions to create a label
label = Label(root, text="Press")
label.grid(row=0, column=0, columnspan=3)

label2 = Label(root, text="°Celsius")
label2.grid(row=0, column=0, columnspan=1)

label3 = Label(root, text="°Fahrenheit")
label3.grid(row=0, column=2, columnspan=1)

temp_celsius = Entry(root)
temp_celsius.grid(row=1, column=0)
temp_fahrenhiet = Entry(root)
temp_fahrenhiet.grid(row=1, column=2)

#numbers inserted in entry will convert
def pressed():
    calculations = (int(temp_celsius.get())*9/5)+32
    temp_fahrenhiet.delete(0, END)
    temp_fahrenhiet.insert(0, str(round(calculations,2)) + "°F")

button = Button(root, text="Convert to °F", command=pressed)
button.grid(row=1, column=1)

def pressed2():
    calculations2 = (int(temp_fahrenhiet.get())-32)*5/9
    temp_celsius.delete(0, END)
    temp_celsius.insert(0, str(round(calculations2,2)) + "°C")
#the function for making buttons
button2 = Button(root, text="Convert to °C", command=pressed2)
button2.grid(row=2, column=1)

def clear():
    temp_celsius.delete(0, END)
    temp_fahrenhiet.delete(0, END)

butoon_clear = Button(root, text="CLEAR", command=clear)
butoon_clear.grid(row=3, column=1)

butoon_exit= Button(root, text="EXIT", command=exit)
butoon_exit.grid(row=0, column=3)

root.mainloop()
