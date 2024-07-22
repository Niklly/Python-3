def todosnumeros(L, i=0, cont = 0): 
    if i < len(L):
        if type(L[i]) == int or type(L[i]) == float:
           return todosnumeros(L, i + 1,cont+1)
        else:
            return todosnumeros(L,i+1,cont)
    
    else :
        if(cont == len(L)):
            return True
        else:
            return False
    
def main():
    l1 = [1,2,3,4]
    print(todosnumeros(l1))
    
main()
