import customtkinter as ctk
import tkinter as tk


app = ctk.CTk()

app.geometry("400x300")

a = ctk.IntVar(value=0)

def plus():
    a.set(a.get()+1)
    label.configure(text=a.get())

def minus():
    a.set(a.get()-1)
    label.configure(text=a.get())

def reset():
    a.set(0)
    label.configure(text=a.get())

label = ctk.CTkLabel(app, text=0)
label.place(relx=0.5, rely=0.3, anchor = tk.CENTER)

frame = ctk.CTkFrame(app, width=300, height=60)
frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
# Minus Button 
btn = ctk.CTkButton(master=frame, text='+', bg_color='green', width=50, command=plus)
btn.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
btn.pack(padx=10, pady=6)

# Reset Button
btn1 = ctk.CTkButton(master=frame, text='reset', bg_color='green', width=50, command=reset)
btn1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
btn1.pack(padx=10, pady=6)

# Plus Button
btn2 = ctk.CTkButton(master=frame, text='-', bg_color='green', width=50, command=minus)
btn2.place(relx=0.7, rely=0.1, anchor=tk.CENTER)
btn2.pack(padx=10, pady=6)


app.mainloop()