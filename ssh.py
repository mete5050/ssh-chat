#ilk olarak /home/ konumunda ssh adlı bir dizin oluşturun.Sonra bu dizine ssh.py yi kaydedin.Bu python3 ssh.py komutu ile çalıştırailirsiniz
import os
normal = '\033[0m'
mor= '\033[35m'
mavi= '\033[36m'
pmavi = '\033[96m'#p --> parlak
pyesil = '\033[92m'
sari= '\033[33m'
print(pmavi)
ad = str(input("Bilgisayar adini giriniz: " ))
ip = str(input("IP adresini giriniz: "))
def read():
    os.system("clear")
    os.system("sudo scp "+ad+"@"+ip+":/home/ssh/message.txt download")
    print(pyesil)
    message = open("download","r")
    print(message.read())
    print(mor)
def send():
    os.system("sudo nano message.txt")
def check():
    print(os.system("sudo ls /home/ssh"))
def remove():
    os.system("sudo rm download")
    print(os.system("ls"))
def connect():
    os.system("ssh "+ad+"@"+ip)
print(pyesil)
while True:
    grs = input(sari + ">>> "+normal)
    if(grs == "read"):
        read()
        remove()
    if(grs == "send"):
        send()
    if(grs == "check"):
        check()
    if(grs == "connect"):
        connect()
    if(grs == "rm"):
        remove()
    if(grs == "rmv"):
        remove()
