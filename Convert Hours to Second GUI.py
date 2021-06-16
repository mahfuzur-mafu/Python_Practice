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
def call_convert(rlabel1, inputn):
 hours = inputn.get()
 seconds = int(hours) * 60 * 60
 rlabel1.config(text="%d sec" % seconds)
 return


#label data entry


numberInput = tk.StringVar()
var = tk.StringVar()
input_label=tk.Label(root,text="Enter   Hours")
input_entry=tk.Entry(root,textvariable=numberInput)
input_label.grid(row=0)
input_entry.grid(row=0,column=1)


#result

input_label = tk.Label(root)
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=0)
input_entry.grid(row=0, column=1)

result_label1 = tk.Label(root)
result_label1.grid(row=2, column=1)

call_convert = partial(call_convert, result_label1, numberInput)
result_button = tk.Button(root, text="Convert", command=call_convert)
result_button.grid(row=0, column=4)

root.mainloop()
