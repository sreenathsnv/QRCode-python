from tkinter import *
import qrcode


#GUI for the app

root = Tk()

# globlal variables
url_var = StringVar()
bg_color,tcolor = "#112b3c","#ffffff"


root.geometry("400x500")
root.resizable(width=False,height= False)
root.title("QRcode Generator")
root.config(background="#112b3c")



# -------------------title section --------------------------

Ftitle  = Frame(master= root,width= 400,height=75,bg = bg_color)
Ftitle.pack(fill=X,ipady=5)

title = Label(master=Ftitle,text = "QRcode!!",font=("Segoe UI Black",30),fg = "#fff89a",bg = bg_color)
title.pack()

# ---------------------------USER INPUT -------------------------------------

U_frame = Frame(master=root,width = 400,height = 50, background = bg_color)
U_frame.pack(fill=Y,ipady=10)

url_label = Label(master = U_frame,text = "URL : ",fg = tcolor,bg = bg_color,font = ("Segoe UI Black",16,))
url_label.pack(padx=9,side='left')

url = Entry(master=U_frame,text = "Enter the url",font=("Segoe UI",10),relief=RIDGE,width = 30,justify= 'left',textvariable = url_var)
url.pack(ipadx = 10,padx=1,side = 'left')

submit = Button(master = U_frame, text = "Submit",fg = bg_color,bg = "#ffc900",relief='groove',font = ("Segoe UI bold",10,'bold'),
                command= None)
submit.pack(side = 'right',padx = 1)


#----------------- Qr part--------------------------------
root.mainloop()