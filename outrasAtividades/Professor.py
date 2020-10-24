import json

def escreve_json(dados):
    with open('meu_arquivo.json', 'w') as f:
        json.dump(dados, f, indent=4)
        f.write(dados)

professor = {
    'nome': 'Rodrigo Fujioka',
    'idade': '32 anos',
    'disciplina': 'APS',
    'instituicao': 'Unipe',
    'civil': 'casado',
    'estado': 'Paraiba' 
}

escreve_json(professor)