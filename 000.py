import urllib.parse
msg  = "asdfsadf@123   nihao  "
num = msg.count("@")
if (num>0):
    uid = msg.split("@",num)[num]
    if(uid.count(" ")>0):
        uid = uid.split(" ",1)[0]
    if(uid.isnumeric()):
        uid = int(uid)
        if (uid<1000 and uid >0):
            re_msg = msg.replace("@" + str(uid), "")
            print (uid)
            print(re_msg)
        else:
            pass
    else:
        pass

