from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient("127.0.0.1", port=5020)

if not client.connect():
    print("Brak połączenia z serwerem")
    exit()

try:
    while True:
        response = client.read_holding_registers(0, count=3, slave=1)

        if response.isError():
            print("Błąd:", response)
        else:
            print(response.registers)

        time.sleep(1)

except:
    print("\nZatrzymano przez użytkownika")

finally:
    client.close()