import paramiko
import getpass
import telnetlib
import sys


def sshinput():
    IpAddress = input("Enter the ip address:")
    user = input("Enter the username:")
    passwrd = input("Enter the password:")
    port = 22
    command = input("Enter your command:")

    sshconnect(IpAddress, port, user, passwrd, command)

def sshconnect(IpAddress, port, user, passwrd, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IpAddress, port, user, passwrd)
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()

    print(lines)

def telnetconnect():

    IpAddress = input("Enter the ip address:")
    user = input("Enter the username:")
    passwrd = input("Enter the password:")
    # command = bytes(input("Enter your command:"), 'ascii')
    # res = bytes(command, 'utf-8') 
    # please ignore these commented variables will work on them later
    tn = telnetlib.Telnet(IpAddress)

    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if passwrd:
        tn.read_until(b"Password: ")
        tn.write(passwrd.encode('ascii') + b"\n")

    tn.write(b"ls") #Put your command here, will work on a proper user input later
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))


if __name__ == "__main__":
    # if there's passed arguments, parse them
    if len(sys.argv) > 1:
        # only ssh is supported in this format
        if sys.argv[1] == "ssh":
            IpAddress = sys.argv[2]
            port = sys.argv[3]
            user = sys.argv[4]
            passwrd = sys.argv[5]
            command = sys.argv[6]

            sshconnect(IpAddress, port, user, passwrd, command)
        else:
            print("Please use other method for telnet")
    else:
        print("\n Please select a option: \n 1. SSH \n 2. Telnet")
        option = int(input("Option:"))
        if option == 1:
            sshinput()
        elif option == 2:
            telnetconnect()
        else:
            print("Wrong option, terminating")

