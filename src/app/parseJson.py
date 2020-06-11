import json
import os
import re

# Opening JSON file 
f = open('ruaInfo.json',"r") 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
for i in data['ruas']: 
    print(i) 
  
# Closing file 
f.close() 
