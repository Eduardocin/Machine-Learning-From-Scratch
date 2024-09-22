# cálculo da nota final
def nota_final(notas_quesitos, tempo_desfile):
    nota_final = sum(notas_quesitos) / len(notas_quesitos)
    
    if tempo_desfile < 65:
        penalidade = (65 - tempo_desfile) * 0.1
        nota_final -= penalidade
    elif tempo_desfile > 75:
        penalidade = (tempo_desfile - 75) * 0.1
        nota_final -= penalidade
    
    return nota_final
    
# cabecalho
print("Desfile de samba do Rio de janeiro 2024")

# recebe informacoes das escolas

escolas = []
while True:
    nome = input()
    if nome == 'Não há mais escolas':
        break
    tema = input()
    tempo_desfile = int(input())
    escolas.append({'nome': nome, 'tema': tema, 'tempo_desfile': tempo_desfile, 'notas': {}})
    
# recebe notas dos quesitos
quesitos = []
while True:
    quesito = input()
    if quesito == 'Não há mais quesitos':
        break
    else:
        print(f"Vamos às notas para o quesito {quesito}:")
    
        quesitos.append(quesito)
        for escola in escolas:
            escola_nota = input().split(' - ')
            nome_escola = escola_nota[0]
            nota = float(escola_nota[1])
            escola['notas'][quesito] = nota
            if nota==10:
                nota = int(nota)
                print(f"{nome_escola}: {nota}")
            else: 
                print(f"{nome_escola}: {nota:.1f}")
# #imprime as notas para cada quesito
# for quesito in quesitos:
#     print(f"Vamos às notas para o quesito {quesito}:")
#     for escola in escolas:
#         nota = escola['notas'][quesito]
#         if nota==10: 
#             nota = int(nota)
#         print(f"{escola['nome']}: {nota}")

#cálculo da campeã 

campea = max(escolas, key=lambda escola: nota_final(escola['notas'].values(), escola['tempo_desfile']))
nome_campea = campea['nome']
nota_campea = nota_final(campea['notas'].values(), campea['tempo_desfile'])
if nota_campea==10:
    nota_campea = int(nota_campea)
print(f"E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:")
print(f"{nome_campea} com uma nota final de {nota_campea:.2f}!")