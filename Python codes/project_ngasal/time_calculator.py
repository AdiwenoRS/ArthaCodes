hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

exactMinutes = (mins + dura) % 60        #minute converted to minute in an hour
minuteToHour = (mins + dura) // 60      #mins plus duration and take what hours exactly is 

if minuteToHour >= 24:
    exactHourTime = (hour + minuteToHour) % 24
else:
    exactHourTime = minuteToHour + hour
    
print(exactHourTime, exactMinutes, sep=":")



#expectedHour = 