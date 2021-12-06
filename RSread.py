import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient 
#initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer
#from pymodbus.client.sync import ModbusSerialClient as ModbusClient

#client = ModbusClient(method='rtu', port='COM5', baudrate=9600, timeout=0.5)
client = ModbusClient(method = 'rtu', port='/dev/ttyUSB0', stopbits = 1, bytesize = 8, parity = 'E' , baudrate= 9600)


client.connect()

read=client.read_holding_registers(address = 0x1001,count =8,unit=1)
data=read.registers #read register 
#print('Off_write_mode')
print(data) #print register data
write  = client.write_register(0x1001,240,unit=1)# address = , value to set = , slave ID = 1
read=client.read_holding_registers(address = 0x1001,count =8,unit=1)
data=read.registers #read register 
print(data) #print register data
