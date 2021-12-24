

## Basic Usage
```python
from simfaas.ServerlessSimulator import ServerlessSimulator as Sim

sim = Sim(arrival_rate=0.9, warm_service_rate=1/1.991, cold_service_rate=1/2.244,
            expiration_threshold=600, max_time=1e6)
sim.generate_trace(debug_print=False, progress=True
sim.print_trace_results()
```
## Parameters
### arrival_process 
** simfaas.SimProcess**.SimProcess, optional
        The process used for generating inter-arrival samples, if absent, `arrival_rate` should be passed to signal exponential distribution, by default None
### warm_service_process 
 simfaas.SimProcess.SimProcess, optional
        The process which will be used to calculate service times, if absent, `warm_service_rate` should be passed to signal exponential distribution, by default None
### cold_service_process 
simfaas.SimProcess.SimProcess, optional
        The process which will be used to calculate service times, if absent, `cold_service_rate` should be passed to signal exponential distribution, by default None
###  expiration_threshold 
float, optional
        The period of time after which the instance will be expired and the capacity release for use by others, by default 600
### max_time
 float, optional
        The maximum amount of time for which the simulation should continue, by default 24*60*60 (24 hours)
###  maximum_concurrency 
 int, optional
        The maximum number of concurrently executing function instances allowed on the system This will be used to determine when a rejection of request should happen due to lack of capacity, by default 1000
## Init: Choose SimProcess Model
#### ConstSimProcess
generateTrace===1/rate
if rate=5 this is a deterministic process and fires exactly every 0.2 seconds
#### GaussianSimProcess
generateTrace return gaussian field
visualize range 10000 dot on field
visualize result:
Simulated Average Inter-Event Time y-axis
Simulated Average Event Rate x-axis
![Figure_1.png](https://cdn.nlark.com/yuque/0/2021/png/22650027/1639584543831-5693ed13-87c9-4a62-9947-2cef301c4567.png#clientId=ucf4824e3-98ad-4&crop=0&crop=0&crop=1&crop=1&from=ui&id=uc988bfe7&margin=%5Bobject%20Object%5D&name=Figure_1.png&originHeight=613&originWidth=1280&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36784&status=done&style=none&taskId=ubacb22b8-bc1a-4dc7-adf7-6128295a854&title=)
####  ExpSimProcess
exponential rate=1/rate
![Figure_2.png](https://cdn.nlark.com/yuque/0/2021/png/22650027/1639584656390-16c221a5-0a8d-4d36-bbfa-6ed1ead53d8e.png#clientId=ucf4824e3-98ad-4&crop=0&crop=0&crop=1&crop=1&from=ui&id=uee992d54&margin=%5Bobject%20Object%5D&name=Figure_2.png&originHeight=480&originWidth=640&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20627&status=done&style=none&taskId=u7373edab-541c-4afc-a1ed-31874fe80a2&title=)
if kwargs.get==arrival_rate  or warm_service_rate or cold_service_rate  **use this default modal**
## Compute: Generating trace
## Init: Function Instance
Goes through the process necessary for a cold start arrival which includes generation of a new function instance in the `COLD` state and adding it to the cluster.
input:

- creation time
- warm service process
- cold service process
- expiration_threshold

 
## Change:the State of Function Instance
## Analyze: Performance and Cost of the system 
### process model effect
[ConstSimProcess](https://www.yuque.com/kkkokra/lz3l47/gw7i50/edit#pFSON) [GaussianSimProcess](https://www.yuque.com/kkkokra/lz3l47/gw7i50/edit#Joxl4) [ExpSimProcess](https://www.yuque.com/kkkokra/lz3l47/gw7i50/edit#JwEss)
#### Gassian process
**input**

| arrival process | rate=5, std=0.01 |
| --- | --- |
| warm_service_rate | 1/1.991 |
| cold_service_rate​ | 1/2.244 |
| expiration_threshold | 600 |
| max_time | 1e6 |

**output**

| Cold Starts / total requests |  1374 / 4999937 |
| --- | --- |
| Cold Start Probability        |  0.0003 |
| Rejection / total requests |   0 / 4999937 |
| Rejection Probability | 0 |
| Average Instance Life Span | 13354.9118 |
| Average Server Count            |  18.2016 |
| Average Running Count           | 9.9538 |
| Average Idle Count               | 8.2478 |

#### Const process
**input**

| arrival process | rate=5 |
| --- | --- |
| warm_service_rate | 1/1.991 |
| cold_service_rate​ | 1/2.244 |
| expiration_threshold | 600 |
| max_time | 1e6 |

**output**

| Cold Starts / total requests | 1312 / 5000001 |
| --- | --- |
| Cold Start Probability        | 0.0003 |
| Rejection / total requests |  0 / 5000001 |
| Rejection Probability | 0 |
| Average Instance Life Span | 13944.0496 |
| Average Server Count            | 18.2016 |
| Average Running Count           | 9.9514 |
| Average Idle Count               | 8.2357 |

#### Expo process
**input**

| arrival process | rate=0.9 |
| --- | --- |
| warm_service_rate | 1/1.991 |
| cold_service_rate​ | 1/2.244 |
| expiration_threshold | 600 |
| max_time | 1e6 |

**output**

| Cold Starts / total requests |  1222 / 898813 |
| --- | --- |
| Cold Start Probability        |  0.0014 |
| Rejection / total requests |  0 / 898813 |
| Rejection Probability |  0 |
| Average Instance Life Span | 6318.9096 |
| Average Server Count            | 7.6987 |
| Average Running Count           | 1.7907 |
| Average Idle Count               | 5.9080 |

