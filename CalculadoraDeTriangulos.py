# Calculadora de Triângulos Simples

import math

while True:

    print('')
    print('-' * 25)
    print('CALCULADORA DE TRIÂNGULOS')
    print('-' * 25)
    print('\nObs.: UTILIZE APENAS CENTÍMETROS.')
    print('\nEscolha a opção desejada.\n')

    print('1 - Relações Métricas do Triângulo Retângulo')
    print('2 - Relações Métricas do Triângulo Equilátero')
    print('3 - Relações Métricas do Triângulo Isósceles')
    print('4 - Relações Métricas do Triângulo Escaleno')
    print('5 - Relações Trigonométricas do Triângulo')

    print('\nDigite apenas o número correspondente.\n')

    try:

        option = int(input('Número da Opção: '))

        if option == 1:  # Relações Métricas do Triângulo Retângulo

            print('\nOpção escolhida: Relações Métricas do Triângulo Retângulo')

            print('\nEscolha a opção desejada.\n')

            print('1 - Lado')
            print('2 - Altura')
            print('3 - Perímetro')
            print('4 - Área (Catetos)')
            print('5 - Área (Altura)')
            print('6 - Área (Teorema de Heron)')
            print('7 - Área (Raio Circunscrito)')

            optioninside = int(input("\nNúmero da Opção: "))


            if optioninside == 1:  # Lado

                print('\nOpção escolhida: Lado\n')

                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = math.sqrt((lado1 ** 2) + (lado2 ** 2))

                print('\nLado 3: {:.3f} cm\n'.format(lado3))


            elif optioninside == 2:  # Altura

                print('\nOpção escolhida: Altura\n')

                m = float(input('Metade menor da hipotenusa: '))
                n = float(input('Metade maior da hipotenusa: '))
                h = m * n

                print("\nAltura: {:.3f}\n".format(h))


            elif optioninside == 3:  # Perímetro

                print("\nOpção escolhida: Perímetro\n")
                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))

                perimetro = lado1 + lado2 + lado3

                print('Perímetro: {:.3f}'.format(perimetro))


            elif optioninside == 4:  # Área (catetos)

                print('\nOpção escolhida: Área (catetos)\n')

                cateto1 = float(input('Cateto 1: '))
                cateto2 = float(input('Cateto 2: '))
                area = (cateto1 * cateto2) / 2

                print('Area: {:.3f} cm²'.format(area))


            elif optioninside == 5:  # Área (hipotenusa)

                print("\nOpção escolhida: Área (hipotenusa)\n")

                hipotenusa = float(input('Hipotenusa: '))
                metademaiorhipotenusa = float(input('Metade maior da hipotenusa: '))
                area = (metademaiorhipotenusa * hipotenusa) / 2

                print('Area: {:.3f} cm²'.format(area))

            elif optioninside == 6:  # Área (Teorema de Heron)

                print("\nOpção escolhida: Área (Teorema de Heron)\n")

                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))
                p = (lado1 + lado2 + lado3) / 2  # semiperímetro automático

                area = math.sqrt(p * (p - lado1) * (p - lado2) * (p - lado3))

                print('Area: {:.3f} cm²'.format(area))


            elif optioninside == 7:  # Área (Raio Circunscrito)

                print("\nOpção escolhida: Área (Raio Circunscrito)\n")

                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))
                raio = float(input('Raio da Circunferência Circunscrita: '))

                area = (lado1 + lado2 + lado3) / (4 * raio)

                print('Area: {:.3f} cm²'.format(area))


        elif option == 2:  # Relações Métricas do Triângulo Equilátero

            print('\nOpção escolhida: Relações Métricas do Triângulo Equilátero')

            print('\nEscolha a opção desejada.\n')

            print('1 - Lado')
            print('2 - Altura')
            print('3 - Perímetro')
            print('4 - Área (Tradicional)')
            print('5 - Área (Teorema de Heron)')
            print('6 - Área (Raio Circunscrito)')

            optioninside = int(input("\nNúmero da Opção: "))


            if optioninside == 1:  # Lado

                print('\nOpção escolhida: Lado\n')

                lado = float(input('Lado: '))

                print('\nLado 3: {:.3f} cm\n'.format(lado))


            elif optioninside == 2:  # Altura

                print('\nOpção escolhida: Altura\n')

                print("\nOpção escolhida: Perímetro\n")
                lado = float(input('Lado: '))
                h = (math.sqrt(3) * lado) / 2

                print("\nAltura: {:.3f}\n".format(h))


            elif optioninside == 3:  # Perímetro

                print("\nOpção escolhida: Perímetro\n")
                lado = float(input('Lado: '))

                perimetro = lado * 3

                print('Perímetro: {:.3f}'.format(perimetro))


            elif optioninside == 4:  # Área (Tradicional)

                print('\nOpção escolhida: Área\n')

                lado = float(input('Lado: '))
                area = (math.sqrt(3) / 4) * (lado ** 2)

                print('Area: {:.3f} cm²'.format(area))

            elif optioninside == 5:  # Área (Teorema de Heron)

                print("\nOpção escolhida: Área (Teorema de Heron)\n")

                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))
                p = (lado1 + lado2 + lado3) / 2  # semiperímetro automático

                area = math.sqrt(p * (p - lado1) * (p - lado2) * (p - lado3))

                print('Area: {:.3f} cm²'.format(area))


            elif optioninside == 6:  # Área (Raio Circunscrito)

                print("\nOpção escolhida: Área (Raio Circunscrito)\n")

                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))
                raio = float(input('Raio da Circunferência Circunscrita: '))

                area = (lado1 + lado2 + lado3) / (4 * raio)

                print('Area: {:.3f} cm²'.format(area))


        elif option == 3:  # Relações Métricas do Triângulo Isósceles

            print('\nOpção escolhida: Relações Métricas do Triângulo Isósceles')

            print('\nEscolha a opção desejada.\n')

            print('1 - Altura')
            print('2 - Perímetro')
            print('3 - Área (Tradicional)')
            print('5 - Área (Teorema de Heron)')
            print('6 - Área (Raio Circunscrito)')

            optioninside = int(input("\nNúmero da Opção: "))


            if optioninside == 1:  # Altura

                print('\nOpção escolhida: Altura\n')

                ladosiguais = float(input('Medida dos lados iguais: '))
                base = float(input('Base: '))
                altura = math.sqrt(((base / 2) ** 2) - (ladosiguais ** 2))

                print("\nAltura: {:.3f} cm\n".format(altura))


            elif optioninside == 2:  # Perímetro

                print("\nOpção escolhida: Perímetro\n")
                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))

                perimetro = lado1 + lado2 + lado3

                print('Perímetro: {:.3f} cm'.format(perimetro))


            elif optioninside == 3:  # Área (tradicional)

                print('\nOpção escolhida: Área (tradicional)\n')

                base = float(input('Base: '))
                altura = float(input('Altura 2: '))

                area = base * altura / 2

                print('Area: {:.3f} cm²'.format(area))


            elif optioninside == 4:  # Área (Teorema de Heron)

                print("\nOpção escolhida: Área (Teorema de Heron)\n")

                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))
                p = (lado1 + lado2 + lado3) / 2  # semiperímetro automático

                area = math.sqrt(p * (p - lado1) * (p - lado2) * (p - lado3))

                print('Area: {:.3f} cm²'.format(area))


            elif optioninside == 5:  # Área (Raio Circunscrito)

                print("\nOpção escolhida: Área (Raio Circunscrito)\n")

                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))
                raio = float(input('Raio da Circunferência Circunscrita: '))

                area = (lado1 + lado2 + lado3) / (4 * raio)

                print('Area: {:.3f} cm²'.format(area))


        elif option == 4:  # Relações Métricas do Triângulo Escaleno

            print('\nOpção escolhida: Relações Métricas do Triângulo Escaleno')

            print('\nEscolha a opção desejada.\n')

            print('1 - Altura')
            print('2 - Perímetro')
            print('3 - Área (Tradicional)')
            print('5 - Área (Teorema de Heron)')
            print('6 - Área (Raio Circunscrito)')

            optioninside = int(input("\nNúmero da Opção: "))


            if optioninside == 1:  # Altura

                print('\nOpção escolhida: Altura\n')

                ladosiguais = float(input('Medida dos lados iguais: '))
                base = float(input('Base: '))
                altura = math.sqrt(((base / 2) ** 2) - (ladosiguais ** 2))

                print("\nAltura: {:.3f} cm\n".format(altura))


            elif optioninside == 2:  # Perímetro

                print("\nOpção escolhida: Perímetro\n")
                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))

                perimetro = lado1 + lado2 + lado3

                print('Perímetro: {:.3f} cm'.format(perimetro))


            elif optioninside == 3:  # Área (tradicional)

                print('\nOpção escolhida: Área (tradicional)\n')

                base = float(input('Base: '))
                altura = float(input('Altura 2: '))

                area = base * altura / 2

                print('Area: {:.3f} cm²'.format(area))


            elif optioninside == 4:  # Área (Teorema de Heron)

                print("\nOpção escolhida: Área (Teorema de Heron)\n")

                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))
                p = (lado1 + lado2 + lado3) / 2  # semiperímetro automático

                area = math.sqrt(p * (p - lado1) * (p - lado2) * (p - lado3))

                print('Area: {:.3f} cm²'.format(area))


            elif optioninside == 5:  # Área (Raio Circunscrito)

                print("\nOpção escolhida: Área (Raio Circunscrito)\n")

                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                lado3 = float(input('Lado 3: '))
                raio = float(input('Raio da Circunferência Circunscrita: '))

                area = (lado1 + lado2 + lado3) / (4 * raio)

                print('Area: {:.3f} cm²'.format(area))


        elif option == 5:  # Relações Trigonométricas do Triângulo

            print('\nOpção escolhida: Relações Trigonométricas do Triângulo')

            print('\nEscolha a opção desejada.\n')

            print('1 - Seno')
            print('2 - Cosseno')
            print('3 - Tangente')
            print('4 - Secante')
            print('5 - Cossecante')
            print('6 - Cotangente ')

            optioninside = int(input("\nNúmero da Opção: "))

            if optioninside == 1:  # Seno

                print('\nOpção escolhida: Seno\n')

                catetooposto = float(input('Cateto Oposto: '))
                hipotenusa = float(input('Hipotenusa: '))

                seno = catetooposto / hipotenusa

                print('\nSeno: {:.3f}\n'.format(seno))


            elif optioninside == 2:  # Cosseno

                print('\nOpção escolhida: Cosseno\n')

                catetoadjacente = float(input('Cateto Adjacente: '))
                hipotenusa = float(input('Hipotenusa: '))

                cosseno = catetoadjacente / hipotenusa

                print('\nCosseno: {:.3f}\n'.format(cosseno))


            elif optioninside == 3:  # Tangente

                print('\nOpção escolhida: Tangente\n')

                catetooposto = float(input('Cateto Oposto: '))
                catetoadjacente = float(input('Cateto Adjacente: '))

                tangente = catetooposto / catetoadjacente

                print('\nTangente: {:.3f}\n'.format(tangente))

            elif optioninside == 4:  # Secante

                print('\nOpção escolhida: Secante\n')

                catetooposto = float(input('Cateto Oposto: '))
                hipotenusa = float(input('Hipotenusa: '))

                secante = 1 / (catetooposto / hipotenusa)

                print('\nSecante: {:.3f}\n'.format(secante))

            elif optioninside == 5:  # Cossecante

                print('\nOpção escolhida: Cossecante\n')

                catetoadjacente = float(input('Cateto Adjacente: '))
                hipotenusa = float(input('Hipotenusa: '))

                cossecante = 1 / (catetoadjacente / hipotenusa)

                print('\nCossecante: {:.3f}\n'.format(cossecante))

            elif optioninside == 6:  # Cotangente

                print('\nOpção escolhida: Cotangente\n')

                catetooposto = float(input('Cateto Oposto: '))
                catetoadjacente = float(input('Cateto Adjacente: '))

                cotangente = 1 / (catetooposto / catetoadjacente)

                print('\nCotangente: {:.3f}\n'.format(cotangente))


    except:
        print('\nErro, por favor, insira apenas o que se pede.')
