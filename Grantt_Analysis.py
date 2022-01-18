class GranttAnalysis:
    grantt_chart = []
    turn_around_time = []
    response_time = []
    waiting_time = []

    def __init__(self, grantt_chart, processes):
        self.grantt_chart = grantt_chart
        for process_info in self.grantt_chart:
            for process in processes:
                if process_info.process.process_id == process.process_id:
                    process_info.process = process

    def calculate_turn_around_time(self):
        for info in self.grantt_chart:
            self.turn_around_time.append([  # list
                info.process,
                info.get_end_time() - info.process.arrival_time
            ])

    def calculate_waiting_time(self):
        for info in self.grantt_chart:
            self.waiting_time.append([  # list
                info.process,
                (info.get_end_time() - info.process.arrival_time) -
                (info.process.cpu_burst_time1 + info.process.cpu_burst_time2)  # turn around - cpu burst time
            ])

    def calculate_response_time(self):
        for info in self.grantt_chart:
            self.response_time.append([  # list
                info.process,
                info.get_start_time() - info.process.arrival_time
            ])

    def get_total_time(self):
        max_end_time = 0
        for grantt in self.grantt_chart:
            max_end_time = max(max_end_time, grantt.get_end_time())
        return max_end_time

    def pretty_print(self, status):
        response_time_avg = 0
        turn_around_time_avg = 0
        waiting_time_avg = 0

        self.calculate_response_time()
        self.calculate_turn_around_time()
        self.calculate_waiting_time()

        print('=======================================================================================================')
        print('                                               %s                                    ' % status.upper())
        print('=======================================================================================================')

        print('\t\t   Response Time\t  Turnaround Time\t   Waiting Time\t\t    Start Time\t\t\t End Time')
        indexes = []
        for info in self.grantt_chart:
            indexes.append(info.process.process_id)
        count = 0
        for index in indexes:
            print('P%d\t\t\t\t%d\t\t\t\t\t%d\t\t\t\t\t%d\t\t\t\t\t%d\t\t\t\t\t%d' % (index,
                                                                                     self.response_time[count][1],
                                                                                     self.turn_around_time[count][1],
                                                                                     self.waiting_time[count][1],
                                                                                     self.grantt_chart[count].get_start_time(),
                                                                                     self.grantt_chart[count].get_end_time()))
            response_time_avg += self.response_time[count][1]
            turn_around_time_avg += self.turn_around_time[count][1]
            waiting_time_avg += self.waiting_time[count][1]
            count += 1

        response_time_avg /= len(self.response_time)
        turn_around_time_avg /= len(self.turn_around_time)
        waiting_time_avg /= len(self.waiting_time)

        print('-------------------------------------------------------------------------------------------------------')

        print('Avg\t\t\t\t%.1f\t\t\t\t\t%.1f\t\t\t\t%.1f\n' % (response_time_avg,
                                                             turn_around_time_avg,
                                                             waiting_time_avg))

        print('Total Time:', self.get_total_time())
        print('Idle Time:', self.get_idle_time())
        print('Burst Time:', self.get_burst_time())
        print('Efficiency is %.2f' % self.get_cpu_efficiency())
        print('Throughput is %.2f per a second' % self.get_throughput())

        print('=======================================================================================================')

    def get_idle_time(self):
        return self.get_total_time() - self.get_burst_time()

    def get_burst_time(self):
        burst_sum = 0
        for grantt in self.grantt_chart:
            burst_sum += grantt.process.cpu_burst_time1 + grantt.process.cpu_burst_time2
        return burst_sum

    def get_cpu_efficiency(self):
        return self.get_burst_time() / self.get_total_time()

    def get_throughput(self):
        return (len(self.grantt_chart) * 1000) / self.get_total_time()
