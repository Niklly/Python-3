preço = float(input('Olá, qual o preço dessa roupa? R$'))
# 10& de 1500 == 1500*10/100
desconto = preço * 0.05
reajuste = preço - desconto
print('A roupa está com um desconto de 5%, logo sai por {:.2f}'.format(reajuste))
