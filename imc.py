alt = float(input("Digite sua altura: "))
ps = float(input("Digite seu peso: "))

imc = ps/(alt*alt)

if imc < 18.5:
    print("Magreza")
elif imc > 18.6 and imc < 24.9:
    print("Normal")
elif imc > 25.0 and imc < 29.9:
    print("sobrepeso")
elif imc > 30.0 and imc < 39.9:
    print("Obesidade")
else:
    print("Obesidade grave")

print(f"{imc}")