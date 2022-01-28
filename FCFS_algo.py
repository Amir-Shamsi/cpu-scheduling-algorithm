import sys

sys.path.append(".")
from Grantt_Information import ProcessGrantInfo


class FCFS:
    processes = []
    grantt_chart = []
    mode = ''
    ClassName = 'FCFS'

    def __init__(self, processes, mode=''):
        self.mode = mode
        self.processes = processes

    def cpu_process(self):
        for process in self.processes:
            if len(self.grantt_chart) == 0:
                self.grantt_chart.append(
                    ProcessGrantInfo(process,
                                     process.arrival_time,  # first cpu start
                                     process.arrival_time + process.cpu_burst_time1,  # io start time
                                     process.arrival_time + process.cpu_burst_time1 + process.io_time,  # sec cpu start
                                     process.arrival_time + process.cpu_burst_time1,  # first cpu end
                                     process.arrival_time + process.cpu_burst_time1 + process.io_time,  # io end time
                                     process.arrival_time + process.cpu_burst_time1 + process.io_time + process.cpu_burst_time2)
                    # sec cpu end
                )
            else:
                prev_process_grantt = self.grantt_chart[len(self.grantt_chart) - 1]
                if process.arrival_time < prev_process_grantt.get_end_time():
                    self.grantt_chart.append(
                        ProcessGrantInfo(process,
                                         prev_process_grantt.get_end_time() + 0,  # first cpu start
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1,  # io start time
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1 + process.io_time,
                                         # sec cpu start
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1,  # first cpu end
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1 + process.io_time,
                                         # io end time
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1 + process.io_time + process.cpu_burst_time2)
                        # sec cpu end
                    )
                else:
                    self.grantt_chart.append(
                        ProcessGrantInfo(process,
                                         process.arrival_time,  # first cpu start
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1,  # io start time
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1 + process.io_time,
                                         # sec cpu start
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1,  # first cpu end
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1 + process.io_time,
                                         # io end time
                                         prev_process_grantt.get_end_time() + process.cpu_burst_time1 + process.io_time + process.cpu_burst_time2)
                        # sec cpu end
                    )
        return self.grantt_chart
