
# primera impresion
print ("hello Nicolas")

# String operations

d = " mi nombre es Diego"
print("El resultado es :",d[-3])

print("El resultado de adelante para atras es:", d[3:10])

# Concatenacion

f = "Paula"
d = "Andrea"

print(f+d)

print(d+f)


# String Formating

colegio = "comfenalco"

year = 1994

# f-string

print(f"yo estudie en el colegio: {colegio} en el ano : {year}")


# Regular Expressions ( re module)

import re

text = "El dia de hoy estuve trabajando duro y tambien estuve super contento, quisiera agradecer a Dios todo"
result = re.findall(r"\b\w{7}\b", text)
print("un texto que contiene 7 letras",result)  # Output: ['rain', 'Spain']





