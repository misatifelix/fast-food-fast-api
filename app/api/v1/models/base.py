class BaseModel(object):
    """
    used to handle the common model methods
    """
    # query by id
    def get_by_id(self,id,data):
        return next(filter(lambda x:x['id'] == id, data), None)

     #query by name
    def get_by_name(self, name,data):
        return next(filter(lambda x:x['name'] == name, data), None)

     #delete 
    def delete_item(self,id,data):
        """
        filter out the items that do not match id
        """
        return list(filter(lambda x:x['id'] != id, data))

    # get list length for  auto-increment 
    def get_length(self,data):
        data_len = len(data)
        return data_len
    
    
