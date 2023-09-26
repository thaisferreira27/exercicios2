nome1 = input("Digite o nome da primeira pessoa: ")
idade1= int(input("digite a idade da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("digite a idade da sengunda pessoa: "))
anoAtual= int(input("Digite o ano atual: "))
nascimento1 = anoAtual-idade1
nascimento2 = anoAtual-idade2
if(idade1 < idade2):
    print("A pessoa mais nova é " + nome1 + " e nasceu em " +str(nascimento1))
elif(idade1>idade2):
    print("A pessoa mais nova é " + nome2 + " e nasceu em " +str(nascimento2))
else:
    print("As duas pessoas tem a mesma idade e nasceram em "+ str(nascimento1))