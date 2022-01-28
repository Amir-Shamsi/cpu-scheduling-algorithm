import sys

sys.path.append(".")
from Grantt_Information import ProcessGrantInfo


def sorted_based_on_burst_time(queue):
    sorted_processes = []
    processes = queue.copy()
    burst_times = []
    for process in processes:
        burst_times.append(process.cpu_burst_time1 + process.cpu_burst_time2)
    burst_times.sort()
    for burst_time in burst_times:
        for process in processes.copy():
            if process.cpu_burst_time1 + process.cpu_burst_time2 == burst_time:
                sorted_processes.append(process)
                processes.remove(process)
    return sorted_processes.copy()


class SJF:
    processes = []
    grantt_chart = []
    ClassName = 'SJF'

    def __init__(self, processes):
        self.processes = processes

    def cpu_process(self):
        not_started = False
        ready_processes_queue = []

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
            ready_processes_queue = sorted_based_on_burst_time(ready_processes_queue)
            current_process = ready_processes_queue[0]
            ready_processes_queue.remove(current_process)

            if len(self.grantt_chart) == 0:
                self.grantt_chart.append(
                    ProcessGrantInfo(current_process,
                                     current_process.arrival_time,  # first cpu start
                                     current_process.arrival_time + current_process.cpu_burst_time1,  # io start time
                                     current_process.arrival_time + current_process.cpu_burst_time1 + current_process.io_time,  # sec cpu start
                                     current_process.arrival_time + current_process.cpu_burst_time1,  # first cpu end
                                     current_process.arrival_time + current_process.cpu_burst_time1 + current_process.io_time,  # io end time
                                     current_process.arrival_time + current_process.cpu_burst_time1 + current_process.io_time + current_process.cpu_burst_time2)  # sec cpu end
                )
            else:
                prev_process_grantt = self.grantt_chart[len(self.grantt_chart) - 1]
                if current_process.arrival_time < prev_process_grantt.get_end_time():
                    self.grantt_chart.append(
                        ProcessGrantInfo(current_process,
                                         prev_process_grantt.get_end_time() + 0,  # first cpu start
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1,
                                         # io start time
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1 + current_process.io_time,
                                         # sec cpu start
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1,
                                         # first cpu end
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1 + current_process.io_time,
                                         # io end time
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1 + current_process.io_time + current_process.cpu_burst_time2)
                        # sec cpu end
                    )
                else:
                    self.grantt_chart.append(
                        ProcessGrantInfo(current_process,
                                         current_process.arrival_time,  # first cpu start
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1,
                                         # io start time
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1 + current_process.io_time,
                                         # sec cpu start
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1,
                                         # first cpu end
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1 + current_process.io_time,
                                         # io end time
                                         prev_process_grantt.get_end_time() + current_process.cpu_burst_time1 + current_process.io_time + current_process.cpu_burst_time2)
                        # sec cpu end
                    )

            cpu_current_time = self.grantt_chart[len(self.grantt_chart) - 1].get_end_time()

            for process in self.processes.copy():
                if process.arrival_time <= cpu_current_time:
                    ready_processes_queue.append(process)
                    self.processes.remove(process)

            if len(self.processes) + len(ready_processes_queue) <= 0:
                break
