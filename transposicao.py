#! python3
# -*- coding: utf-8 -*-

'''Implementação de Cifra de Transposição
Segurança da Informação - UFF/2016-1 - Prof. Antonio Rocha
Aluno: Radamés Aragón'''

import argparse

parser = argparse.ArgumentParser(description='Programa para cifrar ou decifrar mensagem com Algoritmo de Transposição e chave (k)',
                                 epilog='Prova Surpresa 2 - Segurança da Informação UFF 2016-1 - Aluno: Radamés Aragón')
parser.add_argument('-c', '--cifrar', dest='texto_claro', required=False, help='Tipo de Operação: Cifrar')
parser.add_argument('-d', '--decifrar', dest='texto_cifrado', required=False, help='Tipo de Operação: Decifrar')
parser.add_argument('chave', help='Chave usada para cifrar ou decifrar o texto')
args = parser.parse_args()


def valida_chave(chave):
    try:
        colunas = list()
        for n in chave:
            colunas.append(int(n))

        colunas_ordenadas = sorted(colunas)
        for i in range(1, len(chave)):
            if i != colunas_ordenadas[i-1]:
                print(colunas_ordenadas)
                raise ValueError()

        return colunas

    except ValueError as e:
        raise Exception('Chave precisa conter somente números sequenciais a partir de 1 (não ordenados)')


def texto_matriz(texto, num_colunas):
    matriz = list('' for x in range(num_colunas))
    y = 0
    for c in texto:
        if y == num_colunas:
            y = 0
        matriz[y] += c
        y += 1
    return matriz


def cifra(texto, chave):
    complemento = len(texto) % len(chave)
    if complemento > 0:
        texto = texto.ljust(len(texto) + len(chave) - complemento)

    matriz = texto_matriz(texto, len(chave))
    print(matriz)

    matriz_reordenada = [matriz[x - 1] for x in chave]
    return ''.join(matriz_reordenada)


def decifra(cifrado, chave):
    if (len(cifrado) % len(chave)) > 0:
        raise Exception('Texto cifrado não pode ser decifrado com essa chave')

    n = len(cifrado)/len(chave)
    matriz_cifrada = [cifrado[i:i+n] for i in range(0, len(cifrado), n)]
    print(matriz_cifrada)

    result = ''
    for y in range(n):
        result += ''.join([matriz_cifrada[x - 1][y:y+1] for x in chave])

    return result


if __name__ == '__main__':
    try:
        if not args.texto_claro and not args.texto_cifrado:
            raise Exception('Programa requer parâmetro [-c] ou [-d] para definir Operação')

        colunas = valida_chave(args.chave)

        if args.texto_claro:
            result = cifra(args.texto_claro, colunas)
        else:
            result = decifra(args.texto_cifrado, colunas)

        print('Resultado: "%s"' % result)
        exit()

    except Exception as e:
        print('Erro: %s %s' % (e, type(e)))
        exit(1)
