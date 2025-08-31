# Paso 1 : Solicitar al usuario las medidad de la pieza del mueble en cms

medidas_en_cms = float(input("Por favor ingrese la medida de la pieza (en cm): "))

# Paso 2 : Convertir las medidas de centímetros a pulgadas

convertir_medidas_en_pulgadas = medidas_en_cms / 2.54

# Paso 3 : Mostrar la medidas convertidas en pulgadas al usuario

print("Las medidas en pulgadas de la pieza ingresada son:", convertir_medidas_en_pulgadas)