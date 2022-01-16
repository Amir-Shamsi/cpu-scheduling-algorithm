import sys

sys.path.append(".")
from Grantt_Information import ProcessGrantInfo


class FCFS:
    processes = []
    grantt_chart = []

    def __init__(self, processes):
        self.processes = processes

    def cpu_process(self):
        for process in self.processes:
            if len(self.grantt_chart) == 0:
                self.grantt_chart.append(
                    ProcessGrantInfo(process,
                                     0,  # first cpu start
                                     process.cpu_burst_time1,  # io start time
                                     process.cpu_burst_time1 + process.io_time,  # sec cpu start
                                     process.cpu_burst_time1,  # first cpu end
                                     process.cpu_burst_time1 + process.io_time,  # io end time
                                     process.cpu_burst_time1 + process.io_time + process.cpu_burst_time2)  # sec cpu end
                )
            else:
                prev_process_grantt = self.grantt_chart[len(self.grantt_chart) - 1]
                self.grantt_chart.append(
                    ProcessGrantInfo(process,
                                     prev_process_grantt.get_end_time() + 0,  # first cpu start
                                     prev_process_grantt.get_end_time() + process.cpu_burst_time1,  # io start time
                                     prev_process_grantt.get_end_time() + process.cpu_burst_time1 + process.io_time,  # sec cpu start
                                     prev_process_grantt.get_end_time() + process.cpu_burst_time1,  # first cpu end
                                     prev_process_grantt.get_end_time() + process.cpu_burst_time1 + process.io_time,  # io end time
                                     prev_process_grantt.get_end_time() + process.cpu_burst_time1 + process.io_time + process.cpu_burst_time2)  # sec cpu end
                )
        return self.grantt_chart