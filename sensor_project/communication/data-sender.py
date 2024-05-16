import requests

class DataSender:
    def __init__(self, server_url):
        self.server_url = server_url
    
    def send_data(self, data):
        try:
            response = requests.post(self.server_url, json=data)
            response.raise_for_status()
            print("Dados enviados com sucesso")
        except Exception as e:
            print("Erro ao enviar dados:", e)