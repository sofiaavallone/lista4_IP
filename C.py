vidas_fatalis = 1800
vidas_cacador_great_sword = 200
vidas_cacador_glaive_inseto = 200
vidas_cacador_fuzi_arco = 200
vivo_gs = True
vivo_gi = True
vivo_fa = True

def great_sword (acao_cacador, vidas_fatalis):
    if acao_cacador == "Golpe Carregado":
        vidas_fatalis-=165
    elif acao_cacador == "Corte Largo":
        vidas_fatalis-=120
    else:
        vidas_fatalis-=200
    
    return vidas_fatalis

def fuzi_arco (acao_cacador, vida_fatalis):
    if acao_cacador == "Tiro Carregado":
        vida_fatalis-=90
    elif acao_cacador == "Bala de Penetração":
        vida_fatalis-=120
    else:
        vida_fatalis-=150
    
    return vida_fatalis

def glaive_inseto (acao_cacador, vida_fatalis, extrato_kinseto, vidas_cacador):
    if acao_cacador == "Corte Aéreo":
        vida_fatalis-=100
        return vida_fatalis
    elif acao_cacador == "Descida Carregada":
        vida_fatalis-=120
        return vida_fatalis
    else:
        if extrato_kinseto == "Vermelho":
            vida_fatalis-=40
            return vida_fatalis
        elif extrato_kinseto == "Amarelo":
            vidas_fatalis-=15
            return vidas_fatalis
        else:
            vida_cacador+=40
            return vida_cacador

def fatalis (vidas_cacador_gs, vidas_cacador_gi, vidas_cacador_fa, acao_fatalis, status_gs, status_gi, status_fa, vivo_gs, vivo_gi, vivo_fa):
    if acao_fatalis == "Ataque com Cauda":
        vidas_cacador_gs-=55
        vidas_cacador_gi-=55
        vidas_cacador_fa-=55
        return vidas_cacador_gs, vidas_cacador_gi, vidas_cacador_fa
    elif acao_fatalis == "Bola de Fogo":
        vidas_cacador_gs-=65
        vidas_cacador_gi-=65
        vidas_cacador_fa-=65
        return vidas_cacador_gs, vidas_cacador_gi, vidas_cacador_fa
    else:
        if status_gs == "Desprotegido":
            vivo_gs = False
        if status_gi == "Desprotegido":
            vivo_gi = False
        if status_fa == "Desprotegido":
            vivo_fa = False
        return vivo_gs, vivo_gi, vivo_fa

print("Hora de Lutar contra a Historia!")
print()

for i in range(4):
    if vivo_gs == True and vidas_cacador_great_sword > 0:
        acao_cacador_gs = input()
    if vivo_gi == True and vidas_cacador_glaive_inseto > 0:
        acao_cacador_gi = input()
        if acao_cacador_gi == "Kinseto":
            extrato_kinseto = input()
    if vivo_fa == True and vidas_cacador_fuzi_arco > 0:
        acao_cacador_fa = input()
    if vidas_fatalis > 0:
        acao_fatalis = input()
        if acao_fatalis == "Mar de Chamas Negras":
            status_gs = input()
            status_gi = input()
            status_fa = input()

if vidas_fatalis > 0:
    print("O Fatalis conseguiu sobreviver ao combate...")
    print("O mundo corre perigo!")
else:
    print("Eu não acredito, vocês conseguiram!")
    print("Obrigado caçadores! O mundo está salvo.")