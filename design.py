import tkinter as tk
window=tk.Tk()
window.geometry("1000x800")
window.title("Hello Tkinter")
window.resizable(False,False)

def first_print():
    text="Hello World"
    text_output=tk.Label(window,text=text,fg="red",font= ("Helvetica",16))
    text_output.grid(row=0,column=1)
def second_print():
    text="NUOVO MESSAGGIO BROA"
    text_output=tk.Label(window,text=text,fg="green")
    text_output.grid(row=1,column=1,padx=100)
first_button=tk.Button(text="Saluta",command=first_print)
first_button.grid(row=0,column=0)

second_button=tk.Button(text="Hello",command=second_print)
second_button.grid(row=1,column=1)



if __name__ == "__main__":
    window.mainloop()
   