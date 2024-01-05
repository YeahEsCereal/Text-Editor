import os
from tkinter import *
from tkinter import filedialog

def openFile():
    file = filedialog.askopenfilename(defaultextension = ".txt",
                                title = "Open",
                                file = [
                                    ("Text File", "*.txt"),
                                    ("All Files", "*.*")
                                ])
    try:
        window.title(os.path.basename(file))
        text.delete(1.0, END)
        file = open(file, "r")
        text.insert(1.0, file.read())
    except:
        print("Error while opening")
        window.title("Untitled")
    finally:
        file.close()
    

def saveFile():
    file = filedialog.asksaveasfilename(initialfile = "Untitled.txt",
                                        defaultextension = ".txt", 
                                        title = "Save",
                                        filetypes = [
                                            ("Text File", ".txt"),
                                            ("All Files", ".*")
                                        ])
    if file == None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text.get(1.0, END))
        except:
            print("Error while saving")
            window.title("Untitled")

window = Tk()
window.title("Untitled")
window.geometry("500x500")

menuBar = Menu(window)
window.config(menu = menuBar)

fileMenu = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Open", command = openFile, font = ("Arial", 10))
fileMenu.add_command(label = "Save", command = saveFile, font = ("Arial", 10))

text = Text(window, font = ("Arial", 20))
text.pack()

scrollBar = Scrollbar(window)
scrollBar.pack(side = RIGHT, fill = Y)
text.config(yscrollcommand = scrollBar.set)

window.mainloop()
