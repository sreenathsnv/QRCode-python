import qrcode as q
from PIL import Image , ImageTk
from tkinter import *
from tkinter import messagebox



#functions for the app


#GUI for the app

root = Tk()

def qr_generator(url):
    if url == '':
        messagebox.showwarning("WARNING.!!","The field is required")
    else:
        qr = q.QRCode(
            version = 1,
            error_correction=q.ERROR_CORRECT_L,
            box_size=10,
            border=1
        ) 
        qr.add_data(url)
        qr.make(fit =True)
        img = qr.make_image(fill_color = 'black',back_color= 'white')
        img.save('qrcode.png')
        qr_img = ImageTk.PhotoImage(img)
        img_label.config(image=qr_img)
    print("success")

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
                command= lambda : qr_generator(str(url_var.get())))
submit.pack(side = 'right',padx = 1)


#----------------- Qr part--------------------------------


Q_frame = Frame(master = root,width = 400,height = 100, background = bg_color)
Q_frame.pack(fill=X)

img_label = Label(master = Q_frame,width = 300,height = 300,bg = bg_color)
img_label.pack(padx = 10,pady = 2)

save_button = Button(master=Q_frame, text = "Download",fg = bg_color,bg = "#ffc900",relief='flat',font = ("Segoe UI bold",15,'bold'),
                width=50,height=12 ,command= None)
save_button.pack(ipadx=12,padx = 5,pady =5)




root.mainloop()