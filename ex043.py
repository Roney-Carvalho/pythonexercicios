print(f'\33[7mNUTRIBALANCE\33[m')


altura = float(input('Qual su altura (m)? '))
peso = float(input('Qual seu peso (Kg)? '))
imc = peso / (altura ** 2)
peso_ideal_1 = 18.5 * (altura ** 2)
peso_ideal_2 = 24.8 * (altura ** 2)
print(f'\33[7mO seu IMC é de {imc:.1f} kg/m².\33[m')
print('__--' * 20)
if imc < 18.5:
    print('MAGREZA. Seu peso precisa ser maior.')
elif 18.5 <= imc < 24.9:
    print('NORMAL. Peso ideal para sua altura.')
elif 24.9 <= imc <= 30:
    print('SOBREPESO. Seu peso precisa ser menor.')
else:
    print('\33[31mOBESIDADE. Seu peso precisa ser menor.\33[m')
print(f'Para sua altura, você deve pesar entre \33[33m{peso_ideal_1:.1f} Kg\33[m e \33[33m{peso_ideal_2:.1f} Kg\33[m.')
