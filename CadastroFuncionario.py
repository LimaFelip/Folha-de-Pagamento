# cadastro de funcionarios
print()
print('============== RELATORIO DO FUNCIONARIO ==============  ''\n')

# Dados da empresa

NOME_EM, CNPJ = "   Tavares Industrias LTDA", "00.215.000/0001.21"
print(NOME_EM, ', CNPJ', CNPJ)

EMDERECO_EMPRESA, CIDADE_EM, ESTADO_EM = "          Rua Tavares Nº 000", "São Gonçalo", "RJ"
print(EMDERECO_EMPRESA, CIDADE_EM, ESTADO_EM, "\n")

# informaçoes pessoais do funcionario

# nome = str(input('Nome: '))
# dataNasci = str(input('Data de Nascimento: '))
# idade = int(input('Idade: '))
# cpf = str(input('CPF: '))

# cidade = str(input('Cidade: '))
# estado = str(input('Estado: '))
# endereco = str(input('Rua: '))
# num_endereco = int(input('N°: '))

# quantidade_dependentes = int(input('Quantos dependentes? '))
# cargo = str(input('Cargo: '))
salario_base = float(input("Salario: R$ "))
# data_admicao = str(input('Data de Admição: '))

# Informações Administrativas de pagamentos

# adiantamento = float(input('Adiantamento de: '))
# comissao = float(input('Valor da Comissão: '))
# vr = float(input('Vale refeição: '))
# gratificacao = float(input('Gratificação: '))
# horas_extras = float(input('Horas Extras: '))

# Instituto Nacional do Seguro Social - INSS

aliquata_7_5 = salario_base * 0.75 - 0
aliquata_9 = salario_base * 0.9 - 21.18
aliquata_12 = salario_base * 0.12 - 101.18
aliquata_14 = salario_base * 0.14 - 181.18

deducao_7_5 = 'INSETO'
deducao_9 = 21.18
deducao_12 = 101.18
deducao_14 = 181.18

if salario_base >= 0.0 and salario_base < 1413.00:
     print(f"Salario Base = R$ {salario_base:.2f}")
     print(f"Salario liquido = R$ {aliquata_7_5:.2f}")
     print(f"Alíquota de 7,5%")
     print(f"Valor da parcela a Deduzir = R$ {deducao_7_5} ")

if  salario_base >= 1412.01 and salario_base <=2666.68:
    print(f"Salario Base = R$ {salario_base:.2f}")
    print(f"Salario liquido = R$ {aliquata_9:.2f}")
    print(f"Salario alíquota de 9%")
    print(f"Valor da parcela a Deduzir = R$ {deducao_9} ")

if  salario_base >= 2666.69 and salario_base <= 4000.03:
    print(f"Salario Base = R$ {salario_base:.2f}")
    print(f"Salario liquido = R$ {aliquata_12:.2f}")
    print(f"Alíquota de 12%")
    print(f"Valor da parcela a Deduzir = R$ {deducao_12} ")

if salario_base >= 4000.04 and salario_base <= 7786.01:
     print(f"Salario Base = R$ {salario_base:.2f}")
     print(f"Salario liquido = R$ {aliquata_14:.2f}")
     print(f"Valor da Alíquota de 14%")
     print(f"Valor da parcela a Deduzir = R$ {deducao_14} ")

elif salario_base:
  if salario_base > 7786.02:
    print("Passou do teto de imposto")
  elif salario_base == ( ):
    print("ERRO: Você não digitou nada")

else:
    print("ERRO")


# Imposto de Renda - IRRF
# if salrio_base <=
# FGTS
# Ferias
#  = (salario_base/3)+salario_base
# salario_13 =

# print(f'Salario R${salario_base:.2f}')
# print(f'Ferias R${ferias:.2f}')
