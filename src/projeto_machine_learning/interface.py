import tkinter as tk
from tkinter import messagebox
import joblib

# Carregamento do modelo treinado
modelo_carregado = joblib.load('modelo_poluicao_ar.joblib')

# Função para fazer previsão com base na hora inserida pelo usuário
def fazer_previsao():
    hora_previsao = entrada_hora.get()

    # Verifica se a entrada é um número entre 0 e 23
    if not hora_previsao.isdigit() or int(hora_previsao) < 0 or int(hora_previsao) > 23:
        messagebox.showerror("Erro", "Hora inserida inválida. Por favor, insira um valor entre 0 e 23.")
    else:
        # Fazendo previsões com o modelo
        previsao = modelo_carregado.predict([[int(hora_previsao)]])
        messagebox.showinfo("Previsão", f"Previsão de qualidade do ar às {hora_previsao} horas: {previsao[0]:.2f}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Previsão da Qualidade do Ar")

# Widget Label
label_hora = tk.Label(janela, text="Insira a hora para previsão (0-23):")
label_hora.pack()

# Widget Entry
entrada_hora = tk.Entry(janela)
entrada_hora.pack()

# Widget Button
botao_prever = tk.Button(janela, text="Prever", command=fazer_previsao)
botao_prever.pack()

# Execução do loop principal
janela.mainloop()
