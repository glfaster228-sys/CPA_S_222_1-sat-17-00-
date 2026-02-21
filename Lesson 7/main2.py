class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self   
    def __next__(self):
        if self.i < self.max_number:
            self.i += 1
            return self.i
        else:
            raise StopIteration 
counter = Counter(5)
for i in counter:
    print(i) 
  