'''
Author: your name
Date: 2021-12-20 22:35:52
LastEditTime: 2021-12-22 09:49:20
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /simfaas/test.py
'''
import csv
import random
from simfaas.ServerlessSimulator import ServerlessSimulator as Sim
from simfaas.SimProcess import ReqSimProcess
f=csv.reader(open('invocations_per_function_md.anon.d13.csv'))
rows=[row for row in f]
gaps=[]
for i in range(1,2):
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
                time_list[row_count].append(round(count+random.random(),1))
                time_list[row_count].sort()
                time_before=0
                for time in time_list[row_count]:
                    time_gap=round(time-time_before,2)
                    time_gap_list[row_count].append(time_gap)
                    time_before=time
                j-=1
        count=count+1
        continue
sim = Sim(ReqSimProcess(time=time_gap_list[0]),warm_service_rate=1/1.991,cold_service_rate=1/2.244,
expiration_threshold=600,max_time=1e4)
sim.generate_trace(debug_print=False,progress=True)
sim.print_trace_results()
#print (time_gap_list)
# for i in time_gap_list:
#     time_gap_list[i]=
