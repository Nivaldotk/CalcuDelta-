def delta(a, b, c):
    r = ((a ** 2) - 4 * a* c)
    return r

a = int(input("Digite o valor de B"))
b = int(input("Digite o valor de A"))
c = int(input("Digite o valor de C"))
print("O resultado de Delta é ", delta(a, b, c))
