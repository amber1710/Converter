from tkinter import *

def testing():
   my_name=("Amber")
   mytextbox.insert(0,my_name)
   return None
   my_surname=("Adonis")
   mytextbox.insert(0,my_surname)
   return None
   my_result=("Positive")
   mytextbox.insert(0,my_result)
   return None

mywindow=Tk()

mywindow.title("Forms")

mywindow.geometry("500x400")

mywindow.configure(background="light blue")

theLabel=Label(mywindow, text="First Number",relief="solid")
theLabel1=Label(mywindow, text="Surname",relief="solid")
theLabel2=Label(mywindow, text="Result",relief="solid")
theLabel.pack()

my_name=mytextbox= Entry(mywindow,width=40)
my_surname=mytextbox=Entry(mywindow,width=40)
my_result=mytextbox= Entry(mywindow,width=40)

mytextbox.pack()

my_button=Button(mywindow,text="Clear",bg="light green",command=testing)

my_button=Button(mywindow,text="Add", bg="yellow" , command=testing)
my_button.pack()

mywindow.mainloop()




