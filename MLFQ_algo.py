import sys

sys.path.append(".")
from RR_algo import RoundRobin
from FCFS_algo import FCFS


class MLFQ:
    processes = []
    grantt_chart = []

    def __init__(self, processes):
        self.processes = processes

    def cpu_process(self):
        first_time_quantum = 8
        first_queue = RoundRobin(processes=self.processes, mode='0x1')  # 0x1: one cycle execute
        first_queue.cpu_process(time_quantum=first_time_quantum)

        sec_time_quantum = 16
        sec_queue = RoundRobin(processes=self.processes, mode='0x1')  # 0x1: one cycle execute
        sec_queue.cpu_process(time_quantum=sec_time_quantum)

        third_queue = FCFS(processes=self.processes, mode='0x1')  # 0x1: one cycle execute
        third_queue.cpu_process()

        return self.grantt_chart