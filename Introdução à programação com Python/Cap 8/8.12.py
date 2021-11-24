def esta(a,b):
    if a in b:
        return True
    else:
        return False

a = "Tiago"
b = ["Tiago", "Thiago", "Willian", "Eduardo", "Antônio"]
c = ["Lissin", "Thiago", "Willian", "Eduardo", "Antônio"]

print(esta(a,b))
print(esta(a,c))