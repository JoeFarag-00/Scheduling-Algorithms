import numpy as np

class second_chance:
    def second(self, pages, ref_string):
      pages_arr=[]
      sorted_pages_arr=[]
      chances=np.zeros(pages,dtype=int)
      page_faults=pages
      frames=[]

      for i in range(len(ref_string)):
        if len(pages_arr) < pages:
          if ref_string[i] not in pages_arr:
            pages_arr.append(ref_string[i])
          else:
            a=pages_arr.index(ref_string[i])
            chances[a]=1
          sorted_pages_arr=pages_arr.copy()  
        else:
          if ref_string[i] not in pages_arr:
            for k in range(pages):
                if chances[k]==0:

                  aa=sorted_pages_arr.index(pages_arr[k])
                  sorted_pages_arr[aa]=ref_string[i]

                  del pages_arr[k]
                  pages_arr.append(ref_string[i])
                  chances=np.roll(chances,pages-1) 
                  page_faults+=1
                  break
                else:
                  chances[k]=0

          else:
            
            a=pages_arr.index(ref_string[i])
            chances[a]=1
          
        frames.append(sorted_pages_arr.copy())
      return page_faults,frames
  

hey=second_chance()

report=hey.second(3,[0,4,1,4,2,4,3,4,2,4,0,4,1,4,2,4,3,4])
print(report)    


    



    
  
