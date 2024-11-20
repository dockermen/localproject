from dotenv import load_dotenv
from pymodbus.client import ModbusSerialClient as ModbusClient
from time import sleep
import json

client = ModbusClient(port='COM3', baudrate=115200, timeout=1000)
def getrtu():
    # 创建 Modbus RTU 客户端
    

    # 连接到从设备
    connection = client.connect()
    print(connection)
    if connection:
        print("成功连接到 Modbus 从设备")

        #读写寄存器
        result=client.read_input_registers(address=4096,count=122,slave=1)
        #print(result.registers)
        return result.registers
        #写线圈
        # for val in [True,False]:
        #     for addr in range(4):
        #         result = client.write_coil(address=addr,value=val,slave=1)
        #         #print(result.get_response_pdu_size())
        #         sleep(10)
        #         status = client.read_coils(address=0,count=10,slave=1)
        #         print(status.bits)
        #         a = bytes(status.bits)
        #         #a = "".join([hex(i)[2:] for i in status.bits])
        #         print(a,len(a))
        #         sleep(5)
        
        #读线圈
        # status = client.read_coils(address=0,count=10,slave=1)
        # #print(result)
        # a = [int(i) for i in status.bits]
        # print(a)
        
    else:
        print("连接失败")
    #client.close()


print(getrtu())
#print((li[0]).to_bytes(4, 'big', signed=True))
# print(['%02X' % i for i in [2]])
#print(int.from_bytes(-14, byteorder='big', signed=True))
# while True:
#     a,b=int(input("线路:")),bool(int(input("开关:")))
#     result = client.write_coil(address=a,value=b,slave=1)
    
#     print(result.encode)