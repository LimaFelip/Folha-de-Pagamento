# ----- Sistema de interno dos funcionarios -----
# ---->Sistema de autenticação
    * Cadastro de login
    * login
    * banco de dados

# ----> Cadastro da Empresa e Funcionario Separados
 # 1 - Dados da empresa:
        Nome da empresa
        nome fantasia
        CNPJ
        Endereço
            CEP
            Rua Nº
            Cidade
            Estado
            Pais
        1.1 salvar no Banco de dados
        1.2 Emitir Relatorio para:
            visualização pdf
            Impressão

 # 2 -  Cadastro Informaçoes pessoais do funcionario
        Nome
        Data de nascimento
        Idade
        Data de admição
        Cargo
        Endereço
            CEP
            Rua Nº
            Cidade
            Estado
            Pais
    2.1 salvar no Banco de dados
        1.2 Emitir Relatorio para:
            visualização pdf
            Impressão


----> Informações Administrativas de pagamentos

----------------------------------------------------------------------------------
no Artigo 462 da Constituição Federal, da Consolidação das Leis do Trabalho,
"ao empregador é vedado efetuar qualquer desconto nos salários do empregado,
salvo quando este resultar de adiantamentos, de dispositivos de lei ou de contrato coletivo"
-----------------------------------------------------------------------------------
    Data de Admição - data_admicao
    Salario Base/Bruto - salario_base
    Instituto Nacional do Seguro Social - INSS
    Imposto de Renda Retido na Folha - IRRF
    Fundo de Garantia do Tempo de Serviço - FGTS

    Salario - salario
    Vale Refeição - VR
    Ferias - ferias
    13º Salario - salario_13


Gerar Relatorio Geral
   salvar no Banco de dados
        Emitir Relatorio para:
            visualização pdf
            Impressão

Gerar Relatorio Selecionando Data
(No mês escolhido gerar Salario, valor total do VR, valor das Ferias e data de vencimento e o proximo 13º)
