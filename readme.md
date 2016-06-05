# Implementação de Cifra de Transposição

## Segurança da Informação - UFF/2016-1 - Prof. Antonio Rocha

Programa para cifrar e decifrar com algoritmo de Transposição.

#### Para cifrar:

`>python transposicao.py -c {texto_claro} {chave}`
* __texto_claro__: palavra ou texto (entre aspas "") para cifrar
* __chave__: chave para cifrar (necessária para decifrar)

> Caso a palavra ou texto possua um número de caracteres não divisível pelo tamanho da chave, espaços vazios serão adicionados para compor a matriz de colunas.

#### Para decifrar:

`>python transposicao.py -d {texto_cifrado} {chave}`
* __texto_cifrado__: palavra ou texto cifrado (entre aspas "") para decifrar
* __chave__: chave para decifrar

> A entrada (texto_cifrado) para decifrar precisa ter um número divisível de caracteres pelo tamanho da chave.
