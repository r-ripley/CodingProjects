class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        
    def rank():
        return user.rank
    
    def progress():
        return user.progress
    
    def inc_progress(self, value):
        if value == 0 or value > 8 or value < -8:
            raise Exception("Not a value")
        else:
            # edge cases for rank
            if self.rank == 8:
                self.progress = 0
            elif self.rank == value:
                self.progress += 3
            elif self.rank - value == 1 or self.rank == 1 and value == -1:
                self.progress += 1
            # add progress based on fighting values
            elif self.rank < 0 and value >= 1:
                self.progress += 10 * (self.rank - value + 1) * (self.rank - value + 1)
            elif self.rank < value and (value <= -1 or value >= 1):
                self.progress += 10 * (self.rank - value) * (self.rank - value)
            # reduce progress to value less than 100, add to rank each time progress is reduced
            while self.progress >= 100:
                self.rank += 1
                self.progress -= 100
                if self.rank == 0:
                    self.rank = 1
                if self.rank == 8:
                    self.progress = 0