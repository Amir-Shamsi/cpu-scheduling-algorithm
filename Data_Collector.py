import pandas
import sys

sys.path.append(".")
from Process import Process

class DataCollector:
    processes = []
    csv_file_path = ''

    def __init__(self, csv_path):
        self.csv_file_path = csv_path
        self.openCsvFile(self.csv_file_path)

    def openCsvFile(self, path):
        file = pandas.read_csv(path)
        for index in range(len(file)):
            self.processes.append(Process(int(file['process_id'][index]),
                                          int(file['arrival_time'][index]),
                                          int(file['cpu_time1'][index]),
                                          int(file['io_time'][index]),
                                          int(file['cpu_time2'][index])
                                          ))

    def getProcesses(self):
        self.sort()
        return self.processes

    def sort(self):
        sorted_processes = []
        arrival_times = []
        for process in self.processes:
            arrival_times.append(process.arrival_time)
        arrival_times.sort()
        for arrival_time in arrival_times:
            for process in self.processes.copy():
                if process.arrival_time == arrival_time:
                    sorted_processes.append(process)
                    self.processes.remove(process)
        self.processes.clear()
        self.processes = sorted_processes.copy()