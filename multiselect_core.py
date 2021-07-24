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
    
    def tick(self,index):
        self.data[index]["value"]=True
    
    def untick(self,index):
        self.data[index]["value"]=False
        
        
    def tick_first_by_key(self,key):
        index=self.keys().index(key)
        self.tick(index)
        
    def tick_all_by_key(self,key):
        indices=[i for i,x in enumerate(self.keys()) if x==key]
        for index in indices:
            self.tick(index)
            
    def tick_all_by_keys(self,keys):
        for key in keys:
            self.tick_all_by_key(key)
            
    def tick_by_indices(self,indices):
        for index in indices:
            self.tick(index)
            
 
    def untick_first_by_key(self,key):
        index=self.keys().index(key)
        self.untick(index)

    def untick_all_by_key(self,key):
        indices=[i for i,x in enumerate(self.keys()) if x==key]
        for index in indices:
            self.untick(index)
        
    def untick_all_by_keys(self,keys):
        for key in keys:
            self.untick_all_by_key(key)
        
    def untick_by_indices(self,indices):
        for index in indices:
            self.untick(index)

        
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
                self.untick(index)
            else:
                self.tick(index)
    
      
    def get_ticked_indices(self):
        return([i for i,x in enumerate(self.keys()) if self.data[i]["value"]==True])
        
    def get_unticked_indices(self):
        return([i for i,x in enumerate(self.keys()) if self.data[i]["value"]==False])

    def __str__(self):
        return("<Multiselect object> "+str(self.data))
    
    def __getitem__(self,key):
        try:
            index=self.keys().index(key)
            return(self.data[index]["value"])        
        except ValueError as e:
            raise KeyError("'"+key+"' is not in the multiselect")
