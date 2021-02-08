import serial
import time
serdev = '/dev/ttyACM0'                # use the device name you get from `ls /dev/ttyACM*`
s = serial.Serial(serdev)

s.write(bytes("/myled/write 1\n", 'UTF-8'))
line=s.readline() # Read an echo string from K66F terminated with '\n' (pc.putc())
print(line)
line=s.readline() # Read an echo string from K66F terminated with '\n' (RPC reply)
print(line)
time.sleep(1)

s.write(bytes("/myled/write 0\n", 'UTF-8'))
line=s.readline() # Read an echo string from K66F terminated with '\n' (pc.putc())
print(line)
line=s.readline() # Read an echo string from K66F terminated with '\n' (RPC reply)
print(line)
s.close()
