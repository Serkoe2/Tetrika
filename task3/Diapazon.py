class Diapazon:
    def __init__(self,start,end):
        if start >= end:
            self.start = False
            return
        self.start = start
        self.end = end
        
    def union(self,b):
        if b.start > self.end:
            return False
        if self.end >= b.end:
            return self
        if b.end > self.end:
            self.end = b.end
            return self
    def unionMaxima(self,b):
        if self.start >= b.end:
            return -1
        if b.start >= self.end:
            return -2
        if self.start >= b.start and b.end<=self.end:
            result = b.end - self.start
            return result
        if self.start <= b.start and b.end<=self.end:
            result = b.end - b.start
            return result
        if self.start <= b.start and self.end <= b.end:
            result = self.end - b.start
            return result
        if self.start >= b.start and self.end<=b.end:
            result = self.end - self.start
            return result

    
    def __repr__(self):
        return f"start {self.start} , end {self.end}"