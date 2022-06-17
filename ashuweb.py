#importing
import wikipedia

from tkinter import *
from tkinter import messagebox

root = Tk()

root.wm_iconbitmap('wiki.ico')
root.title("Ashuweb")
root.geometry("900x550")
root.resizable(0,0)

#functions
def wiki():
	try:
		query = entry.get()
		result = wikipedia.summary(query)
		text.insert(END,result)
	except Exception as e:
		messagebox.showerror("Error",e)

# Vars
questionvalue = StringVar()

# Body structure
f = Frame(bg="black")

Label(f, text="Saoogle", fg="cyan", bg="black", font="Ds-Digital 40", width=50).pack(pady=15)

entry = Entry(f, textvariable=questionvalue,bg="white", fg="darkblue", font="Lucida 25", width=40)
entry.pack(pady=10)

Button(f, text="Search", bg="black", fg="cyan", activeforeground="cyan", activebackground="black", font="Ds-Digital 20", command=wiki).pack(pady=10)

f.pack()


text = Text(root,font="arial 18",undo=True, bg="black", fg="cyan", padx=40, pady=15)
text.pack(expand=True,fill=BOTH,padx=12)
def exit_func(event=None):
	global file, text_changed
	try:
		if text_changed:
			mbox = messagebox.askyesnocancel("warning", "do you want to save it")
			
			if mbox is True:
				if file:
					with open(file,"w") as op:
						op.write(str(text.get(1.0,END)))
						root.destroy()
				else:

					file = filedialog.asksaveasfile(mode="w",initialdir=os.getcwd(),defaultextension=".txt",
													filetypes=[
														("Text document as",".txt"),
														("All files","*.*")									
													])	
					filetext = str(text.get(1.0,END))
					file.write(filetext)
					file.close()
			else:
				root.destroy()	
	except Exception as w:
		pass

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()