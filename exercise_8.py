import time

for hour in range(0,24,1):
    for minute in range(0,60,1):
        for second in range(0,60,1):
            print("\r",hour, ":",minute, ":",second,end="")
            time.sleep(1)






