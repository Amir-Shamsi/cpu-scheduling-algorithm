import sys

sys.path.append(".")
from Grantt_Information import ProcessGrantInfo


class RoundRobin:
    processes = []
    mode = ''
    grantt_chart = []
    queue_num = None
    ClassName = 'RR'

    def __init__(self, processes, mode=''):
        self.mode = mode
        self.processes = processes
        if mode != '':
            self.queue_num = mode.split('xx')[0]

    def cpu_process(self, time_quantum):
        current_cpu_time = 0
        prev_cpu_time = 0
        not_started = False
        ready_processes_queue = []
        processes_next_ready_queue = self.get_arrival_times()

        while True:
            finished = False
            if not not_started:
                first_process = self.processes[0]
                self.processes.remove(first_process)
                ready_processes_queue.append([first_process, 0])
                for process in self.processes.copy():
                    if process.arrival_time == first_process.arrival_time:
                        ready_processes_queue.append([process, 0])
                        self.processes.remove(process)
                not_started = True

            if len(ready_processes_queue) == 0:
                current_cpu_time += 1
                continue

            sub_count = ready_processes_queue[0][1]
            current_process = ready_processes_queue[0][0]
            pre_current_process = current_process.cpu_burst_time1 + current_process.cpu_burst_time2 + current_process.io_time
            if current_process.cpu_burst_time1 > 0 and current_process.arrival_time <= current_cpu_time:
                not_entered = True
                for element in self.grantt_chart:
                    if element.process.process_id == current_process.process_id:
                        not_entered = False
                if not_entered:
                    self.grantt_chart.append(ProcessGrantInfo(current_process,
                                                              max(current_process.arrival_time, current_cpu_time),
                                                              # first cpu start
                                                              -1,  # io start time
                                                              -1,  # sec cpu start
                                                              -1,  # first cpu end
                                                              -1,  # io end time
                                                              -1))  # sec cpu end

                current_process.cpu_burst_time1 -= time_quantum
                sub_count += 1
                if current_process.cpu_burst_time1 < 0:
                    current_cpu_time += (current_process.cpu_burst_time1 + time_quantum)
                else:
                    current_cpu_time += time_quantum

            if current_process.cpu_burst_time1 <= 0 and current_process.arrival_time <= current_cpu_time and \
                    processes_next_ready_queue[str(current_process.process_id)] <= current_cpu_time:
                if current_process.io_time > 0:
                    ready_processes_queue[0][1] = 0  # sub_count = 0
                    sub_count = 0
                    processes_next_ready_queue[
                        str(current_process.process_id)] = current_cpu_time + current_process.io_time

                    for info in self.grantt_chart:
                        if info.process.process_id == current_process.process_id:
                            info.process = current_process
                            info.io_start_time = current_cpu_time
                            info.cpu_end_time1 = current_cpu_time
                            info.io_end_time = current_cpu_time + current_process.io_time
                            if current_process.cpu_burst_time2 <= 0:
                                info.cpu_start_time2 = -1
                                info.cpu_end_time2 = -1
                            break
                    current_process.io_time = 0
                    finished = True
                elif current_process.cpu_burst_time2 > 0 and current_process.cpu_burst_time1 <= 0:
                    if sub_count == 0:
                        for info in self.grantt_chart:
                            if info.process.process_id == current_process.process_id:
                                info.cpu_start_time2 = current_cpu_time
                    if processes_next_ready_queue[str(current_process.process_id)] <= current_cpu_time:
                        current_process.cpu_burst_time2 -= time_quantum
                        sub_count += 1
                        if current_process.cpu_burst_time2 < 0:
                            current_cpu_time += (current_process.cpu_burst_time2 + time_quantum)
                        else:
                            current_cpu_time += time_quantum
                    if current_process.cpu_burst_time2 <= 0:
                        for info in self.grantt_chart:
                            if info.process.process_id == current_process.process_id:
                                info.process = current_process
                                info.cpu_end_time2 = current_cpu_time
                                break

            # if ready_processes_queue[0][1] != sub_count or finished:
            current_process_value = current_process.cpu_burst_time1 + current_process.cpu_burst_time2 + current_process.io_time
            if pre_current_process != current_process_value:
                ready_processes_queue.pop(0)
                if current_process.cpu_burst_time2 > 0 or current_process.cpu_burst_time1 > 0 or current_process.io_time > 0:
                    ready_processes_queue.append([current_process, sub_count])
            #  if current_process.cpu_burst_time2 + current_process.cpu_burst_time1 + current_process.io_time <= 0:
            #  ready_processes_queue.pop(0)
            if len(self.processes) <= 0 and len(ready_processes_queue) <= 0:
                break

            if prev_cpu_time == current_cpu_time:
                current_cpu_time += 1
            prev_cpu_time = current_cpu_time

            _temp = []
            new_queue = False
            for process in self.processes.copy():
                if process.arrival_time <= current_cpu_time:
                    _temp.insert(0, [process, 0])
                    self.processes.remove(process)
                    new_queue = True

            if new_queue:
                for process_info in _temp:
                    ready_processes_queue.insert(0, process_info)
            _temp.clear()

    def get_arrival_times(self):
        _temp = {}
        for process in self.processes:
            _temp[str(process.process_id)] = process.arrival_time
        return _temp
