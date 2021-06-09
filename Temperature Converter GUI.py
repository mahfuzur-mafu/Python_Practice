import tkinter as tk
from functools import partial
 
 
 
#app gui
root=tk.Tk()
root.configure(bg='#ebcf34')

tempVal="Celsius"
 
#getting dropdownbox
def store_temp(sel_temp):
    global tempVal
    tempVal=sel_temp
 
#main conversion
def call_convert(rlabel1, rlabel2,inputn):
    tem=inputn.get()
    if tempVal == 'Celsius':
        f = float((float(tem) * 9 / 5) + 32)
        k = float((float(tem) + 273.15))
        rlabel1.config(text="%.2f Fahrenheit" % f)
        rlabel2.config(text="%.2f Kelvin" % k)
    if tempVal == 'Fahrenheit':
        c = float((float(tem) - 32) * 5 / 9)
        k = c + 273
        rlabel1.config(text="%.2f Celsius" % c)
        rlabel2.config(text="%.2f Kelvin" % k)
    if tempVal == 'Kelvin':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        rlabel1.config(text="%.2f Celsius" % c)
        rlabel2.config(text="%.2f Fahrenheit" % f)
    return
 
 
#label data entry
numberInput=tk.StringVar()
var=tk.StringVar()
 
 
input_label=tk.Label(root,text="Enter temperature")
input_entry=tk.Entry(root,textvariable=numberInput)
input_label.grid(row=0, column=0)
input_entry.grid(row=0,column=1)
#dropdownbox
dropDownList=["Celsius","Fahrenheit"," Kalvin"]

dropDown=tk.OptionMenu(root,var,*dropDownList,command=store_temp)
var.set(dropDownList[0])
dropDown.grid(row=0, column=2)

 
#resultdata
 
result_label1=tk.Label(root)
result_label2=tk.Label(root)
result_label1.grid(row=2, column=1)
result_label2.grid(row=3,column=1)
 
 
 
#button 
 
call_convert=partial(call_convert,result_label1,result_label2,numberInput)
result_button=tk.Button(root,text="Convert",command=call_convert)
result_button.grid(row=1, column=1)
 
 
 
root.mainloop()

