import serial
import time

ser = serial.Serial(
    port='COM6',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.12
)
print("Connected to:" + ser.port)

while True:
        rcv = ser.readline().hex()
        hex_code = [0xAA]
        ser.write(serial.to_bytes(hex_code))
        time.sleep(0.120)
        if rcv == '55':
            print('Hex code received')
            break




