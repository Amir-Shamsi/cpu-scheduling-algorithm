class GranttAnalysis:
    grantt_chart = []
    turn_around_time = []
    response_time = []
    waiting_time = []

    def __init__(self, grantt_chart):
        self.grantt_chart = grantt_chart

    def calculate_turn_around_time(self):
        for info in self.grantt_chart:
            self.turn_around_time.append((  # tuple
                info.process,
                info.get_end_time() - info.process.arrival_time
            ))

    def calculate_waiting_time(self):
        for info in self.grantt_chart:
            self.response_time.append((  # tuple
                info.process,
                (info.get_end_time() - info.process.arrival_time) -
                (info.process.cpu_burst_time1 + info.process.cpu_burst_time2)  # turn around - cpu burst time
            ))

    def calculate_response_time(self):
        for info in self.grantt_chart:
            self.turn_around_time.append((  # tuple
                info.process,
                info.get_start_time()
            ))