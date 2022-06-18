import socket
import hashlib
import urllib.request
import requests
import whois
import builtwith
import wget
import os
from faker import Faker
from bs4 import BeautifulSoup
from getmac import get_mac_address as gmac
extip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print("\n"+hostname + "\n Private IP " + ipaddr+ "\n Public IP " + extip+"\n MAC Addr "+str(gmac()))
def hashify():
    print("""\n\t 0 for python int hash \n\t 1 for MD5 Hash \n\t 2 for SHA1 Hash \n\t 3 for SHA2 Hash \n\t 4 for SHA3 Hash \n\t 5 for SHA5 Hash""")
    hashval = int(input("Enter your choice of Hashing: "))
    hashify = str(input("Enter the value to hash: "))
    if(hashval == 0):
        print("The hashed value is: " + str(hash(hashify)))
    elif(hashval == 1):
        print("The hashed value is: " + str(hashlib.md5(hashify.encode('utf-8')).hexdigest()))
    elif(hashval == 2):
        print("The hashed value is: " + str(hashlib.sha1(hashify.encode('utf-8')).hexdigest()))
    elif (hashval == 3):
        print("The hashed value is: " + str(hashlib.sha256(hashify.encode('utf-8')).hexdigest()))
    elif(hashval == 4):
        print("The hashed value is: " + str(hashlib.sha384(hashify.encode('utf-8')).hexdigest()))
    elif(hashval == 5):
        print("The hashed value is: " + str(hashlib.sha512(hashify.encode('utf-8')).hexdigest()))
    else:
        print("Invalid choice")

def my_ip_info():
    os.system('ipconfig /all')
    url = requests.get('https://ipinfo.io/')
    soup = BeautifulSoup(url.text, 'lxml')
    #print(soup.title.text)
    #print(soup.text)
    print(soup.string.title())

def sys_info():
    try:
     os.system('systeminfo')
     os.system('wmic baseboard')
     os.system('wmic bios')
     os.system('wmic bootconfig')
     os.system('wmic cdrom')
     os.system('wmic computersystem')
     os.system('wmic cpu')
     os.system('wmic group')
     os.system('wmic desktopmonitor')
     os.system('wmic desktop')
     os.system('wmic diskdrive')
     os.system('wmic devicememoryaddress')
     os.system('wmic logicaldisk')
     os.system('wmic memorychip')
     os.system('wmic memcache')
     os.system('wmic logon')
     os.system('wmic memphysical')
     os.system('wmic netclient')
     os.system('wmic netlogin')
     os.system('wmic netprotocol')
     os.system('wmic netuse')
     os.system('wmic nic')
     os.system('wmic nicconfig')
     os.system('wmic onboarddevice')
     os.system('wmic os')
     os.system('wmic partition')
     os.system('wmic port')
     os.system('wmic printer')
     os.system('wmic process')
     os.system('wmic product')
     os.system('wmic recoveros')
     os.system('wmic registry')
     os.system('wmic server')
     os.system('wmic service')
     os.system('wmic startup')
     os.system('wmic tempertaure')
     os.system('wmic timezone')
     os.system('wmic ups')
     os.system('wmic useraccount')
     os.system('wmic voltage')
     os.system('wmic volume')
     os.system('wmic softwarefeature')
     os.system('wmic sounddev')
     os.system('wmic sysaccpunt')
     os.system('wmic sysdriver')
     print("END")
    except:
        print("Ctrl+C to exit")
def web_info():
    dname = input("Enter the URL to analyse with www: ")
    os.system('nslookup '+dname)
    ip = socket.gethostbyname(dname)
    webinfo = whois.whois(dname)
    print(str(ip)+"\n "+str(webinfo))

def web_tech_use():
    dname = input("Enter the URL to analyse with www: ")
    buiwith = builtwith.parse('https://' + dname)
    print(buiwith)

def w_get():
    url = input("Enter the full URL: ")
    file = wget.download(url)
    cwd = os.getcwd()
    print(cwd+file)

def fake_it():
    val = input("Enter the language Code like en-US, hi-IN: ")
    fake = Faker(val)
    print(fake.name())
    print(fake.address)
    print(fake.email())
    print(fake.country())
    print(fake.profile())
    print(fake.date_of_birth())
    print(fake.latitude(), fake.longitude())
    print(fake.url())

def http_serv():
    try:
     print("it will host on private ip and on current dir".upper())
     os.system('python -m http.server 8080')
    except:
     print("Ctrl+C to exit")

def ftp_serv():
    try:
        print("Start ftp server")
        os.system('python -m pyftpdlib')
    except:
        print("Ctrl+C to exit")

def net_stat():
    try:
        os.system('netstat')
    except:
        print("Ctrl+C to exit")

def trace_route():
    try:
        url = input("Enter IP/URL: ")
        os.system('tracert '+ url)
    except:
        print("Ctrl+C to exit")

def list_ps():
    try:
        os.system('tasklist')
    except:
        print("Ctrl+C to exit")

def list_serv():
    try:
        os.system('sc queryex type=service state=all')
    except:
        print("Ctrl+C to exit")

def driv_moni():
    try:
        os.system('driverquery -v')
    except:
        print("Ctrl+C to exit")

def shut_down():
    try:
        shutval = input("Enter your choice \n\t 1 for Shutdown \n\t 2 for Signing Out \n\t 3 for hibernate \n\t 4 for BIOS \n\t 5 for Bootmenue \n\t 6 for restart \n\t 7 for exit program")
        if(shutval == 0):
            exit()
        elif(shutval == 1):
            os.system('shutdown /s /c "Goodbye shutting down"')
        elif (shutval == 2):
            os.system('shutdown /l /c "Goodbye logging off"')
        elif(shutval == 3):
            os.system('shutdown /h /c "Goodbye hibernating"')
        elif (shutval == 4):
            os.system('shutdown /s /fw /c "Goodbye to bios"')
        elif (shutval == 5):
            os.system('shutdown /r /o /c "Goodbye to Boot menu"')
        elif (shutval == 6):
            os.system('shutdown /r /c "Goodbye Restarting"')
        elif (int(shutval) <= 7):
            exit()
        else:
            print("Invalid choice")
    except:
        print("")
Finalval = int(input("Chose what do you want to do: \n\t 1 for Hashing \n\t 2 for System info \n\t 3 for IP Info \n\t 4 for Website Info \n\t 5 for Tech used by Web \n\t 6 for Get file from Web \n\t 7 for Fake id Generator \n\t 8 for Start HTTP Server \n\t 9 for Start FTP Server \n\t 10 for Network Status \n\t 11 for Trace Route to Web \n\t 12 for List of Process Running \n\t 13 for List of Services running \n\t 14 for Monitoring Drivers \n\t 15 for Shutdown Options: "))
if(Finalval == 1):
    hashify()
elif(Finalval == 2):
    sys_info()
elif(Finalval == 3):
    my_ip_info()
elif(Finalval == 4):
    web_info()
elif(Finalval == 5):
    web_tech_use()
elif(Finalval == 6):
    w_get()
elif(Finalval == 7):
    fake_it()
elif(Finalval == 8):
    http_serv()
elif(Finalval == 9):
    ftp_serv()
elif(Finalval == 10):
    net_stat()
elif(Finalval == 11):
    trace_route()
elif(Finalval == 12):
    list_ps()
elif(Finalval == 13):
    list_serv()
elif(Finalval == 14):
    driv_moni()
elif(Finalval == 15):
    shut_down()
else:
    print("Invalid Choice")
    exit()