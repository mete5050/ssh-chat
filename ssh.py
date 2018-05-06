import os
normal = '\033[0m'
mor= '\033[35m'
mavi= '\033[36m'
pmavi = '\033[96m'
pyesil = '\033[92m'
sari= '\033[33m'
print(pmavi)
ad = str(input("Bilgisayar adini giriniz: " ))#bağlanıcağımız bilgisayarın adını giriyotuz Ör: mete , pi , mypc gibi Not:Bilgisayar adını adresini bağlanıcağımız bilgisayarın terminaline "whoami" yazarak öğrenebilirsiniz
ip = str(input("IP adresini giriniz: "))#bağlanıcağımız bilgisayarın ip adresini  giriyotuz Ör:192.168.123 , 192.168.1.143 gibi Not:İP adresini bağlanıcağımız bilgisayarın terminaline "ifconfig" yazarak öğrenebilirsiniz
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
    os.system("sudo rm message.txt")
    print(os.system("ls"))
def connect():
    os.system("ssh "+ad+"@"+ip)
print(pyesil)
while True:
    grs = input(sari + ">>> "+normal)
    if(grs == "oku"):
        read()
        remove()
    if(grs == "yaz"):
        remove
        send()
    if(grs == "kontrol"):
        check()
    if(grs == "bağlan"):
        connect()
    if(grs == "sil"):
        renmove()
