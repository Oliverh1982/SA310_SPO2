import pexpect
import time

child = pexpect.spawn("sudo gatttool -b 18:7A:93:12:51:65 -I")

print("Connecting to Rossmax SA310")
child.sendline("connect")
child.expect("Connection successful", timeout=10)
print(" Connected!")

time.sleep(1)
child.sendline("char-write-req 0x0047 0100")
print(" Write cmd!")

while True:
     try:
      child.expect("Notification handle = 0x0046 value: ", timeout=2)
      child.expect("\r\n", timeout=2)

      print(child.before)
      #value=bytes.decode(child.before)
      #print('str value=',value)
      
      spo2=child.before[21:23]
      pulse=child.before[24:26]
     
      spo2_value=int(spo2,16)
      pulse_value=int(pulse,16) 
      print()
      print('Spo2 is %d'%spo2_value,'%')
      print('Pulse is %d /min'%pulse_value)

     except pexpect.TIMEOUT:
       print('waiting.....')
       pass

