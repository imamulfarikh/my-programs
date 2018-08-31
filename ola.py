
sp=input("Enter the starting point")
sp=int(sp)
ep=input("Enter the rnding point")
ep=int(ep)
print ("total distance")
totDist=ep-sp
print(totDist)
#this is a comment
cabType=input("Enter the cab type")
if (cabType=="share"):
  rate=5
if (cabType=="mini"):
 rate=10
if(cabType=="micro"):
  rate=11
if(cabType=="prime"):
  rate=20
print("total cost=")
print(totDist*rate)

