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

class NetData():
    def __init__(self):
        # Thread.__init__(self)
        # self.stopped = event
        pass

    def run(self):
        # run this for a lot of time
        while True:
            for days in range(7):
                scale = np.random.uniform(low=0.9, high=1.1)
                for index in range(len(arrivalRatePerSecond)):
                    for run_time in range(granuality):
                        if(index == (len(arrivalRatePerSecond) - 1)):
                            a = arrivalRatePerSecond[index] + (arrivalRatePerSecond[0] - arrivalRatePerSecond[index])*(run_time + 1)/granuality
                        else :
                            a = arrivalRatePerSecond[index] + (arrivalRatePerSecond[index + 1] - arrivalRatePerSecond[index])*(run_time + 1)/granuality
                        number_request = int(a * scale)
                        # print("arrivalRatePerSecond: " + str(arrivalRatePerSecond[index]) + " | " + "run_time" + str(run_time) + " | " + "a " + str(a))
                        # print(str(np.random.poisson(a)) + "  "+ str(a))
                        # number_request.append(np.random.poisson(a))
                        # self.stopped.wait(1)
                        # rate = np.random.poisson(arrivalRate/granuality, 1)
                        # # exception control here: 
                        # # TODO: add timeout exception:
                        #TODO: timer is prolong due to timer clock.
                        # # with urllib.request.urlopen("http://" + os.environ['SERVER_IP']  + ":8983/solr/demo/select?q=*%3A*") as url:
                        start = time.perf_counter()
                        count = 0
                        for i in range(number_request):
                            count = count + 1
                            end = time.perf_counter()
                            if (end - start > 1):
                                # print("number_request " + str(number_request) + " | "+ "count" + str(count))
                                break
                            with urllib.request.urlopen("http://" + os.environ['SERVER_IP'] + ":"  + os.environ['SERVER_PORT'] + "/solr/demo/select?q=*%3A*") as url:
                            # with urllib.request.urlopen("http://192.168.2.83:8983/solr/demo/select?q=*%3A*") as url:
                                data = json.loads(url.read().decode())
                        # end = time.perf_counter()
                        # print(end - start)
                            # sleep_time = ((1000 - 2.5*number_request)/number_request)/1000
                            end2 = time.perf_counter()
                            if((end2 - end) > 1/number_request):
                                sleep_time = (end2 - end)
                            else :
                                sleep_time = 1/number_request - (end2 - end)
                            # print("sleep time" + str(sleep_time))
                            time.sleep(sleep_time)
                            # print(data)
                        # print("number_request " + str(number_request) + " | "+ "count" + str(count))
    def getData():
        pass


netData = NetData()
netData.run()
# print(netData.getMetric())

# stopFlag = Event()
# thread = NetData(stopFlag)
# thread.start()
# print("http://" + "os.environ['SERVER_IP']" + ":8983/solr/demo/select?q=*%3A*")
# this will stop the timer
# stopFlag.set()
# import time

# start = time.perf_counter()
# for i in range(300):
#     time.sleep(1/300)
# end = time.perf_counter()
# print(end - start)