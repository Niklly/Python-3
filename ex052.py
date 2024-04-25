print('\033[34m{:*^30}\033[m'.format('É PRIMO OU NÃO É'))
n = int(input('Digite um número inteiro: '))
for c in range(1):
    if n == 2 or n == 3 or n == 7 or n == 5:
        print('\033[34mÉ primo.\033[m')
    elif n % 2 == 0:
        print('\033[31mNão é primo, mas é múltiplo de 2.\033[m')
    elif n % 3 == 0:
        print('\033[31mNão é primo, mas é múltiplo de 3.\033[m')
    elif n % 5 == 0:
        print('\033[31mNão é primo, mas é múltiplo de 5.\033[m')
    elif n % 7 == 0:
        print('\033[31mNão é primo, mas é múltiplo de 7.\033[m')
    elif n == 1:
        print('\033[33mEsse número não é primo, pois ele só tem um divisor(que é ele).\033[m')
    else:
        print('\033[34mÉ primo.\033[m')



'''para ser número primo ele precisa SÓ PODE SER DIVISÍVEL POR ELE MESMO E POR UM
# EXCLUIR OS MÚLTIPLOS DE 2,3,5,7
# DIVISEIS POR 2 SÃO PARES, NÃO POD TERMINAR EM 2,4,6,8,0
# DIVISIVEIS POR 3, A SOMA DOS ALGARISMOS = VAI SER MULTIPLO DE 3
# DIVISIEVIS POR 5: NÃO PODE TERMINAR EM 0 OU 5

FORMULA DOS MÚLTILOS: M = 2 * K'''