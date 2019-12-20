import subprocess
import time
import os
import sys





class Mitm_Proxy:

    def __init__(self):
        self.process =subprocess.Popen("mitmdump -s mitm_script.py > main.log", shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)


    # def open_process(self):
    #     # process = subprocess.Popen("mitmdump -s mitm_script.py > logs.log", stdin=subprocess.PIPE,
    #     #                            stdout=subprocess.PIPE, shell=True)
    #     print("before subprooces start")
    #
    #     print("after subprooces start")
    #
    #     # process.terminate()




    def terminate_proxy(self):
        self.process.terminate()




