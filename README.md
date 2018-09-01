# my-programs
python

sp=input("enter the starting point = ")
sp=int(sp)
ep=input("enter the ending point  = ")
ep=int(ep)
totdist=ep-sp
print("total distance  = ",totdist," Km")
cabType=input("enter the cabtype  = ")
if (cabType=="share"):
 rate=5
if(cabType=="prime"):
 rate=10
if (cabType=="mini"):
 rate=15
if (cabType=="micro"):
 rate=20
if(cabType=="auto"):
  rate=4
tc=totdist*rate
print("total cost   = Rs.",tc)
