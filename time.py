import time

if time.asctime( time.localtime(time.time()))[0:3] == "Mon":
    print("Day:",time.asctime( time.localtime(time.time()))[0:3]+"day")
elif time.asctime( time.localtime(time.time()))[0:3] == "Tue":
    print("Day:",time.asctime( time.localtime(time.time()))[0:3]+"sday")
elif time.asctime( time.localtime(time.time()))[0:3] == "Wed":
    print("Day:",time.asctime( time.localtime(time.time()))[0:3]+"nesday")
elif time.asctime( time.localtime(time.time()))[0:3] == "Thu":
    print("Day:",time.asctime( time.localtime(time.time()))[0:3]+"rsday")
elif time.asctime( time.localtime(time.time()))[0:3] == "Fri":
    print("Day:",time.asctime( time.localtime(time.time()))[0:3]+"day")
elif time.asctime( time.localtime(time.time()))[0:3] == "Sat":
    print("Day:",time.asctime( time.localtime(time.time()))[0:3]+"urday")
elif time.asctime( time.localtime(time.time()))[0:3] == "Sun":
    print("Day:",time.asctime( time.localtime(time.time()))[0:3]+"day")
print("Month:",time.asctime( time.localtime(time.time()))[4:7])
print("Day Number:",time.asctime( time.localtime(time.time()))[8:10])
print("Time:",time.asctime( time.localtime(time.time()))[10:16])
print("Year:",time.asctime( time.localtime(time.time()))[20:])


# time.asctime(time.localtime(time.time()))
# asctime'ın localtime'ının time.time'ı
