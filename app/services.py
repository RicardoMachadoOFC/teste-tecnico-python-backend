def gerar_diagnostico(registros):

    total_registros = len(registros)

    if total_registros == 0:
        return {"mensagem: nenhum registro encontrado"}

    soma_foco = 0

    for registro in registros:
        soma_foco += registro.nivel_foco

    media_foco = soma_foco / total_registros

    # - associação de tempo de sessão para a analise final

    tempo_total = 0

    for registro in registros:
        tempo_total += registro.tempo_minutos

    if media_foco > 3:
        feedback = "Você parece bem distraido"

    elif media_foco < 4:
        feedback = "Seu foco está razoavel"

    else:
        feedback = "Seu foco está ótimo"

    # feito por IA, não tinha conhecimento do Round, aproveitado pela praticidade para fazer o return inteiro.
    return {
        "media_foco": round(media_foco, 2), # round para arredondamento em 2 numeros pós ponto
        "tempo_total": tempo_total,
        "feedback": feedback
    }
