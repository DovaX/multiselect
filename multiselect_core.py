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
    