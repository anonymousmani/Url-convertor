import qrcode
ur=input(" enter your url")

pth=input("enter path with file name")
print("your qrcode is generating")
f=qrcode.make(ur)
f.save(pth)
