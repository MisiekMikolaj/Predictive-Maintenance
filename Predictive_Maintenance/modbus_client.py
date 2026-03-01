from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient("127.0.0.1", port=5020)
client.connect()

# read_holding_registers(address, count, slave=1) -> używamy slave jako keyword

while True:
    response = client.read_holding_registers(0, count = 3, slave = 1)
    print(response.registers)  # powinno wypisać: [25, 50, 75]
    time.sleep(1)

client.close()