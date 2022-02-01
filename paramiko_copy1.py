import out as out
import paramiko
import time

from Tools.scripts.fixcid import err

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Initiating connection")
ssh_client.connect(hostname='192.168.172.129', username='op', password='PZ8Hfy3=Ve7fQkt*')
print("Connection established")
stdin, stdout, stderr = ssh_client.exec_command('show bank')
time.sleep(20)
print("sleep time completed")
while not stdout.channel.exit_status_ready():
    if stdout.channel.recv_ready():
        out = stdout.readlines()
err = stderr.readlines()
ssh_client.close()
print("Closed connection")
print(f"Output: {out}")
print(f"Err: {err}")
