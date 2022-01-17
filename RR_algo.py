import sys

sys.path.append(".")
from Grantt_Information import ProcessGrantInfo


class RoundRobin:
    processes = []
    grantt_chart = []

    def __init__(self, processes):
        self.processes = processes

    def cpu_process(self, time_quantum):
        current_cpu_time = 0
        prev_cpu_time = 0
        not_started = False
        ready_processes_queue = []
        processes_next_ready_time = self.get_arrival_times()

        while True:
            if not not_started:
                first_process = self.processes[0]
                self.processes.remove(first_process)
                ready_processes_queue.append(first_process)
                for process in self.processes.copy():
                    if process.arrival_time == first_process.arrival_time:
                        ready_processes_queue.append(process)
                        self.processes.remove(process)
                not_started = True

            current_process = ready_processes_queue.pop(0)

            if current_process.cpu_burst_time1 > 0 and current_cpu_time.arrival_time <= current_cpu_time:
                current_process.cpu_burst_time1 -= time_quantum
                current_cpu_time = current_process.cpu_burst_time1 + time_quantum
            if current_process.cpu_burst_time1 <= 0:
                if current_process.io_time > 0:
                    processes_next_ready_time[current_process.process_id] = current_cpu_time + current_process.io_time
                elif current_process.cpu_burst_time2 > 0 and processes_next_ready_time[current_process.process_id] <= current_cpu_time:
                    current_process.cpu_burst_time2 -= time_quantum
            
            if current_process.cpu_burst_time2 + current_process.cpu_burst_time1 + current_process.io_time > 0:
                ready_processes_queue.append(current_process)

            if prev_cpu_time == current_cpu_time:
                current_cpu_time += 1
            prev_cpu_time = current_cpu_time




    def get_arrival_times(self):
        _temp = []
        for process in self.processes:
            _temp[process.process_id] = process.arrival_time
        return _temp

