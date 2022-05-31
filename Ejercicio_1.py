print("----------------------------")
print("----- Caso 1 centinela -----")
print("----- NOTAS ESTUDIANTES ----")
print("----------------------------")

#Entrada
cod = int(input(" Digite el codigo del estudiante: "))
nombre = input(" Digite el nombre del estudiante: ")
if cod != 0 :
    nota1 = float(input(" Digite la nota del parcial no. 1: "))
    nota2 = float(input(" Digite la nota de parcial no. 2: "))
    nota3 = float(input(" DIgite la nota del parcial no. 3: "))
else:
    print(" Fin de los datos de entrada ")

#procesamiento
reprobados = 0

while cod != 0:
    nota_final = ( nota1 + nota2 + nota3) / 3
    print(" El estudiante de codigo " + str(cod) + " cuyo nombre es " + nombre + " obtuvo una nota definitiva de " + str(nota_final))
    if nota_final < 3:
        reprobados = reprobados + 1
    #Entrada 
    cod = int(input(" DIgite el codigo del estudiante: "))
    nombre = input(" Digite el nombre del estudiante: ")
    if cod != 0 :
        nota1 = float(input(" Digite la nota del parcial no. 1: "))
        nota2 = float(input(" Digite la nota de parcial no. 2: "))
        nota3 = float(input(" DIgite la nota del parcial no. 3: "))
    else:
        print("Fin de los datos de entrada ")
#Salida 
print(" Cantidad de estudiantes que reprobaron la materia: " + str(reprobados))

    

       