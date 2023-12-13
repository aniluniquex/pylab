class Time:
    def __init__(self,seconds):
        self.seconds=seconds

    def convert(self):
        self.seconds = self.seconds % (12 * 3600)
        hour = self.seconds // 3600
        self.seconds %= 3600
        minutes = self.seconds // 60
        self.seconds %= 60
        return "%d:%02d:%02d" % (hour, minutes, self.seconds)

a=Time(230)
print(a.convert())
