disCar1 = float(input("Insira a distancia percorrida pelo primeiro carro: "))
tempCar1 = float(input("Insira o tempo levado pelo primeiro carro: "))
disCar2 = float(input("Insira a distancia percorrida pelo segundo carro: "))
tempCar2 = float(input("Insira o tempo levado pelo segundo carro: "))
velocidadeMed1 = disCar1/tempCar1
velocidadeMed2 = disCar2/tempCar2 
if(velocidadeMed1>velocidadeMed2):
    print ("O primeiro carro teve a maior velocidade media.")
elif(velocidadeMed1<velocidadeMed2):
        print ("O segundo carro teve a maior velocidade media.")
else: 
      print("A velocidade media dos carros foi igual")