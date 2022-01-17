import sys

sys.path.append(".")
from Data_Collector import DataCollector
from FCFS_algo import FCFS
from Grantt_Analysis import GranttAnalysis
from SJF_algo import SJF
from RR_algo import RoundRobin

csv_input_path = 'test/process_input_data.csv'

data_collector = DataCollector(csv_path=csv_input_path)
# ------------------- FCFS -------------------
# fcfs = FCFS(processes=data_collector.getProcesses())
# grantt_chart = fcfs.cpu_process()
# ------------------- SJF --------------------
# sjf = SJF(processes=data_collector.getProcesses())
# grantt_chart = sjf.cpu_process()
# ------------------- RR ---------------------
rr = RoundRobin(processes=data_collector.getProcesses())
grantt_chart = rr.cpu_process(time_quantum=5)

analysis = GranttAnalysis(grantt_chart=rr.grantt_chart)
analysis.pretty_print('sjf')
