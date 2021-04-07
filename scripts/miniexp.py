import os
import json
import multiprocessing
import time
from p2_multi import process_docker
from p2_multi import monitor_ad


sets = ["NoIntent_Adult","Intent_Adult","NoIntent_Sports","Intent_Sports","NoIntent_Recreation","Intent_Recreation"]

for s in sets:

    p1 = multiprocessing.Process(target=process_docker, args=(s,range(1,26)))
    p2 = multiprocessing.Process(target=process_docker, args=(s,range(26,51)))

    p1.start()
    p2.start()

    b1 = multiprocessing.Process(target=monitor_ad, args=(s,range(1,26)))
    b2 = multiprocessing.Process(target=monitor_ad, args=(s,range(26,51)))
    b1.start()
    b2.start()