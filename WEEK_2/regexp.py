#regular experations
# Data extractions 
# patterns, retun data points of our interest
#re, search, finall, pass paterns


# data extractions based on pattern definations

# modules, re

import re 

text = "we are learning python"

pattern = "python"

match = re.search(pattern,text)

if match:
 print("match found")

else:
  print("match not found")
  
