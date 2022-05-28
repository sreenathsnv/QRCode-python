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




root.mainloop()