import sys

sys.path.append(".")
from Grantt_Information import ProcessGrantInfo


class RoundRobin:
    processes = []
    grantt_chart = []

    def __init__(self, processes):
        self.processes = processes

    def cpu_process(self):
        arrival_time = self.get_arrival_times()
        current_cpu_time = 0
        first_ready_processes_queue_A = []
        first_ready_processes_queue_B = []
        ready_for_io_queue = []

        while True:
            count = 0
            if count == len(self.processes):
                for process in self.processes:
                    if process.arrival_time <= current_cpu_time:
                        first_ready_processes_queue_A.append(process)
                        count += 1

            if len(first_ready_processes_queue_A and first_ready_processes_queue_B) == 0:
                current_cpu_time += 1
            else:
                process = first_ready_processes_queue_A.pop()
                if len(self.grantt_chart) == 0:
                    self.grantt_chart.append(ProcessGrantInfo(
                        process,
                        current_cpu_time,
                        0, 0, 0, 0, 0
                    ))
                else:
                    step = 5
                    if process.cpu_burst_time1 < 5:
                        step = process.cpu_burst_time1





    def get_arrival_times(self):
        _temp = []
        for process in self.processes:
            _temp.append(process.arrival_time)
        return _temp

