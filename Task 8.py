def convert_to_time(num):
    if(num // 60 > 0):
        hours = num // 60
        minutes = 0
        if(num % 60 > 0):
            minutes = num % 60
        if(minutes > 0):
            if(minutes > 1):
                print(str(hours)+" hours, "+ str(minutes)+" minutes.")
            else:
                print(str(hours)+" hours, "+ str(minutes)+" minute.")
        else:
            print(str(hours)+" hours.")
    else:
        minutes = num
        if(minutes != 1):
            print(str(minutes)+" minutes.")
        else:
            print(str(minutes)+" minute.")
convert_to_time(350) 
