print("_"*35)
print("101 - Batata list                - R$4.50")
print("305 - Suco pay                   - R$2.00")
print("248 - Suco importado             - R$4.25")
print("389 - Guarana lambda             - R$3.50")
print("145 - Sanduiche integral         - R$9.00")
print("567 - Cerveja derivada           - R$8.50")
print("673 - Vitamina Compilada         - R$7.80")
print("_"*35)

produto = int(input("Escolha o seu produto:"))
SemErro = True
codigos = 101; 305; 248; 389; 145; 567; 673

if produto == 101:
    print("Batata List                - R$4.50")
    SemErro = False
elif produto == 305:
    print("Suco Pay                   - R$2.00")
    SemErro = False
elif produto == 248:
    print("Suco Importado             - R$4.25")
    SemErro = False
elif produto == 389:
    print("Guarana lambda             - R$3.50")
    SemErro = False
elif produto == 145:
    print("Sanduiche integral         - R$9.00")
    SemErro = False
elif produto == 567:
    print("Cerveja derivada           - R$8.50")
    SemErro = False
elif produto == 673:
    print("Vitamina Compilada         - R$7.80")
    SemErro = False

if SemErro:
    print("Produto nao identificado.")