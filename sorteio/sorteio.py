#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# sorteio.py - programa para sortear nomes de alunos de arquivos de alunos extraídos
# a partir de copiar-colar página de preenchimento de presença do sistema acadêmico da UTFPR

import random
import sys

def juntaApenasStrings(lista):
	return [ item  for item in lista if item.isalpha() ]


def procura(arquivo,sortudo):
	arquivo = open(arquivo)

	for linha in arquivo:
		numero = linha[0:2]

		if int(numero)==sortudo:
			return " ".join(juntaApenasStrings(linha.split()))

def verificaSituacaoAluno(nomeAluno, situacao):
	try:
			nomeAluno.index(situacao)
			return False
	except(ValueError), ex:
			return True
	
def alunoFrequenta(aluno):
		return verificaSituacaoAluno(aluno, "Trancado")    \
						and verificaSituacaoAluno(aluno, "Consignado")  \
						and verificaSituacaoAluno(aluno, "Cancelado")  \
						and verificaSituacaoAluno(aluno, "Desistente")


def sorteia(arquivo):

	random.seed()

	linhas = len(file(arquivo).readlines())

	while True:
		sortudo = 1+int(random.random()*linhas)
		alunoSortudo = procura(arquivo,sortudo)
#		print "DEBUG - aluno sorteado: ",  alunoSortudo
		if alunoFrequenta(alunoSortudo):
			return "A(O) aluna(o) de sorte é " + alunoSortudo

def main():
	if len(sys.argv) < 2:
		print "Deve haver um segundo argumento: o nome do arquivo"
		exit(0)

	arquivo=sys.argv[1]
 
	print sorteia(arquivo)

if __name__ == "__main__":
	main()
