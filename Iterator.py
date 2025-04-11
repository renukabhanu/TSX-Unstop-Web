Class Counter:
    def __init__(self,start,end):
        self.current=start-1
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        self.current=1
        if self.current<self.end:
            return self.current
        else:
            raise Stop Iteration
for c in counter(3,9):
    print(c)
