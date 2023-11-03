class Terminal:
    def __init__(self, digits):
        if digits[0] in ["9", "7", "6"] and len(digits) == 9:
            self.__digits = digits
        else:
            raise TypeError(f'{digits} no es un número de teléfono válido.')
        self.__time_made = 0
        self.__time_received = 0
        self.__total_time = 0
    @property
    def time_received(self):
        return self.__time_received
    @time_received.setter
    def time_received(self, call_time):
        self.__time_received += call_time
        self.__total_time += call_time
    @property
    def time_made(self):
        return self.__time_made
    @time_made.setter
    def time_made(self, call_time):
        self.__time_made += call_time
        self.__total_time += call_time
    @property
    def total_time(self):
        return self.__total_time
    def call(self, terminal, call_time):
        self.time_made = call_time
        terminal.time_received = call_time

    def __str__(self):
        return f'{self.__digits} - Conversation time: {self.__total_time}'



