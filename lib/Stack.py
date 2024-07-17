class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0: 
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        return self.items
        

    def pop(self):
        if len(self.items)>0:
            return self.items.pop()        
    

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit: 
            return True
        else:
            return False

    def search(self, target):
        for i in range(0, len(self.items)) :
            if (self.items[i]==target):
                return len(self.items)-i-1
        return -1
