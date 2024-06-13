# Lista de gols marcados pelo time em cada jogo
gols_marcados = [2, 1, 3, 1, 0]

# Lista de gols sofridos pelo time em cada jogo
gols_sofridos = [1, 2, 2, 1, 3]

# Função para calcular pontos e aproveitamento do time
def calcula_pontos(gols_marcados, gols_sofridos):
    pontos = 0
    
    # Itera sobre os índices dos jogos
    for i in range(len(gols_marcados)):
        if gols_marcados[i] > gols_sofridos[i]:
            pontos += 3  # Ganhou o jogo
        elif gols_marcados[i] == gols_sofridos[i]:
            pontos += 1  # Empatou o jogo
    
    # Calcula o aproveitamento em porcentagem
    aproveitamento = 100 * pontos / (len(gols_marcados) * 3)
    
    return (pontos, aproveitamento)

# Chamada da função para obter os pontos e aproveitamento
pontos, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)

# Imprime os resultados formatados
print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {round(aproveitamento)}%")

