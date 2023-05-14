# python3

class Treade:
    def __init__(self, timeStart, position, taskNumber):
        self.taskNumber  = taskNumber
        self.timestart = timeStart
        self.position = position
    
    def getTime(self):
        return self.timestart
    
    def getTaskNumber(self):
        return self.taskNumber
    
    def getPosition(self):
        return self.position
    
    def setTime(self, timeStart):
        self.timestart = timeStart
    def setPosition(self, position):
        self.position = position
    
    def setTaskNumber(self, taskNumber):
        self.taskNumber = taskNumber

    
   



def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    tread_list =[]
    max_time = 0
    for i in data:
        if max_time < i:
            max_time = i
    
    while len(tread_list)< n :
        tread = Treade(0,True,len(tread_list))
        #tread.setPosition(True)
        tread_list.append(tread)
    
    time = 0
    j = 0

    while time < m*n:
        i = 0
        
        while i < len(tread_list)  :
             
            if time == 0:
           
               tread_list[i].setPosition(False)
               tread_list[i].setTime(time)
               tread_list[i].setTaskNumber(j)
               if len(output)< m:
                    arr =[i,tread_list[i].getTime()]
                    output.append(arr)
               j = j +1
            

            if tread_list[i].getPosition() == False and tread_list[i].getTaskNumber()<len(data) and  time - tread_list[i].getTime()== data[tread_list[i].getTaskNumber()] :
               tread_list[i].setPosition(True) 

               
            
                   
            i = i + 1
        
        
        i = 0
        while i <= len(tread_list)-1 :
            if j < len(data)+1:
                if tread_list[i].getPosition() == True:
                    tread_list[i].setPosition(False)
                    tread_list[i].setTime(time)
                    tread_list[i].setTaskNumber(j)
                    if len(output)< m:
                        arr =[i,tread_list[i].getTime()]
                        output.append(arr)
                    j = j +1
            i = i +1
        
        #i = 0
        #while i < len(output):
       
            #print("position",i.getPosition())
            #print("tread number",i)
            #print("task number",tread_list[i].getTaskNumber())
            #print("time",i.getTime())
            #i = i+ 1
        time = time +1


        


        
    
    # create the output pairs
    #print(max_time)
   
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    first_line = list(map(int,input().split()))
    if len(first_line) > 2 :
        print("ERROR")
        return 0
    n = 0
    m = 0

    n = first_line[0]
    m = first_line[1]



    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split()))
    
    if m != len(data):
        print("ERROR")
        return 0

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i in result:
        print(i[0],i[1])
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
