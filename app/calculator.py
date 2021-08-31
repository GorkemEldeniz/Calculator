import tkinter  as tk



root=tk.Tk()
root.geometry("406x207")
root.resizable(False,False) 
root.title("CALCULATOR")
root.configure(bg="orange")


calculation=""

def Eval():
    global calculation
    try:
        result=str(eval(calculation))
        calculation=""
        entry.delete(0,"end")
        entry.insert(0,result)    

    except:
        tk.messagebox.showerror(title="HATA", message="Hatalı Veri Girişi Yaptınız..")     



def Gönder(symbol):
    global calculation
    calculation+=str(symbol)
    entry.delete(0,"end")
    entry.insert(0,calculation)

def temizle():
    global calculation
    calculation=""
    entry.delete(0,"end")


entry=tk.Entry(root,bd=10,font="Raleway 15",width=35,justify=tk.CENTER)
entry.grid(columnspan=4,row=0)

buton=tk.Button(root,bd=3,text="0",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(0))
buton.grid(column=0,row=1)

buton1=tk.Button(root,bd=3,text="1",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(1))
buton1.grid(column=1,row=1)

buton2=tk.Button(root,bd=3,text="2",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(2))
buton2.grid(column=2,row=1)

buton3=tk.Button(root,bd=3,text="+",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder("+"))
buton3.grid(column=3,row=1)

buton4=tk.Button(root,bd=3,text="3",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(3))
buton4.grid(column=0,row=2)

buton5=tk.Button(root,bd=3,text="4",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(4))
buton5.grid(column=1,row=2)

buton6=tk.Button(root,bd=3,text="5",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(5))
buton6.grid(column=2,row=2)

buton7=tk.Button(root,bd=3,text="-",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder("-"))
buton7.grid(column=3,row=2)

buton8=tk.Button(root,bd=3,text="6",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(6))
buton8.grid(column=0,row=3)

buton9=tk.Button(root,bd=3,text="7",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(7))
buton9.grid(column=1,row=3)

buton10=tk.Button(root,bd=3,text="8",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(8))
buton10.grid(column=2,row=3)

buton11=tk.Button(root,bd=3,text="x",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder("*"))
buton11.grid(column=3,row=3)

buton12=tk.Button(root,bd=3,text="9",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder(9))
buton12.grid(column=0,row=4)

buton13=tk.Button(root,bd=3,text="=",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Eval())
buton13.grid(column=1,row=4)

buton14=tk.Button(root,bd=3,text="DELETE",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:temizle())
buton14.grid(column=2,row=4)


buton15=tk.Button(root,bd=3,text="/",width=5,bg="#3D0E09",font="Raleway 14",padx=15,fg="orange",command=lambda:Gönder("/"))
buton15.grid(column=3,row=4)

root.mainloop()
