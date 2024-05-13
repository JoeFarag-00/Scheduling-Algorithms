class Look:
    def __init__(self, disk_size, initial_position=0,initial_Forward_move=True):
        self.disk_size = disk_size
        self.current_position = initial_position
        self.request_queue = [initial_position]
        self.total_seek_distance = 0
        self.Paths_List=[]
        self.initial_Forward_move=initial_Forward_move

    def add_request(self, requests):
        self.request_queue.extend(requests)

    def schedule(self):
        self.request_queue.append(self.disk_size)  
        self.request_queue.sort()  

        current_index = self.request_queue.index(self.current_position)

        if self.initial_Forward_move==True:
            for i in range(current_index, len(self.request_queue)):
                self.Paths_List.append(self.request_queue[i])
    
            for i in range(0, current_index):
                self.Paths_List.append(self.request_queue[i])
                    
        if self.initial_Forward_move==False:
               
            for i in range(current_index, -1, -1):
                self.Paths_List.append(self.request_queue[i])
            
            for i in range(len(self.request_queue) - 1, current_index, -1):
                self.Paths_List.append(self.request_queue[i])

        total_seek_distance=0
        rm = 0
        
        if self.disk_size in self.Paths_List:
            self.Paths_List.remove(self.disk_size)
            
        if rm in self.Paths_List:
            self.Paths_List.remove(rm)
            
        max_index = self.Paths_List.index(max(self.Paths_List))  
        sorted_sublist = sorted(self.Paths_List[max_index + 1:], reverse=True) 
        self.Paths_List = self.Paths_List[:max_index + 1] + sorted_sublist

        for i in range(1,len(self.Paths_List)):
            total_seek_distance += abs(self.Paths_List[i] - self.Paths_List[i-1])

        return self.Paths_List, total_seek_distance
    