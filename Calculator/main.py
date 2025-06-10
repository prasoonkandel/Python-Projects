import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("550x500")
root.maxsize(550,500)
root.minsize(550,500)
style= ttk.Style()
style.configure(
    "TEntry",
    borderwidth=2,
    relief="sunken",
    justify="right" ,

)
style.configure(
    "TButton",
    font=("Montserrat",35),
)  

def validate_input(action,current_val,proposed_val,actual_val):
    return not actual_val.isalpha()

def backspace():
    display_box.delete(len(display_box.get()) - 1, tk.END)
display_box= ttk.Entry(
    root ,
    style="TEntry",
    font=("Montserrat",30),
    justify="right",
    validate="key",
    validatecommand=((
        root.register(validate_input), "%d",
        "%s", "%P","%S"
)))
display_box.grid(row=0, column=0, columnspan=3, sticky="nsew", )
erase= ttk.Button(root,text="⌫", command=backspace)
erase.grid(row=0, column=3, sticky="nsew", )

excludeButtons=("C","=")
def move_cursor():
    display_box.focus_set()  
    display_box.icursor(tk.END) 
    display_box.xview_moveto(1.0) 
def buttonClick(val):
    if val not in excludeButtons:
        display_box.insert(tk.END,val)
        move_cursor()
        root.update()
    if val == "=" :
        errorOccured=False
        try:
           result= round(eval(display_box.get()),2)
           
           
        except:
            errorOccured=True
        else:
            if result>=10**15:
                display_box.delete(0,tk.END)
                display_box.insert(0,"Exceeds limit 10**15")  
                
            else: 
                display_box.delete(0,tk.END)
                display_box.insert(0,str(result))
                display_box.icursor(0)
            
        if errorOccured==True:
            display_box.delete(0,tk.END)
            display_box.insert(0,"Error")  
            move_cursor()
    if val == "C" :
        display_box.delete(0,tk.END)               
keys=(
    ("C","(",")","/"),
    ("7","8","9","*"),
    ("4","5","6","-"),
    ("1","2","3","+"),
    ("0","00",".","="),)
for row in range(0,5):
    for column in range(0,4):
        new_button = ttk.Button(
            root,
            text=f"{keys[row][column]}",

            style="TButton",
            command= lambda x= keys[row][column]:buttonClick(x)
            )
            
        
        new_button.grid(row=row+1 , column=column, sticky="news",)

for i in range(0 ,4):
    root.grid_rowconfigure(i+1, weight=1)
    root.grid_columnconfigure(i, weight=1)
root.mainloop()