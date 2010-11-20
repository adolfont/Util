#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Aplicação gráfica que usa a aplicação sorteio.py
from Tkinter import *
from sorteio import *
import locale

class SorteioGrafico(Frame):
    def sorteia_proximo(self):
       self.message = sorteia(self.myfile)
#       print self.message
       self.BOTAO_ALUNO["text"] = self.message
       self.BOTAO_ALUNO.pack()


    def createWidgets(self):
        self.BOTAO_ALUNO = Button(self)
        self.BOTAO_ALUNO["text"] = self.message
        self.BOTAO_ALUNO["fg"]   = "red"
        self.BOTAO_ALUNO["command"] =  self.BOTAO_ALUNO
        self.BOTAO_ALUNO["height"] =  3
        self.BOTAO_ALUNO["width"] =  70
        self.BOTAO_ALUNO["font"] =  ("Times", 25, "bold")
        self.BOTAO_ALUNO.pack({"side": "left"})

        self.BOTAO_PROXIMO = Button(self)
        self.BOTAO_PROXIMO["text"] = "Próximo",
        self.BOTAO_PROXIMO["command"] = self.sorteia_proximo
        self.BOTAO_PROXIMO["font"] =  ("Times", 15, "normal")
        self.BOTAO_PROXIMO.pack({"side": "left"})

    def __init__(self, master=None, message=None, myfile=None):
        Frame.__init__(self, master)
        self.pack()
        self.message=message
        self.myfile=myfile
        self.createWidgets()

def main():

	locale.setlocale(locale.LC_CTYPE, ('pt_BR', 'iso8859-1'))

	if len(sys.argv) < 2:
		print "Deve haver um segundo argumento: o nome do arquivo"
		exit(0)
	arquivo=sys.argv[1]
 
	root = Tk()
	root.title("Sorteio de Alunos - DAINF - UTFPR")
	mensagem = "Clique em \'Próximo\" para sortear um(a) aluno(a)"
	app = SorteioGrafico(master=root, message=mensagem, myfile=arquivo)
	app.mainloop()

if __name__ == "__main__":
	main()

