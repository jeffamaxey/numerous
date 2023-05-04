import os

class Historian:
    def __init__(self, max_size, timesteps_reserved_per_event=100):
        self.max_size = max_size
        self.timesteps_reserved_per_event = timesteps_reserved_per_event

    def get_historian_max_size(self, number_of_timesteps, events_count):
        return (
            self.max_size
            if self.max_size
            else number_of_timesteps
            + events_count * self.timesteps_reserved_per_event
            + 1
        )

    def store(self, df):
        pass



class InMemoryHistorian(Historian):

    def __init__(self):
        super().__init__(None)


class LocalHistorian(Historian):

    def __init__(self, filename, max_size):
        super().__init__(max_size)
        self.filename = filename

    def store(self, df):
        if os.path.isfile(self.filename):
            df.dropna().to_csv(self.filename, mode='a', header=False)
        else:
            df.dropna().to_csv(self.filename)