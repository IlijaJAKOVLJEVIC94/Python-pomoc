
from tkinter import *
import os

	

def shoping():
	
	def pice():
		fh=open('menu.txt')
		cita=fh.readlines()
		fh.close()
		rec=[st.rstrip() for st in cita]
		list1.delete(0,END)
		for i in rec:
			list1.insert(END,i)
	def hrana():
		fh=open('menu1.txt')
		cita=fh.readlines()
		fh.close()
		rec=[st.rstrip() for st in cita]
		list1.delete(0,END)
		for i in rec:
			list1.insert(END,i)
		
		
	screen3.destroy()
	screen2.destroy()
	
	global screen6
	
	def zakredit():
		list_of_files = os.listdir()
		fh=open(username1, 'r')
		if username1 in list_of_files:
			cita=fh.readlines()
			fh.close()
			rec=[st.rstrip() for st in cita]
			ImeKupac.delete(0,END)
			for i in rec[0]:
				ImeKupac.insert(END,i)
	

		
	screen6 = Toplevel(screen)
	screen6.title("Prodavnica")
	screen6.geometry("600x300")
	
	
	Kupac=Label(screen6,text="Kupac: ")
	Kupac.grid(row=0,column=0)
	ImeKupac=Label(screen6)
	ImeKupac.grid(row=0,column=1)
	
	Kredit=Label(screen6,text="Kredit: ")
	Kredit.grid(row=1,column=0)
	
	Dinara=Label(screen6,textvariable=zakredit)
	Dinara.grid(row=1,column=1)
	
	Prazan=Label(screen6,text=" ")
	Prazan.grid(row=2,column=0)
	
	Prazan=Label(screen6,text=" ")
	Prazan.grid(row=3,column=0)
	
	
	list1=Listbox(screen6,width=30,height=10)
	list1.grid(row=4,column=0,rowspan=6,sticky=N)
	yscroll=Scrollbar(screen6,command=list1.yview,orient=VERTICAL)
	yscroll.grid(row=4,column=1,rowspan=6,sticky=N+S)
	list1.configure(yscrollcommand=yscroll.set)
	
	def dodaj(ev=0):
		st=Prikaz.get()+"*"+Kolicina.get()
		list2.insert(END,st)
	def edit():
		to=list2.curselection()[0]
		st=list2.get(to)
		list2.delete(to)
		
		pos=st.find('*')
		
		Prikaz.delete(0,END)
		Prikaz.insert(0,st[0:pos].strip())
		
		Kolicina.delete(0,END)
		Kolicina.insert(0,st[pos+1:].strip())
	def delete():
		try:
			to=list2.curselection()[0]
			list2.delete(to)
		except:
			pass
	def select(self):
		to=list1.curselection()[0]
		st=list1.get(to)
		
		Prikaz.delete(0,END)
		Prikaz.insert(0,st)
		
		Kolicina.delete(0,END)
		Kolicina.insert(0,"1")
	def sumcena():
		
		label3=Label(screen6,i)
		label3.grid(row=5,column=5)
	def uplata():
		global screen7
		screen7= Toplevel(screen)
		screen7.title("Uplata")
		screen7.geometry("200x80")
		Label(screen7,text="Unesite iznos koji zelite da uplatite").pack()
		unesen=Entry(screen7).pack()
		Button(screen7,text="Uplati",command=uplaceno).pack()
	def uplaceno():
		global screen8
		screen8= Toplevel(screen)
		screen8.title("Uplaceno")
		screen8.geometry("100x60")
		screen7.destroy()
		Label(screen8,text="Uplaceno je").pack()
		Button(screen8,text="OK",command=delete8).pack()
	def delete8():
		screen8.destroy()
	
	Hrana=Button(screen6,text="Hrana",command=hrana,width=5).grid(row=2,column=0)
	Pice=Button(screen6,text="Pice",command=pice,width=5).grid(row=3,column=0)
	Unesi=Button(screen6,text="Unesi",command=dodaj,width=5)
	Unesi.grid(row=3,column=5)
	Izmeni=Button(screen6,text="Izmeni",command=edit,width=5)
	Izmeni.grid(row=4,column=5)
	Delete=Button(screen6,text="Delete",command=delete,width=5)
	Delete.grid(row=5,column=5)
	kupi=Button(screen6,text="Kupi",command=sumcena,width=5)
	kupi.grid(row=6,column=5)
	Prikaz=Entry(screen6,width=25)
	Prikaz.grid(row=2,column=4)
	Kolicina1=Label(screen6,text="Kolicina")
	Kolicina1.grid(row=1,column=5)
	Kolicina=Entry(screen6,width=5)
	Kolicina.grid(row=2,column=5)
	Kolicina.bind('<Return>',dodaj)
	list1.bind('<<ListboxSelect>>',select)
	list2=Listbox(screen6,width=25)
	list2.grid(row=4,column=4,rowspan=6,sticky=N)
	Upnovac=Button(screen6,text="Uplati Novac",command=uplata)
	Upnovac.grid(row=3,column=6)
	
	
		
	
	
def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command =shoping).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Found")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()
  credit_info = credit.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info+"\n")
  file.write(credit_info)
  file.close()
 

  username_entry.delete(0, END)
  password_entry.delete(0, END)
 
  

  Label(screen1, text = "Registration Sucess",bg="black", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  global credit
  global credit_info


  username = StringVar()
  password = StringVar()
  credit = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  
  Label(screen1, text = "Username * ").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  
  Label(screen1, text= " Credit:").pack()
  credit_entry = Entry(screen1, textvariable= credit)
  credit_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Prijavi se")
  Label(text = "Prijavi se", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()
  
