def 10():
  parcial = float(input("Ingrese la nota de exámenes parciales: "))
  practica = float(input("Ingrese la nota de trabajos prácticos: "))
  integrador = float(input("Ingrese la nota del examen integrador: "))
  nota_final = (parciales * 0.3) + (practicos * 0.2) + (integrador * 0.5)
  print("La nota final es:", nota_final)
