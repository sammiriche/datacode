import paramiko
 
def sshclient_execmd(hostname, port, username, password, execmd):
    #paramiko.util.log_to_file("paramiko.log")
    
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command (execmd)
    # stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    
    print (stdout.read())
    
    s.close()
    
        
def main():
    
    hostname = '172.31.64.35'
    port = 22
    username = 'admin'
    password = 'xtgsywb6193'
    execmd = "ping 172.31.64.28"
    
    sshclient_execmd(hostname, port, username, password, execmd)
    
    
if __name__ == "__main__":
    main()