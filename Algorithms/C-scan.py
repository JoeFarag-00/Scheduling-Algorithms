class CScan:
    def __init__(self, disk_size, initial_position=0,initial_Forward_move=True):
        self.disk_size = disk_size
        self.current_position = initial_position
        self.request_queue = [initial_position]
        self.total_seek_distance = 0
        self.awnser=[]
        self.initial_Forward_move=initial_Forward_move

    def add_request(self, requests):
        self.request_queue.extend(requests)


    def schedule(self):
        self.request_queue.append(self.disk_size)  
        self.request_queue.sort()  

       
        current_index = self.request_queue.index(self.current_position)



        if self.initial_Forward_move==True:
            for i in range(current_index, len(self.request_queue)):
                print(f"Servicing request at index number: {i} ---->", self.request_queue[i])
                self.awnser.append(self.request_queue[i])
    
            
            for i in range(0, current_index):
                print(f"Servicing request at index number: {i} ---->", self.request_queue[i])
                self.awnser.append(self.request_queue[i])
                
        
        
        if self.initial_Forward_move==False:
            
            
           
            for i in range(current_index, -1, -1):
                print(f"Servicing request at index number: {i} ---->", self.request_queue[i])
                self.awnser.append(self.request_queue[i])
            
            for i in range(len(self.request_queue) - 1, current_index, -1):
                print(f"Servicing request at index number: {i} ---->", self.request_queue[i])
                self.awnser.append(self.request_queue[i])
                
                
        
        return self.awnser
        # print("Total Seek distance is ",self.total_seek_distance)
    
            
            
    




c_scan = CScan(4999, initial_position=143, initial_Forward_move=True)


c_scan.add_request([ 86, 1470, 913, 1774, 948, 1509, 1022, 1750, 130])


final_awnser=c_scan.schedule()
print("Final Awnser ",final_awnser)


seek_distance=[]
total_seek_distance=0


for i in range(1,len(final_awnser)):
   total_seek_distance += abs(final_awnser[i] - final_awnser[i-1])
   seek_distance.append(abs(final_awnser[i] - final_awnser[i-1]))


print("the seek_distance ",seek_distance)
print("total Seek distance ",total_seek_distance)


