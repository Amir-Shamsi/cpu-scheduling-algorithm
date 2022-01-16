class Process:
    process_id = 0
    arrival_time = 0
    cpu_burst_time1 = 0
    cpu_burst_time2 = 0
    io_time = 0

    def __init__(self, process_id, arrival_time, cpu_time1, io_time, cpu_time2):
        self.arrival_time = arrival_time
        self.cpu_burst_time1 = cpu_time1
        self.cpu_burst_time2 = cpu_time2
        self.io_time = io_time
        self.process_id = process_id