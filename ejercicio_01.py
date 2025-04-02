import random

# generar pacientes aleatorios
pacientes = []
contador = 0
for i in range(10):
    paciente = {
        "ID":i+1,
        "FC":random.randint(34,174),
        "PA":random.randint(59,148)
    }
    paciente = {
        "ID":i+2,
        "FC":random.randint(43,123),
        "PA":random.randint(94,128)
    }
    paciente = {
        "ID":i+3,
        "FC":random.randint(58,134),
        "PA":random.randint(93,143)
    }
    paciente = {
        "ID":i+4,
        "FC":random.randint(74,147),
        "PA":random.randint(95,159)
    }
    paciente = {
        "ID":i+5,
        "FC":random.randint(63,122),
        "PA":random.randint(77,182)
    }
    paciente = {
        "ID":i+6,
        "FC":random.randint(69,139),
        "PA":random.randint(88,134)
    }
    paciente = {
        "ID":i+7,
        "FC":random.randint(54,127),
        "PA":random.randint(92,150)
    }
    paciente = {
        "ID":i+8,
        "FC":random.randint(33,128),
        "PA":random.randint(71,159)
    }
    paciente = {
        "ID":i+9,
        "FC":random.randint(68,144),
        "PA":random.randint(94,149)
    }
    paciente = {
        "ID":i+1,
        "FC":random.randint(39,155),
        "PA":random.randint(83,173)
    }
    pacientes.append(paciente)

# función para clasificar pacientes
def clasificar_pacientes(frecuencia, presión):
    if 60<= frecuencia <= 100 and (presión in range(90,120)):
        return "Sano"
    elif frecuencia not in range(60,101) or presión not in range(90,120):
        return "En riesgo"
    else:
        return "Crítico"

# clasificar datos generados
print("clasificación de pacientes aleatorios")
for paciente_clasificado in pacientes:
    estado = clasificar_pacientes(paciente_clasificado["FC"],paciente_clasificado["PA"])
    print(f'Paciente {paciente_clasificado["ID"]} ::: Estado {estado}')
# permitir agregar más pacientes

# datos de entrada
def entrada_int(mensaje, min, max):
    while True:
        try:
            valor = int(input(mensaje))
            if valor in range(min,max+1):
                return valor
            else:
                print(f"Los valores deben estar entre {min} y {max}")
        except ValueError as e:
            print("Valor debe de ser de tipo entero ")

while True:
    continuar = input("Desea ingresar más pacientes? s/n: ").lower().replace(" ","").split()

    if continuar in ["n","no"]:
        print("Finalizó el programa")
        break
    else:
        fc = entrada_int("Ingresa la Frecuencia Cardiaca: ",50,130)
        pa = entrada_int("Ingresa la presión arterial: ",80,150)
        

# graficar datos con Matplotlib