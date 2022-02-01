import out as out
import paramiko
import time

from Tools.scripts.fixcid import err

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Initiating connection")
ssh_client.connect(hostname='192.168.172.129', username='op', password='PZ8Hfy3=Ve7fQkt*')
print("Connection established")
print(ssh_client)
stdin, stdout, stderr = ssh_client.exec_command('show bank')
print(stdin)
print(stdout)
time.sleep(10)
print("sleepover")
# err = stderr.readlines()
while not stdout.channel.exit_status_ready():
    # time.sleep(0.1)
    # stdin.write('PZ8Hfy3=Ve7fQkt*\n')
    # stdin.write("ls\n")
    # stdin.flush()
    if stdout.channel.recv_ready():
        stdoutLines = stdout.readlines()
ssh_client.close()
print("Closed connection")
print(f"Output: {out}")
print(f"Err: {err}")
