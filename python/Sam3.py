from datetime import datetime
import time

if __name__ == '__main__':
    for _ in range(5):
        now = datetime.now()
        print(now.strftime("%H:%M:%S"))
        time.sleep(1)