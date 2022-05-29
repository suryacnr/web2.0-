#! usr/bin/env python

with open("/root/web_pentrasiton/7.dir_xxs/xsspayload") as f:
	data = f.readlines()
data= [file.strip() for file in data]
with open("/root/web_pentrasiton/7.dir_xxs/colabrater","r") as f1:
	data1 =f1.readlines()

data1= [file1.strip() for file1 in data1]

		
payload =[]
i=0
while i< len(data):
	print(data[i].replace("<REPLCE_ME>", data1[i]))
	i += 1



