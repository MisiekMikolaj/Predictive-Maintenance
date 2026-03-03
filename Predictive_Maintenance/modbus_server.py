from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusServerContext, ModbusSlaveContext, ModbusSparseDataBlock
import time
import threading
import random

# przykładowe rejestry Holding Registers
store = ModbusSlaveContext(
    hr=ModbusSparseDataBlock({1: 2, 2: 60, 3: 5})  # rejestry z wartościami
)

context = ModbusServerContext(slaves=store, single=True)

# --- CYKLICZNA ZMIANA DANYCH (symulacja pracy maszyny) ---
def update_registers():
    i = 0

    while True:

        # zmieniamy wartości jak w realnym procesie
        store.setValues(3, 0, [i])        # HR1 – licznik
        store.setValues(3, 1, [random.randint(50, 100)])  # HR2 – np. temperatura
        store.setValues(3, 2, [random.randint(15, 19)])              # HR3 – stała wartość

        print("Nowe wartości:", store.getValues(3, 0, 3))
        time.sleep(1)  # cykl PLC = 1 sekunda
        i = i +1

# --- START ---
if __name__ == "__main__":
    threading.Thread(target=update_registers, daemon=True).start()
    StartTcpServer(context, address=("127.0.0.1", 5020))