# This Python file uses the following encoding: utf-8
import urllib2
import json
def encodeStr(str):
	return str.encode("utf-8").replace('"','\\"').replace('“','\\"').replace('”','\\"').replace("’","'")
obj=open("output.html","w+")
jdata=urllib2.urlopen("http://quizbowldb.com/api/search/hydrogen?condition=answer&params%5Bdifficulty%5D=HS&limit=100000000")
data=json.load(jdata);
obj.write('{setName:"NAME???", info: "", termList: [\n')
for i in data["data"]["tossups"]:
	obj.write("\t{term:\""+encodeStr(i["answer"])+"\",def:\"")
	obj.write(encodeStr(i["question"])+"\"},\n")
obj.write("]},\n")
obj.close()