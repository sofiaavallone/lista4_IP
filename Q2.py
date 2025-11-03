nomes_digitais = []

print("TRIBUNAL EM SESSÃO")
print("Juiz: Que comece o julgamento do caso em pauta.")
print()

print("Promotor Edgeworth: A promotoria está pronta, Meritíssimo.")
print("Phoenix Wright: (Lá vamos nós... A reputação do escritório está em jogo.) A defesa está pronta.")
print()

print("--- SALA DE VISITAS DO TRIBUNAL ---")
print("João Guilherme: Sr. Wright, eu juro, eu não o matei! Eu estive lá, mas... é só isso!")
print("Phoenix Wright: (Eu sinto que ele está escondendo algo... Devo pressioná-lo por mais detalhes ou confiar no que ele me disse?)")
print()

escolha_inicial = input()

print("--- DE VOLTA AO TRIBUNAL ---")
print("Juiz: Promotoria, apresente as evidências.")
print("Promotor Edgeworth: A promotoria acusa este homem pelo crime de assassinato...")
print("Promotor Edgeworth: ...João Guilherme!")
print("Promotor Edgeworth: Comecemos com a evidência virtual chave, o registro da última modificação no computador da vítima.")

hora_modificacao = int(input())

print("Promotor Edgeworth: E, de acordo com o legista, a hora exata da morte.")

hora_morte = int(input())

print("Promotor Edgeworth: Finalmente, a prova irrefutável. O relatório de digitais da arma do crime, o troféu.")

numero_digitais = int(input())

print("Promotor Edgeworth: Que o escrivão leia os nomes encontrados na arma...")

for i in range(numero_digitais):
    nomes_digitais.append(input())

print()
print("ARGUMENTOS FINAIS")
print()