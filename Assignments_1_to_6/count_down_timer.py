import time


def countdownTimer(t):
    while t:
        mins, secs = divmod(t , 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print("Timer Completed!!")

t = input("Enter a time in Seconds?  ")
countdownTimer(int(t)) 