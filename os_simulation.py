import sys

sys.path.append(".")
from Data_Collector import DataCollector
from FCFS_algo import FCFS
from Grantt_Analysis import GranttAnalysis

csv_input_path = 'test/process_input_data.csv'

data_collector = DataCollector(csv_path=csv_input_path)
fcfs = FCFS(processes=data_collector.getProcesses())
analysis = GranttAnalysis(grantt_chart=fcfs.grantt_chart)
analysis.pretty_print('fcfs')
