import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert


app = ctk.CTk()


app.geometry('500x500')

def selectFile():
    global files
    files = filedialog.askopenfilenames(
        title='Select',
        filetypes=[('Docx files', '*.docx')]
    )
    text = ''
    for file in files:
        a = file.rfind('/')  
        text+= f'\n{file[a+1: -5]}'
    label.configure(text=f'Selected file {text}')


def convertFile():
    label.configure(text='Converting')
    for file in files:
        a = file.rfind('/')
        convert(file, f'{file[0:a+1]}{file[a+1: -5]}.pdf')
    label.configure(text='Converted')

btnSelect = ctk.CTkButton(app, text='Select file', fg_color='#008cff', hover_color='#008cff', command=selectFile)
btnSelect.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

btnConvert = ctk.CTkButton(app, text='Convert', fg_color='red', hover_color='red', command=convertFile)
btnConvert.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

label = ctk.CTkLabel(app, text='Selected file \nfvfv')
label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)



app.mainloop()
