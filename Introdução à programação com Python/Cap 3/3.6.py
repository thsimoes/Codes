materia1 = float(input())
materia2 = float(input())
materia3 = float(input())
aprovado = False
if materia1 > 7 and materia2 > 7 and materia3 > 7:
    aprovado = not(aprovado)
print(aprovado)