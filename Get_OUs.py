import re
import requests
import pprint
import json
from datetime import datetime
from docx import Document
from docx.shared import Inches
import importlib.machinery
#This allows the valenceConnect.py file to be imported from a parent directory
loader = importlib.machinery.SourceFileLoader('VC', 'C:/Users/jbooth3/Documents/Python Scripts/ValenceConnect.py')
ValenceConnect = loader.load_module('VC')

semesterId = "848472"      #Fall 2016
deptId = "49608"            #Information Technology
courseId = "1136338"        #Abnormal Psychology Section 90 Summer Semester 2016
Count = 0

#returns a Forbidden errors
route1 = "/d2l/api/lp/1.9/courses/"+semesterId
route2 = "/d2l/api/lp/1.9/courses/"+deptId
#returns individual course information
route3 = "/d2l/api/lp/1.9/courses/"+courseId

#returns all courses and templates under the given Id
route2 = "/d2l/api/lp/1.9/orgstructure/"+semesterId+"/descendants/paged/"
url = ValenceConnect.uc.create_authenticated_url(route2)
r = requests.get(url)
    
# text response of each course.
respString = r.text
line = str(respString)+ "\n"
e = json.loads(respString) # now we convert it to JSON.
#print(e)

f = open('OU.txt', "a") # opens a file for writing. if the file doesn't exist, it makes the file.
f.write(str(datetime.now())+"\n")

###Tables###

for item in e['Items']:
    ou = item['Identifier']
    name = item['Name']  
    code = item['Code'] 
    typeId = item['Type']['Id']      
    line = name + ", " + str(ou) + ", " + str(code)+ "\n"
    print(line)
    if 3 == 3:
        f.write(line)
        Count+=1
f.write("\n")
f.close()

json_acceptable_string = re.sub(r'{', '\n', respString)
json_acceptable_string = respString.replace('"', "'")
json_acceptable_string = respString.replace(',', ",\n")

print("Test: "+json_acceptable_string)
with open('OUs.json', 'a') as jsonFile:
	jsonFile.write("\n"+str(datetime.now()) + "\n" +json_acceptable_string + "\n")
