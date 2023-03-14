import json
pessoa = {
    'nome': 'Diego',
    'sobrenome': 'Alencar Jacober',
    'idade': 18,
    'pais': {
        'mae': 'Janete',
        'pai': 'Thiago'
    },
    'altura': 1.73,
    'dev': True
}

# for i in range(60):
#     with open('manipulando_arquivos/pessoas.json','a+', encoding='utf8') as arquivo:
#     #dicionario, arquivo, salvar como na tabela asc, formatar documento
#         json.dump(pessoa,arquivo,ensure_ascii=True,indent=2)

# with open('manipulando_arquivos/pessoas.json','a+', encoding='utf8') as arquivo:
#     #dicionario, arquivo, salvar como na tabela asc, formatar documento
#         json.dump(pessoa,arquivo,ensure_ascii=True,indent=2)

with open('manipulando_arquivos/pessoas.json','r', encoding='utf8') as arquivo:
    pessoa_json = json.load(arquivo)
    print(pessoa_json)
    print(f'Nome: {pessoa_json["nome"]}')