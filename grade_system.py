math=int(input("Enter your math marks"))
science=int(input("Enter your science marks"))
english=int(input("Enter you english marks"))
urdu=int(input("Enter your urdu marks"))
marks01=math+science+english+urdu
marks=marks01/4
if marks>=90:
    print("You have A grade.")
elif marks>=75:
    print("You have B grade.")
elif marks>=50:
    print("You have C grade.")
elif marks>=35:
    print("You have D grade.")
else:
    print("You are fail.")