import json
#dump: It will dump the python object or data in to a json file
#dumps:it will convert python object to string;
#loads:Converts a JSON string into a Python object

#file=open(r"D:\\OLD F(Life)\\BRoadridge\\NandaAnnaPrepared\\Json.json",'r')
#content=json.load(file)

#loads

file=open(r"D:\\OLD F(Life)\\BRoadridge\\NandaAnnaPrepared\\Json.json",'r')
print(json.loads(file,))



#dump
'''
data ={
    "name":"subbu",
    "age":95,
    "properties":["white","Too Long"]

}

file=open(r"D:\\OLD F(Life)\\BRoadridge\\NandaAnnaPrepared\\data.json",'w')
json.dump(data,file)
print(type(data))

words=["hello","how","are","you"]

file=open(r"D:\\OLD F(Life)\\BRoadridge\\NandaAnnaPrepared\\data.json",'w')
json.dump(words,file)
print(type(words))

'''



#dumps
'''
data ={
    "name":"subbu",
    "age":95,
    "properties":["white","Too Long"]
}

string=json.dumps(data)
print(string)
print(type(string))

words=["hello","how","are","you"]
print(type(words))
string=json.dumps(words)
print(string)
print(type(string))
'''









