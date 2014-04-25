#encoding utf-8
import matplotlib.pyplot as plt
def is_number(s): #number within string; ex: is_number("5") = True
    try:
        float(s)
        return True
    except ValueError:
        return False

#s=raw_input('Continue? (y/n) -->')
s="y"
if (s=="y"):
	obj=open("stockInfo.txt","r")
	lines = obj.readlines()
	jorig=str(lines[0]).split(",")
	x=float(jorig[len(jorig)-1])
	obj.close()
elif s=="n":
	x=3.14
else:
	print "NGUYEN";exit()
j=[x]
cont="y"
print "STARTING!:"
while (cont=="y" or is_number(cont)):
	if is_number(cont):
		maax=int(cont);
	else:
		maax=100000;
	for i in range(1,maax):
		x=x**(x/round(x));
		j.append(x);
	cont=raw_input('Continue? (y/n/#) -->')
print "DONE!"
obj=open("stockInfo.txt","a")
#print map(str,j),lines
obj.write(","+",".join(map(str,j)))
obj.close()
fin=jorig+j
print len(fin)
plt.plot(fin[0::len(fin)/750])
#plt.ylabel('some numbers')
plt.show()


"""
jdata=urllib2.urlopen("http://quizbowldb.com/api/search/hydrogen?condition=answer&params%5Bdifficulty%5D=HS&limit=100000000")
data=json.load(jdata);
obj.write('{setName:"NAME???", info: "", termList: [\n')
for i in data["data"]["tossups"]:
	obj.write("\t{term:\""+encodeStr(i["answer"])+"\",def:\"")
	obj.write(encodeStr(i["question"])+"\"},\n")
obj.write("]},\n")
obj.close()



lines = file_1.readlines()
sentences = []
for line in lines:
    if line:
        sentences.insert(len(sentences)-1,line + '-d')
file_1.close()
file_2 = open('./output.txt', 'w+')
if len(sentences) > 0:
    for sentence in sentences:
        file_2.write(sentence)
file_2.close()
"""