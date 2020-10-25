from tkinter import *
root=Tk()

def sub():
	print("name", f"{user.get(), age.get(), gender.get(), mobile.get()}")
	with open("atul.txt", "a") as f:
		f.write(f"{user.get(), age.get(), gender.get(), mobile.get()}\n")

Label(root, text="username").grid()
Label(root, text="age").grid(row=1, column=0)
Label(root, text="gender").grid(row=2, column=0)
Label(root, text="mobile").grid(row=3, column=0)
user=StringVar()
age=StringVar()
gender=StringVar()
mobile=StringVar()

user1=Entry(text="username", textvariable=user).grid(row=0, column=2)
age1=Entry(text="username", textvariable=age).grid(row=1, column=2)
gender1=Entry(text="username", textvariable=gender).grid(row=2, column=2)
mobile1=Entry(text="username", textvariable=mobile).grid(row=3, column=2)
Button(root, text="subbmite", command=sub).grid(row=4, column=0)
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.grid(row=5, column=2,)


root.mainloop()