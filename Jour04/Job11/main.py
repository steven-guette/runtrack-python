import functions

L = [7, 11, 42, 39, 2]

print(f"Liste utilisée : {L[:]}\n")

for i in range(10):
    functions.IncrementElementsOfList(L)
    print(f"{L[:]}")