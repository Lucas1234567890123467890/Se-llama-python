autos_vendidos = int(input("Ingrese el número de autos vendidos: "))
valor_auto = float(input("Ingrese el valor de venta de un auto: "))
salario_base = 5500
comision_fija = autos_vendidos * 200
comision_variable = autos_vendidos * (valor_auto * 0.05)
salario_total = salario_base + comision_fija + comision_variable
print("El salario total es:", salario_total)