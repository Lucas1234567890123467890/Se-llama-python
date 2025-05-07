def 9():
  fecha = int(input("Ingrese una fecha: "))
  año = fecha % 10000
  mes = (fecha // 10000) % 100
  dia = fecha // 1000000
  print("Día:", dia)
  print("Mes:", mes)
  print("Año:", año)
