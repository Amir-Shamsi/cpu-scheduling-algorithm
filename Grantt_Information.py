class ProcessGrantInfo:
    process = None
    cpu_start_time1 = 0
    cpu_start_time2 = 0
    io_start_time = 0
    cpu_end_time1 = 0
    cpu_end_time2 = 0
    io_end_time = 0

    def __init__(self, process,
                 cpu_start_time1,
                 io_start_time,
                 cpu_start_time2,
                 cpu_end_time1,
                 io_end_time,
                 cpu_end_time2):
        self.process = process
        self.io_end_time = io_end_time
        self.cpu_end_time2 = cpu_end_time2
        self.cpu_end_time1 = cpu_end_time1
        self.io_start_time = io_start_time
        self.cpu_start_time2 = cpu_start_time2
        self.cpu_start_time1 = cpu_start_time1

    def get_start_time(self):
        return self.cpu_start_time1

    def get_end_time(self):
        return self.cpu_end_time2
