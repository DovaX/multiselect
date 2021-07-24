class Multiselect:
    def __init__(self,data):
        self.data=data
        
    @classmethod
    def init_from_options(cls,options):
        data=[{"key":x,"value":False} for x in options]
        return(cls(data))

    def keys(self):
        keys=[x["key"] for x in self.data]
        return(keys)
    
    def values(self):
        values=[x["value"] for x in self.data]
        return(values)
    
    def items(self):
        items=[(x["key"],x["value"]) for x in self.data]
        return(items)
    
    
    def tick_first_by_key(self,key):
        index=self.keys().index(key)
        self.data[index]["value"]=True
        
    def tick_all_by_key(self,key):
        indices=[i for i,x in enumerate(self.keys()) if x==key]
        for index in indices:
            self.data[index]["value"]=True
            
    def tick_by_indices(self,indices):
        for index in indices:
            self.data[index]["value"]=True
            
 
    def untick_first_by_key(self,key):
        index=self.keys().index(key)
        self.data[index]["value"]=False

    def untick_all_by_key(self,key):
        indices=[i for i,x in enumerate(self.keys()) if x==key]
        for index in indices:
            self.data[index]["value"]=False
        
    def untick_by_indices(self,indices):
        for index in indices:
            self.data[index]["value"]=False

        
    def toggle_first_by_key(self,key):
        index=self.keys().index(key)
        if self.data[index]["value"]:
            self.untick_first_by_key(key)
        else:
            self.tick_first_by_key(key)
            
    def toggle_all_by_key(self,key):
        indices=[i for i,x in enumerate(self.keys()) if x==key]
        self.toggle_by_indices(indices)
            
    def toggle_by_indices(self,indices):
        for index in indices:
            if self.data[index]["value"]:
                self.untick_by_indices([index])
            else:
                self.tick_by_indices([index])
    
      