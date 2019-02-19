import tkinter as tk

class Tela(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.oi = tk.Button(self)
        self.oi['text'] = 'OI THAMARA\nclique em mim'
        self.oi['command'] = self.frase
        self.oi.pack(side='top')

        self.sair = tk.Button(self, text='SAIR', fg='violet', command=root.destroy)
        self.sair.pack(side='bottom')

    def frase(self):
        print('ME AJUDA A TE DAR O MUNDO')

root = tk.Tk()
app = Tela(master=root)
app.mainloop()