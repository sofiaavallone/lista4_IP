# Times oponentes possíveis
# Lorelei 
lorelai = [["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60],
    ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78],
    ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70],
    ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100]]

# Bruno
bruno = [["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100],
    ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95],
    ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75],
    ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130]]

# Agatha 
agatha = [["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80],
    ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50],
    ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110],
    ["Poliwrath", "agua", 190, 55, "Soco Dinâmico", 60, "agua", 70]]

# Lance 
lance = [["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105],
    ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130],
    ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55],
    ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93]]

time_jogador = []

# Fase de preparação
print("Hora de montar seu time Pokémon!")
for i in range(4): # Montagem do time jogador
    entrada = input().split(" - ") # Nome, tipo, HP, defesa, nome do ataque, poder do ataque, tipo do ataque, velocidade
    time_jogador.append(entrada)

# Escolha do oponente
print()
print("Qual membro da Elite Four você deseja enfrentar?")
oponente = input().lower()
if oponente == "lorelai":
    time_oponente = lorelai
elif oponente == "bruno":
    time_oponente = bruno
elif oponente == "agatha":
    time_oponente = agatha
else:
    time_oponente = lance
print()

def iniciar (pokemon1, pokemon2):
    if int(pokemon2[7]) > int(pokemon1[7]):
        pokemon1 = pokemon2
        pokemon2 = pokemon1
    return pokemon1, pokemon2


# Def das batalhas
while len(time_oponente) > 0 and len(time_jogador) > 0:
    pokemon1 = time_jogador[0]
    pokemon2 = time_oponente[0]
    # Definindo a ordem correta (de acordo com a velocidade)
    ordem = iniciar(pokemon1, pokemon2)
    pokemon1 = ordem[0]
    pokemon2 = ordem[1]

    # Turnos
    #while pokemon1[2] > 0 and pokemon2[2] > 0: