'''
Author: your name
Date: 2022-02-08 03:26:38
LastEditTime: 2022-02-09 03:23:47
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /simfaas/simfaas/simfaas/Histogram.py
'''
import matplotlib
import matplotlib.pyplot as plt

class Histogram:
    def __init__(self, range = 4*60*60, bin = 1*60):
        """
        Histogram is a statistical treatment for a certain range of requests pattern

        Parameters
        ----------
        range: the maximum limited scale of histogram 
        bin: the bin of histogram
        IT_list: the IT array of latest range of request

        Raises
        ------
        Exception
        Raises if 

        """
        super().__init__()
        self.bin = bin
        self.range = range
        self.tail_time = 0
        self.head_time = 0
        self.current_time = 0
        
        
    def update_histogram(self,current_time):
        self.current_time = current_time
        if current_time > self.range:
            tail_time = current_time
            head_time = current_time - self.range
        else:
            head_time = 0
            tail_time = current_time
        self.tail_time = tail_time
        self.head_time = head_time
        return self

    def visualize_limited_ranged_histogram(self,it_list,current_time):
        self=self.update_histogram(current_time)
        head=int(self.head_time/60)
        tail=int(self.tail_time/60)
        it_list=it_list[head:tail]
        x_axis=[]
        for i in range(head,tail):
            x_axis.append(i)
        y_axis=it_list[:]
        print(x_axis)
        plt.bar(x_axis,y_axis)
        plt.legend()
        plt.xlabel("time in range")
        plt.ylabel("invocation times per minutes")
        plt.title("histogram")
        plt.show()