import psutil
import time
from datetime import datetime


print("Monitoring usage")
try:
    while True:
        cpu_percent_now = psutil.cpu_percent(interval=1)

        if cpu_percent_now >= 80:
            print(datetime.now(), "- ALERT! CPU high:", cpu_percent_now)

        else:
            print(datetime.now(), "- CPU normal:", cpu_percent_now)

        time.sleep(1)
    
except KeyboardInterrupt:
    print("Interptuded by user")
except Exception as e:
    print("unexpected error" , e)
    
