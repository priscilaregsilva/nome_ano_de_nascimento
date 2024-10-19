#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano
#atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e 
#continuará perguntando até que um valor correto seja preenchido.

nome = input("Digite seu nome completo: ")

while True:
    ano = input("Digite o ano de nascimento: (entre 1922 e 2021) ")

    if int(ano) >=1922 and int(ano) <=2021:
        idade = 2022 - int(ano)
        print("A idade de " + nome + " é : " + str(idade))
        break

    else:
        print("Ano digitado inválido: ")