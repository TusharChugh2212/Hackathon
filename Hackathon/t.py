import serial
import sqlite3

change = 0
flag = 0
conn = sqlite3.connect('site.db')
cur = conn.cursor()
serial_port = 'COM5'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)
while True:
    line = ser.readline().decode()
    line = str(line.strip())
    print(line)
    if (line == '1' or line == '0'):
        flag = 0
        print("hi")
    line = bool(line)
    if(change != line and flag != 1):
        cur.execute('UPDATE parking_lot SET parked=? WHERE slot_no=?', [change, 1])
        cur.execute("SELECT * FROM parking_lot")
        flag = 1
        print(cur.fetchone())
        conn.commit()
        change = not change

