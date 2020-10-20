import paramiko

IpAddress = input("Enter the ip address:")
user = input("Enter the username:")
passwrd = input("Enter the password:")
port = 22
command = input("Enter your command:")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(IpAddress, port, user, passwrd)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()

print(lines)