
# sudoku

Algoritmo para resolver Sudoku

**Método Escolhido: Backtracking**  
Backtracking é um tipo de algoritmo que representa um refinamento da busca
por força bruta, em que múltiplas soluções podem ser eliminadas sem serem explicitamente examinadas.

**Como esse método funciona**  
A árvore é percorrida sistematicamente de cima para baixo e da esquerda para direita. Quando essa pesquisa falha, ou é encontrado um nodo terminal da árvore, entra em funcionamento o mecanismo de backtracking. Esse procedimento faz com que o sistema retorne pelo mesmo caminho percorrido com a finalidade de encontrar soluções alternativas

**Linguagem utilizada: Python**  
  
**Como executar**   
Para a execução do do algoritmo, o estado inicial do tabuleiro do jogo sudoku deve ser lido de um arquivo *.txt. Como o tabuleiro contém 81 posições, o arquivo deve conter 81 dígitos, cada um correspondendo ao valor de uma das posições do tabuleiro. 
Os valores “0” do arquivo, correspondem às posições vazias no tabuleiro inicial e, portanto, correspondem às posições cujos valores devem ser encontrados pelo agente. A variável '*path*' deverá receber o endereço do arquivo *.txt de entrada.

**Exemplo**    
**Entrada**(Estado Inicial): 530070000600195000098000060800060003400803001700020006060000280000419005000080079

**Saída**(Estado Final): [[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]