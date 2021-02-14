import urllib.request, json 
import time
from threading import Thread
from threading import Event
import os
import numpy as np

arrivalRate= [1280, 800, 640, 480, 320, 160, 160, 320, 2720, 5920, 9280, 12480, 13900, 15520, 15840, 16800, 16640, 13920, 11200, 9120, 6400, 4480, 2880, 1600]
granuality= 60 
arrivalRatePerSecond = [rate/granuality for rate in arrivalRate]
# number_request =[]

class NetData(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        # run this for a lot of time
        while not self.stopped.wait(1):
            for index in range(len(arrivalRatePerSecond)):
                for run_time in range(granuality):
                    if(index == (len(arrivalRatePerSecond) - 1)):
                        a = arrivalRatePerSecond[index] + (arrivalRatePerSecond[0] - arrivalRatePerSecond[index])*(run_time + 1)/granuality
                    else :
                        a = arrivalRatePerSecond[index] + (arrivalRatePerSecond[index + 1] - arrivalRatePerSecond[index])*(run_time + 1)/granuality
                    number_request = np.random.poisson(a)
                    # print(str(np.random.poisson(a)) + "  "+ str(a))
                    # number_request.append(np.random.poisson(a))
                    # self.stopped.wait(1)
                    # rate = np.random.poisson(arrivalRate/granuality, 1)
                    # # exception control here: 
                    # # TODO: add timeout exception:
                    # # with urllib.request.urlopen("http://" + os.environ['SERVER_IP']  + ":8983/solr/demo/select?q=*%3A*") as url:
                    for i in range(number_request):
                        with urllib.request.urlopen("http://" + os.environ['SERVER_IP']  + ":8983/solr/demo/select?q=*%3A*") as url:
                            data = json.loads(url.read().decode())
                        print(data)
    def getData():
        pass


# netData = NetData()
# print(netData.getMetric())

stopFlag = Event()
thread = NetData(stopFlag)
thread.start()
# print("http://" + "os.environ['SERVER_IP']" + ":8983/solr/demo/select?q=*%3A*")
# this will stop the timer
# stopFlag.set()