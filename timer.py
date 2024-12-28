# Time Countdown
import time

my_time = int(input("Enter the time in seconds: "))

for remaining_time in range(my_time,0,-1):
    seconds = int (remaining_time%60)
    minutes = int (remaining_time/60)%60
    hours = int (remaining_time/(60*60))

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
    time.sleep(1)

print("Time's up!")