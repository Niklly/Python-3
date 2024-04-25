primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))

if primeiro < segundo < terceiro or primeiro < terceiro < segundo:
    print('O menor número foi: {}'.format(primeiro))
if segundo < primeiro < terceiro or segundo < terceiro < primeiro:
    print('O menor número foi: {}'.format(segundo))
if terceiro < primeiro < segundo or terceiro < segundo < primeiro:
    print('O menor número foi: {}'.format(terceiro))


if primeiro > segundo > terceiro or primeiro > terceiro > segundo:
    print('O maior número foi: {}'.format(primeiro))

if segundo > primeiro > terceiro or segundo > terceiro > primeiro:
    print('O maior número foi: {}'.format(segundo))

if terceiro > primeiro > segundo or terceiro > segundo > primeiro:
    print('O maior número foi: {}'.format(terceiro))


'''
eu posso definir menor = a, e começar a testar:

ex: if b<a and b<c: logo b = menor. 
ex: if c<a and c<b: logo c = menor.
Assim, eu faço com o maior também. Logo posso diminuir o código.


'''
