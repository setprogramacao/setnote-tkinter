import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk

class SetNote:
    #Inicializando a nossa janela
    __root = Tk()

    #Configuracoes iniciais de nosso bloco de notas
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root, pady=10, padx=10, wrap='word', font=('Consolas 12'))
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisViewMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None


    def __init__(self, **kwargs):

        #set icon
        try:
            self.__root.wm_iconbitmap('snote.ico')
        except:
            pass

        #configurando o tamanho da tela (300x300)
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        self.__root.title('Sem titulo - SetNote')

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__thisTextArea.grid(sticky=N + E + S + W)

    #----------------File menu-------------------
        self.__thisFileMenu.add_command(label='Novo', command=self.__newfile)

        self.__thisFileMenu.add_command(label='Abrir', command=self.__openFile)

        self.__thisFileMenu.add_command(label='Salvar', command=self.__saveFile)

        self.__thisFileMenu.add_separator()

        self.__thisFileMenu.add_command(label='Sair', command=self.__quitApplication)

        self.__thisMenuBar.add_cascade(label='Ficheiro', menu=self.__thisFileMenu)

    #----------------Edit Menu----------------------
        self.__thisEditMenu.add_command(label='Cortar', command=self.__cut)

        self.__thisEditMenu.add_command(label='Copiar', command=self.__copy)

        self.__thisEditMenu.add_command(label='Colar', command=self.__paste)

        self.__thisMenuBar.add_cascade(label='Editar', menu=self.__thisEditMenu)
    
    #---------------- Help Menu ---------------------------
        self.__thisHelpMenu.add_command(label='Sobre Aplicação', command=self.__showAbout)

        self.__thisMenuBar.add_cascade(label='Ajuda', menu=self.__thisHelpMenu)

    #------- Mostrar menu e scrollBar na tela---------
        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    #--------Funcoes de menu ficneiro---------------------
    def __newfile(self):
        self.__root.title('Sem titulo - SetNote')
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __openFile(self):
        self.__file = askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

        if self.__file == '':
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + ' - SetNote')
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, 'r')
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Sem titulo', defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

            if self.__file == '':
                self.__file = None
            else:
                file = open(self.__file, 'w')
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                self.__root.title(os.path.basename(self.__file) + ' - SetNote')

        else:
            file = open(self.__file, 'w')
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()


    def __quitApplication(self):
        self.__root.destroy()

    #---------- Funcoes do menu editar---------------
    def __cut(self):
        self.__thisTextArea.event_generate('<<Cut>>')

    def __copy(self):
        self.__thisTextArea.event_generate('<<Copy>>')

    def __paste(self):
        self.__thisTextArea.event_generate('<<Paste>>')

    #------------ Funcoes do Help Menu -----------------
    def __showAbout(self):
        showinfo('Informacao do Software - SetNote', 'Versão: 1.0.0\nLicença: Grátis\nDesenvolvedor: @setprogramacao')

    def run(self):
        self.__root.mainloop()

note = SetNote(width=600, height=400)
note.run()