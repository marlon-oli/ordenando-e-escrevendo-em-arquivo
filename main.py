from auxiliares import *

def main():

#abrindo dicionario
	dicionario = abrirArquivo(escolha())

#criando lista de matriculas
	matriculas = []
	for matricula in dicionario:
		matriculas.append(matricula)

#ordenando
	dualPivotQuickSort(matriculas, dicionario, 0, len(matriculas)-1)

#escrevendo no arquivo de forma ordenada
	escreva(matriculas, dicionario)

	print("\nArquivo saida.txt atualizado com a quantidade de alunos informada!")
	print(fim-inicio)

if __name__ == '__main__':
	main()
