import datetime

now= datetime.datetime.now()
print(now.strftime("%H:%M:%S"))
ora=(now.strftime("%H"))
if (int(ora)>16):
    print ("YESS")