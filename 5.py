def 5():
  horas = int(input("Ingrese las horas: "))
  minutos = int(input("Ingrese los minutos: "))
  segundos = int(input("Ingrese los segundos: "))
  Seg_Max = horas * 3600 + minutos * 60 + segundos
  print("El total en segundos es:", Seg_Max)
