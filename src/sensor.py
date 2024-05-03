import random

def coletar_dados():
    # Simula a coleta de dados dos sensores
    poluicao_ar = random.uniform(0, 100)
    qualidade_agua = random.uniform(0, 10)
    ruido_urbano = random.uniform(0, 150)
    
    return poluicao_ar, qualidade_agua, ruido_urbano
