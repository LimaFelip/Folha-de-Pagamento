# ----- Sistema de interno dos funcionarios -----

IMPORTANTE! O projeto está sendo desenvolvido de forma simples e robusta, seguindo as diretrizes Engenharia de Software para fins de estudo e comercial escalavel em python 3.10.1. 
    SDLC - Software Development Life Cycle(Ciclo de vida de desenvolvimento de software)
        1. Definição de Objetivos ✔️
        2. Levantamento e Análise de Requisitos ✔️
            1. Requisitos Funcionais ✔️
            2. Requisitos Não Funcionais ✔️
            3. Saída✔️
        3. Design e Arquitetura 
            1. Arquitetura de Pastas ✔️
            2. Modelagem de Dados
            3. Design de UI

        4. Implementação
        5. Manutenção
            
# ----> 1. Definição de Objetivos
    Decreto 3.048/1999  Regulamento da Previdência Social 
O artigo 225 do Decreto determina que todas as empresas elaborem mensalmente sua folha, incluindo:

* Todos os segurados empregados, contribuintes individuais e autônomos vinculados.
* Todas as parcelas pagas, devidas ou creditadas a cada um deles.
* Esse dispositivo garante que o governo possa fiscalizar corretamente a arrecadação e combater a sonegação.
        fonte(https://inventsoftware.com.br/gestao-de-pessoas/calculo-folha-de-pagamento-brasil-2026)
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

# ----> Sistema de autenticação
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
    
# 📌 Para instalar Dependências em Python
1. Primeiro, certifique-se de instalar python no seu sistema local.
 [Clique aqui para baixar Python](https://www.python.org/downloads/)

2. Vá até sua pasta de código e no terminal execute.

3. Para a Biblioteca GUI 
    pip install PyQt5

# 💻 Para execultar em seu sistema local.

# ---->Arquiteutra de Pastas
folha_pagamento/
├── venv/
├── data/
│   └── database.db          # Onde os dados dos funcionários moram
├── assets/
│   └── icons/               # Ícones de usuário, dinheiro, etc.
├── src/
│   ├── main.py              # Inicia o app
│   ├── ui/                  # Arquivos .ui do Qt Designer
│   │   ├── login.ui
│   │   └── funcionarios.ui
│   ├── views/               # Lógica da Interface (Frontend Desktop)
│   │   ├── login_view.py    # Captura o clique do botão
│   │   ├── register_view.py
│   │   └── dashboard_view.py
│   └── backend/             # O "CÉREBRO" DO APP
│       ├── database.py      # Comandos SQL (INSERT, SELECT)
│       ├── calculations.py      # Lógica da Folha (INSS, IRRF, FGTS)
│       └── validations.py    # Verifica CPF, PIS, etc.
├── requirements.txt
└── .gitignore


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
