"""
Ambientes virtuais em Python (Venv)
Um ambinete virtual carrega toda a sua instalação do python para uma pasta no caminho escolhido
ao ativar um ambiente virtual será usada
pode se dar o nome que quiser mas geralemente é venv env .venv .env


1 -> Criar ambiente virtual: python -m venv nome_do_ambiente Ex: python -m venv venv  
ver onde o python global esta: gcm python -Syntax

2 -> Ativar o ambiente virtual: nome_do_ambiente\Scripts\activate

Set-ExecutionPolicy AllSigned -> caso dê erro para ativar

Selecionar interpretador do venv

rodar para atualizar o pip: python pip install --upgrade pip

instalar pacotes que não vem com o python: pip install biblioteca

requirements.txt -> requirementos do ambiente virtual para rodar o programa: pip freeze > requirements.txt

recriar o ambiente -> pip freeze > requirements.txt

pip freeze -> escreve tudo que tem

3 -> Desativar o ambiente virtual: nome_do_ambiente\Scripts\deactivate ou só deactivate
"""