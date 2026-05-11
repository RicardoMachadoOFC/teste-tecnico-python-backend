def gerar_diagnostico(registros):

    if len(registros) == 0:
        return {"mensagem": "nenhum registro encontrado"}

    soma_foco = sum(r.nivel_foco for r in registros)
    tempo_total = sum(r.tempo_minutos for r in registros)

    media_foco = soma_foco / len(registros)

    if media_foco < 3:
        feedback = "Você está muito distraído"
    elif media_foco < 4:
        feedback = "Foco razoável"
    else:
        feedback = "Excelente produtividade"

    return {
        "media_foco": round(media_foco, 2),
        "tempo_total": tempo_total,
        "feedback": feedback
    }