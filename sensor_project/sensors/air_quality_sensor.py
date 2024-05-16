import busio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import board

class AirQualitySensor:
    def __init__(self):
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        cs = board.D5
        self.mcp = MCP.MCP3008(spi, cs)
        self.channel = AnalogIn(self.mcp, MCP.P0)
    
    def read_data(self):
        try:
            air_quality = self.channel.value
            return air_quality
        except Exception as e:
            print("Erro ao ler dados do sensor de qualidade do ar:", e)
            return None