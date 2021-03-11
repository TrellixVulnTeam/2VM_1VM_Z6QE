import os
import json
import multiprocessing
import time
from p2_multi import process_docker
from p2_multi import monitor_ad


sets = ["NoIntent_News","NoIntent_Sports","Intent_News","Intent_Sports"]

for s in sets:

    p1 = multiprocessing.Process(target=process_docker, args=(s,range(1,26)))

    p1.start()

    
    break


    # b1 = multiprocessing.Process(target=monitor_ad, args=(s,range(1,26)))

    # b1.start()