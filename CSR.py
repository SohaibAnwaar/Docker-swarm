#!/usr/bin/env python
# coding: utf-8

# # Customer Sales Representative
#     Hey I am a customer sales representative. My only work here is to entertain our beloved clients and in results I get a pay raise. (Party) 

# In[2]:


import pymongo
import os

connectionString = os.getenv("MONGO_URL");
myclient = pymongo.MongoClient(connectionString)

print(myclient.list_database_names())


# In[3]:


from pymongo import MongoClient
import pymongo


connectionString = os.getenv("MONGO_URL");
client           = MongoClient(connectionString)
db               = client.magic_shop        # test is my database
col              = db.req                   # Here spam is my collection


# # Listening to the Insert Stream

# In[ ]:


import socket
machine_name = socket.gethostname()
from datetime import datetime
import time

def processing_request(request):
    '''
    Description:
        Get the string, takes its length and run a loop 10 times of string length and set the 
        response to processed.
        
    Input:
        request  (str) : Random String
        
    Output:
        Set value back to the mongo db
            response: Processed
    '''
    for i in range(0,len(request)*10):
        pass
    
    

try:
    with db.req.watch([{'$match': {'operationType': 'insert'}}]) as stream:
        print("Catching Insert Triggers")
        for values in stream:
            request_id = values['fullDocument']['request_id']
            request    = values['fullDocument']['request']
            myquery    = { "request_id": request_id }
            
            # Checking if not processed by other replica (Blocking System)
            if len(list(col.find({ 'request_id': request_id, 'CSR_NAME' : { "$exists": False}}))):
                newvalues  = { "$set": { "CSR_NAME": machine_name, "response": "Processing", "processing_time":datetime.today()} }

                # CSR Responding to the client
                col.update_one(myquery, newvalues)
                print(request_id)
                print(f"Processing {request_id}")
                # Now Processing Request
                processing_request(request)
                # Updating that work is done

                myquery   = { "request_id": request_id }
                newvalues = { "$set": {"response": "Request Processed Have a nice Day sir!", 'response_time':datetime.today()} }
                # CSR Responding to the client
                col.update_one(myquery, newvalues)
            
except pymongo.errors.PyMongoError:
    # The ChangeStream encountered an unrecoverable error or the
    # resume attempt failed to recreate the cursor.
    logging.error('...')


# In[ ]:





# In[ ]:




