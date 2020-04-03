import qrcode
import os
os.system("apt install toilet")
os.system("clear")
os.system("toilet -fmono12 -F gay QR-CODE")
print("    \033[1;36;40m Code made by: \033[1;32;40m Brijesh Kumar")
print("    \033[1;36;40m Instagram id: \033[1;32;40m www.instagram.com/x_ploits")
print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/anonymousmani")
print("\n\n")
ur=input(" enter your url[$] ")
pth=input("enter path with file name[$] ")
print("your qrcode is generating")
f=qrcode.make(ur)
f.save(pth)
