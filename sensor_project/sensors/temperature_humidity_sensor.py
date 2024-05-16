import adafruit_dht
import board

class TemperatureHumiditySensor:
    def __init__(self):
        self.sensor = adafruit_dht.DHT22(board.D4)
    
    def read_data(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity
            return temperature, humidity
        except Exception as e:
            print("Erro ao ler dados do sensor de temperatura e umidade:", e)
            return None, None