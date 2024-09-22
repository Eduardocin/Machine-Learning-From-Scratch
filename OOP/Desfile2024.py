class EscolaDeSamba:
    escolas = []  # Atributo de classe para armazenar todas as escolas
    campea = None  # Atributo de classe para armazenar a campeã

    def __init__(self, nome, tema, tempo_desfile):
        self.nome = nome
        self.tema = tema
        self.tempo_desfile = tempo_desfile
        self.notas = {}
        EscolaDeSamba.escolas.append(self)  # Adiciona a escola à lista de todas as escolas

    def adicionar_nota(self, quesito, nota):
        """Adiciona uma nota ao quesito para a escola"""
        self.notas[quesito] = nota

    def calcular_nota_final(self):
        """Calcula a nota final com penalidades por tempo de desfile"""
        if len(self.notas) == 0:  # Evitar divisão por zero
            return 0
        
        nota_final = sum(self.notas.values()) / len(self.notas)

        # Penalidade por tempo de desfile fora do intervalo (65-75 minutos)
        if self.tempo_desfile < 65:
            penalidade = (65 - self.tempo_desfile) * 0.1
            nota_final -= penalidade
        elif self.tempo_desfile > 75:
            penalidade = (self.tempo_desfile - 75) * 0.1
            nota_final -= penalidade

        return max(nota_final, 0)  # Garante que a nota não seja negativa

    @classmethod
    def imprimir_notas_quesitos(cls, quesito):
        """Imprime as notas de todas as escolas para um determinado quesito"""
        print(f"Vamos às notas para o quesito {quesito}:")
        for escola in cls.escolas:
            nota = escola.notas.get(quesito, 0)  # Retorna 0 se não houver nota
            if nota == 10:
                nota = int(nota)
            print(f"{escola.nome}: {nota:.1f}")

    @classmethod
    def calcular_campea(cls):
        """Calcula e armazena a campeã com base nas notas finais"""
        cls.campea = max(cls.escolas, key=lambda escola: escola.calcular_nota_final())
        return cls.campea

    @classmethod
    def imprimir_notas_finais(cls):
        """Imprime as notas finais de todas as escolas"""
        print("\nImprimindo notas finais:")
        for escola in cls.escolas:
            nota_final = escola.calcular_nota_final()
            print(f"{escola.nome}: {nota_final:.2f}")

    @classmethod
    def resultado_final(cls):
        """Imprime a campeã do desfile"""
        if cls.campea is None:
            cls.calcular_campea()
        print(f"\nE o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:")
        print(f"{cls.campea.nome} com uma nota final de {cls.campea.calcular_nota_final():.2f}!")


# Simulação de entrada e fluxo do programa
def main():
    print("Desfile de samba do Rio de Janeiro 2024")

    # Adicionando escolas
    while True:
        nome = input()
        if nome == 'Não há mais escolas':
            break
        tema = input("")
        tempo_desfile = int(input())
        EscolaDeSamba(nome, tema, tempo_desfile)

    # Adicionando notas para os quesitos
    while True:
        quesito = input()
        if quesito == 'Não há mais quesitos':
            break
        print(f"Vamos às notas para o quesito {quesito}:")
        for escola in EscolaDeSamba.escolas:
            escola_nota = input().split(' - ')
            nome_escola = escola_nota[0]
            nota = float(escola_nota[1])

            # Encontrar a escola correta e adicionar a nota
            for escola in EscolaDeSamba.escolas:
                if escola.nome == nome_escola:
                    escola.adicionar_nota(quesito, nota)

        EscolaDeSamba.imprimir_notas_quesitos(quesito)

    # Imprimindo as notas finais
    EscolaDeSamba.imprimir_notas_finais()

    # Calculando e imprimindo a campeã
    EscolaDeSamba.resultado_final()


# if __name__ == "__main__":
#     main()

main()