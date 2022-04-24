import pynvml
import os
import time

pynvml.nvmlInit()

while True:
    time.sleep(1800)
    print('every thing is ok.')
    if pynvml.nvmlDeviceGetMemoryInfo(pynvml.nvmlDeviceGetHandleByIndex(4)).used < 100000000 and \
            pynvml.nvmlDeviceGetMemoryInfo(pynvml.nvmlDeviceGetHandleByIndex(5)).used < 100000000 and \
            pynvml.nvmlDeviceGetMemoryInfo(pynvml.nvmlDeviceGetHandleByIndex(6)).used < 100000000 and \
            pynvml.nvmlDeviceGetMemoryInfo(pynvml.nvmlDeviceGetHandleByIndex(7)).used < 100000000:
        print('error, try to restart.')
        #resume_file = os.popen('ls *.pth.tar').read().split()[-1]
        today_data = str(time.localtime(time.time())[1]) + str(time.localtime(time.time())[2])+ str(time.localtime(time.time())[3])+ str(time.localtime(time.time())[4])
        command = "export CUDA_VISIBLE_DEVICES=4,5,6,7;nohup sh train.sh > log 2>&1 &"
        print(command)
        os.system(command)
        time.sleep(300)
