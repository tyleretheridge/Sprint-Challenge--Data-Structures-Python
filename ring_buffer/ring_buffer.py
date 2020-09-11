class RingBuffer:
    def __init__(self, capacity):
        # Maximum size of ring buffer
        self.capacity = capacity
        # Array to hold data
        self.storage = []
        # Index value to manage data insertion
        self.index = 0

    def append(self, item):
        # As long as index is valid, do nothing
        # If index >= capacity, reset index to head position
        if self.index >= self.capacity:
            self.index = 0
        # If buffer is full, pop values at index before insertion
        if len(self.storage) == self.capacity:
            # Pop at index
            self.storage.pop(self.index)
        # Insert data at index
        self.storage.isnert(self.index, item)
        # Increment index
        self.index += 1

    def get(self):
        # Return a list of buffer items in order, excluding "None" entries
        buffer_list = []
        for data in self.storage:
            if data != None:
                buffer_list.append(data)
        return buffer_list