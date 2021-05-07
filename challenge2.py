##CODE CHALLENGE: CREATE THREE LISTS. CREATE A FOURTH LIST WITH NO ELEMENTS. USING LOOPS, ADD THE ELEMENTS OF ALL THREE LISTS TO THE FOURTH LIST. PUSH THIS TO YOUR REPO.

grocerylst = ["tortillas", "beans", "salsa"]
suppylst = ["ballloons", "cups"]
liquorlst = ["tequila", "margaritamix"]
partylst = []

for elem in grocerylst:
    partylst.append(elem)
for elem2 in suppylst:
    partylst.append(elem2)
for elem3 in liquorlst:
    partylst.append(elem3)

print(partylst)
partylst.reverse()
print(partylst)
partylst.remove("ballloons")
print(partylst)
