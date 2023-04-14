import functions

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

print(f"Liste utilisée :\n{L[:]}")
print(f"\nNombres conformes à l'interval [25, 90] :\n{functions.GetValuesToCalculate(L)}")
print(f"\nRésultat du produit des nombres : {functions.GetProduct(L)}")