class CScan:
    def __init__(self, disk_size, initial_position=0):
        self.disk_size = disk_size
        self.current_position = initial_position
        self.request_queue = [initial_position]
        self.total_seek_distance = 0
        self.awnser=[]

    def add_request(self, requests):
        self.request_queue.extend(requests)


    def schedule(self):
        self.request_queue.append(self.disk_size)  
        self.request_queue.sort()  

       
        current_index = self.request_queue.index(self.current_position)

        
        for i in range(current_index, len(self.request_queue)):
            print(f"Servicing request at index number: {i} ---->", self.request_queue[i])
            self.awnser.append(self.request_queue[i])

        
        for i in range(0, current_index):
            print(f"Servicing request at index number: {i} ---->", self.request_queue[i])
            self.awnser.append(self.request_queue[i])

        for i in range(1,len(self.awnser)):
            self.total_seek_distance += abs(self.awnser[i] - self.awnser[i-1])
            print("seek distance in this step ",abs(self.awnser[i] - self.awnser[i-1]))

        print("Final Awnser ",self.awnser)
        print("Total Seek distance is ",self.total_seek_distance)


c_scan = CScan(199, initial_position=53)


c_scan.add_request([98, 183, 37, 122, 14, 124, 65, 67])


c_scan.schedule()

