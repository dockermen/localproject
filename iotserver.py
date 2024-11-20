from dotenv import load_dotenv
from pymodbus.server import ModbusSerialServer,StartAsyncSerialServer

# 创建 Modbus RTU 客户端
#client = ModbusClient(port='COM3', baudrate=115200, timeout=1000)
server = ModbusSerialServer(port='COM3', baudrate=115200, timeout=1000,context=)
# 连接到从设备
#connection = client.connect()
connection = server.connect()

if connection:
    print("成功连接到 Modbus 从设备")
    #result=client.read_input_registers(address=1000,count=122,slave=1)
else:
    print("连接失败")

