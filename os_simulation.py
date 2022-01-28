import sys

sys.path.append(".")
from Data_Collector import DataCollector
from FCFS_algo import FCFS
from Grantt_Analysis import GranttAnalysis
from SJF_algo import SJF
from MLFQ_algo import MLFQ
from Process import Process
from RR_algo import RoundRobin

csv_input_path = 'test/process_input_data.csv'

while True:
    print('\033[94m' + '--------------------------------------')
    print('FCFS = 1 | SJF = 2 | RR = 3 | MLFQ = 4')
    print('--------------------------------------' + '\033[0m')
    data_collector = []
    try:
        mode = int(input('Enter: '))
    except Exception as error:
        print('\033[93m' + 'Error: Wrong Input!')
        exit(-1)
    data_collector = DataCollector(csv_path=csv_input_path)
    # ------- get a deep copy of processes -------
    processes_copy = []
    result = None
    for process in data_collector.getProcesses().copy():
        processes_copy.append(Process(process.process_id,
                                      process.arrival_time,
                                      process.cpu_burst_time1,
                                      process.io_time,
                                      process.cpu_burst_time2))
    if mode == 1:
        # ------------------- FCFS -------------------
        result = FCFS(processes=data_collector.getProcesses())
        grantt_chart = result.cpu_process()
    elif mode == 2:
        # ------------------- SJF --------------------
        result = SJF(processes=data_collector.getProcesses())
        grantt_chart = result.cpu_process()
    elif mode == 3:
        # ------------------- RR ---------------------
        result = RoundRobin(processes=data_collector.getProcesses().copy())
        grantt_chart = result.cpu_process(time_quantum=1)
    elif mode == 4:
        # ------------------ MLFQ --------------------
        result = MLFQ(processes=data_collector.getProcesses().copy())
        grantt_chart = result.cpu_process()
    else:
        exit(0)
    if result is not None:
        analysis = GranttAnalysis(grantt_chart=result.grantt_chart, processes=processes_copy)
        analysis.pretty_print(result.ClassName)
