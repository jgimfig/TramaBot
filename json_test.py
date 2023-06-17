import json
 
# Data to be written
dictionary = {
    "Nombre": "Javi",
    "Tramas": 45
}
 
# Serializing json
json_object = json.dumps(dictionary)
dictionary = {
    "Nombre": "Franky",
    "Tramas": 22
}
json_object = json.dumps(dictionary, indent=2)
# Writing to sample.json
# with open("sample.json", "w") as outfile:
#    outfile.write(json_object)

with open('sample.json', 'r') as openfile: 
    # Reading from json file
    y = json.loads(openfile.read())
    people=y["People"]
    enc=0
    i=0
    while(enc==0 and i< len(people)):
        if(people[i]["Nombre"]=="sejavichan"):
            enc=1
            people[i]["Tramas"]+=1
        else:
            i+=1
    y["People"]=people
    # Writing to sample.json
    print(y)
    print(y["People"][0]["Nombre"])
#with open("sample.json", "w") as outfile:
#    outfile.write(json.dumps(y,indent=2))




