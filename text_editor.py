from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename

screen =Tk()
screen.title("Text Editor")

txt= Text(screen, fg="purple", bg="light yellow", font='Calibri 15')
txt.pack()

def open_file():
    filepath=askopenfilename(filetypes=[('text file', '*.txt')])
    if not filepath:
        return
    txt.delete('1.0',END)
    with open(filepath, mode='r', encoding='utf-8') as input_file:
        text = input_file.read()
        txt.insert(END, text)
        screen.title(f'Simple Text Editor - {filepath}')
        
def save_file():
    Filepath= asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files','*.txt')])
    if not Filepath:
        return
    with open(Filepath, mode='w', encoding='utf-8') as output_file:
        text= txt.get('1.0', END)
        output_file.write(text)
        screen.title(f'Simple Text Editor - {Filepath}')
        

menu = Menu(screen)
screen.config(menu=menu)
filemenu= Menu(menu)


menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save as', command=save_file)


screen.mainloop()