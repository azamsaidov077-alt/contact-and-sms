import time, os
from time import sleep

from threading import Thread,current_thread
from multiprocessing import Process,current_process

def io_b(sec):
    p_id = os.getpid()
    print(f"{p_id}---{current_thread().name}---{current_thread().name}--kutish boshlandi")
    time.sleep(sleep)
    print(f"{p_id}---{current_thread().name}---{current_thread().name}--kutish yakunlandi")

def cpu_b(k):
    p_id = os.getpid()
    print(f"{p_id}---{current_thread().name}---{current_thread().name}-- boshlandi")
    while k>0:
        k-=1

    print(f"{p_id}---{current_thread().name}---{current_thread().name}-- boshlandi")

if __name__ == '__main__':
    s_time = time.time()
    # 1-sinle thread io_b
