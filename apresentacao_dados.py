#Crie uma apresentação completa utilizando a função print.
#Ter as variaveis Nome, Sobrenome, Idade, Ano de Nascimento, É maior de idade?, Altura em metros

print('\n --- Cadastro de dados --- \n')
nome = input('Qual o seu nome? ') 
sobrenome = input ('Qual o seu sobrenome? ')
idade = int(input('Quantos anos você tem? '))
ano_de_nascimento = input('Em que ano você nasceu? ')
altura = float(input('Qual a sua altura? '))

print('--- Apresentação de dados ---')
print(f'O nome informado foi {nome} {sobrenome}')
print(f'A idade informada do {nome} é {idade} anos')
print(f'O {nome} nasceu no ano de {ano_de_nascimento}')

#vericação de maior idade 
if idade >= 18: 
    print(f'O {nome} tem {idade}, então ele é maior de idade ') #se tiver 18 anos ou mais é maior de idade
else:
    print(f'O {nome} tem {idade}, então ele não é maior de idade ') #se não tiver 18 anos ou mais é menor de idade

print(f'E para finalizarmos o {nome} tem {altura:.2f} de altura')
print('\n --- Fim da apresentação de dados ---')
