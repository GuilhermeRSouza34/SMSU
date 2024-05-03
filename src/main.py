import time
import sqlite3
from sensor import coletar_dados
import statistics

def armazenar_dados(conn, poluicao_ar, qualidade_agua, ruido_urbano):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dados_ambientais (poluicao_ar, qualidade_agua, ruido_urbano) VALUES (?, ?, ?)", (poluicao_ar, qualidade_agua, ruido_urbano))
    conn.commit()

def calcular_estatisticas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados_ambientais")
    rows = cursor.fetchall()
    
    poluicao_ar = [row[2] for row in rows]
    qualidade_agua = [row[3] for row in rows]
    ruido_urbano = [row[4] for row in rows]
    
    if poluicao_ar:
        media_poluicao_ar = statistics.mean(poluicao_ar)
        desvio_padr_poluicao_ar = statistics.stdev(poluicao_ar)
        max_poluicao_ar = max(poluicao_ar)
        min_poluicao_ar = min(poluicao_ar)
        print(f"Estatísticas da Poluição do Ar - Média: {media_poluicao_ar}, Desvio Padrão: {desvio_padr_poluicao_ar}, Máximo: {max_poluicao_ar}, Mínimo: {min_poluicao_ar}")
    
    if qualidade_agua:
        media_qualidade_agua = statistics.mean(qualidade_agua)
        desvio_padr_qualidade_agua = statistics.stdev(qualidade_agua)
        max_qualidade_agua = max(qualidade_agua)
        min_qualidade_agua = min(qualidade_agua)
        print(f"Estatísticas da Qualidade da Água - Média: {media_qualidade_agua}, Desvio Padrão: {desvio_padr_qualidade_agua}, Máximo: {max_qualidade_agua}, Mínimo: {min_qualidade_agua}")
    
    if ruido_urbano:
        media_ruido_urbano = statistics.mean(ruido_urbano)
        desvio_padr_ruido_urbano = statistics.stdev(ruido_urbano)
        max_ruido_urbano = max(ruido_urbano)
        min_ruido_urbano = min(ruido_urbano)
        print(f"Estatísticas do Ruído Urbano - Média: {media_ruido_urbano}, Desvio Padrão: {desvio_padr_ruido_urbano}, Máximo: {max_ruido_urbano}, Mínimo: {min_ruido_urbano}")

def main():
    conn = sqlite3.connect('dados_ambientais.db')
    
    while True:
        poluicao_ar, qualidade_agua, ruido_urbano = coletar_dados()
        armazenar_dados(conn, poluicao_ar, qualidade_agua, ruido_urbano)
        print(f"Dados coletados - Poluição do Ar: {poluicao_ar}, Qualidade da Água: {qualidade_agua}, Ruído Urbano: {ruido_urbano}")
        calcular_estatisticas(conn)  # Calcular estatísticas a cada coleta de dados
        time.sleep(60)  # Coleta a cada 1 minuto

if __name__ == "__main__":
    main()
