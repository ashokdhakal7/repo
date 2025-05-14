class counter:
    count=0
    def __init__(self):
        print("init called by ", self)
        counter.count=counter.count+1
        print ("count is ", counter.count)
    def __del__(self):
        print("del called by ", self)
        counter.count=counter.count-1
        
            