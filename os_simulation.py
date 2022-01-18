import sys

sys.path.append(".")
from Data_Collector import DataCollector
from FCFS_algo import FCFS
from Grantt_Analysis import GranttAnalysis
from SJF_algo import SJF
from Process import Process
from RR_algo import RoundRobin

csv_input_path = 'test/process_input_data.csv'

data_collector = DataCollector(csv_path=csv_input_path)
# ------------------- FCFS -------------------
# fcfs = FCFS(processes=data_collector.getProcesses())
# grantt_chart = fcfs.cpu_process()
# ------------------- SJF --------------------
# sjf = SJF(processes=data_collector.getProcesses())
# grantt_chart = sjf.cpu_process()
# ------- get a deep copy of processes -------
processes_copy = []
for process in data_collector.getProcesses().copy():
    processes_copy.append(Process(process.process_id,
                                  process.arrival_time,
                                  process.cpu_burst_time1,
                                  process.io_time,
                                  process.cpu_burst_time2))
# ------------------- RR ---------------------


rr = RoundRobin(processes=data_collector.getProcesses().copy())
grantt_chart = rr.cpu_process(time_quantum=5)

analysis = GranttAnalysis(grantt_chart=rr.grantt_chart, processes=processes_copy)
analysis.pretty_print('RR')
