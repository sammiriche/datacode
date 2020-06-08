import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect('172.31.64.29',22,'admin','xtgsywb6193')
client.connect('172.31.64.29',username='admin',password='xtgsywb6193',allow_agent=False,look_for_keys=False)

stdin,stdout,stderr = client.exec_command('sysname')
stdin,stdout,stderr = client.exec_command('dis cpu-usage')
result = stdout.read()
print(result)