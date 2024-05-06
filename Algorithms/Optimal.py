class Optimal_Page_Replacement:
    def Optimal_Page_Replacement(self, Pages, Number_of_Frames):
        Page_Faults = 0
        Page_Frames = []
        Farthest_Index = -1
        Index_to_Replace = -1 
        Report = []
        for i in range(len(Pages)):
            if Pages[i] not in Page_Frames:
                
                Page_Faults += 1

                if len(Page_Frames) < Number_of_Frames:
                    Page_Frames.append(Pages[i])
                else:
                    Farthest_Index = -1
                    Index_to_Replace = -1 
                    for j in range(len(Page_Frames)):
                        Flag_Found = False
                        for k in range(i + 1, len(Pages)):
                            if Page_Frames[j] == Pages[k]:
                                if k > Farthest_Index:
                                    Farthest_Index = k
                                    Index_to_Replace = j
                                Flag_Found = True
                                break
                        
                        if not Flag_Found:
                            Index_to_Replace = j
                            break
                    
                    if Index_to_Replace != -1:
                        Page_Frames[Index_to_Replace] = Pages[i]
                    else:
                        Page_Frames[0] = Pages[i]

            Report.append([Page_Frames, Page_Faults])
        
        return Report, Page_Faults

# Example usage:
# Pages = [ 1, 2, 3, 2, 1, 5, 2, 1, 6, 2, 5, 6, 3, 1, 3, 6, 1, 2, 4, 3]

# Optimal_Algo = Optimal_Page_Replacement()

# Number_of_Frames = 3
# Report, Page_Faults = Optimal_Algo.Optimal_Page_Replacement(Pages, Number_of_Frames)
# print(Report)
# print("Number of Page Faults: ", Page_Faults)