def funçao(L, i=0, R = []):
    if i >= len(L):
        return R
    else:
        if L[i] in R:
            return funçao(L, i+1, R)
        return funçao(L, i+1, R +[L[i]])

def main():
    l1 = [1,3,3,5,7,9,9,9]
    print(funçao(l1))

main()