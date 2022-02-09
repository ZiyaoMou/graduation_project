'''
Author: your name
Date: 2021-12-20 22:35:52
LastEditTime: 2022-02-09 03:37:20
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /simfaas/test.py
'''
import csv
import random
from numpy import histogram
from simfaas.ServerlessSimulator import ServerlessSimulator as Sim
from simfaas.SimProcess import ReqSimProcess
from simfaas.Histogram import Histogram 
f=csv.reader(open('invocations_per_function_md.anon.d13.csv'))
rows=[row for row in f]
gaps=[]
for i in range(0,2):
    gap=rows[i][4:]
    gaps.append(gap)
time_gap_list=[[] for i in range(1)]
time_list=[[] for i in range(1)]
row_count=0
for row in gaps:
    count=0
    for i in row:
        i=int(i)
        if(i!=0):
            j=i
            while j:
                random.seed()
                time_list[row_count].append(round(count*60+random.random()*60,1))
                time_list[row_count].sort()
                time_before=0
                for time in time_list[row_count]:
                    time_gap=round(time-time_before)
                    time_gap_list[row_count].append(time_gap)
                    time_before=time
                j-=1
        count=count+1
        continue
hist=Histogram()
print(gaps[1])
hist.visualize_limited_ranged_histogram(current_time=1000*60,it_list=gaps[1])
# sim = Sim(arrival_process=ReqSimProcess(time=time_gap_list[0]),warm_service_rate=1/1.991,cold_service_rate=1/2.244,
# expiration_threshold=600,max_time=2e5,preset_servers_count=1)
# sim.generate_trace(debug_print=False,progress=True)
# sim.print_trace_results()
#print (time_gap_list)
# for i in time_gap_list:
#     time_gap_list[i]=
