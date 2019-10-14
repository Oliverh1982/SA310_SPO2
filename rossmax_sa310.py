import pexpect
import time

child = pexpect.spawn("sudo gatttool -b 18:7A:93:12:51:65 -I")

print("Connecting to Rossmax SA310")
child.sendline("connect")
child.expect("Connection successful", timeout=10)
print(" Connected!")



