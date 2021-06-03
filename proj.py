import csv
with open("data.csv",newline="") as f:
  reader = csv.reader(f)
  filedata = list(reader)

filedata.pop(0)
newdata=[]

for i in range(len(filedata)):
  num = filedata[i][1]
  newdata.append(float(num))

n=len(newdata)
total = 0

for x in newdata:
  total=total + x 
mean = total/n
print("Mean is",mean)

newdata.sort()

if n%2==0:
  median1 = float(newdata[n//2])
  median2 = float(newdata[n//2-1])
  median = (median1 + median2)/2
else:
  median = newdata[n//2]
print("Median is",median)

from collections import Counter

data = Counter(newdata)
modedataforrange = {"50-60":0,"60-70":0,"70-80":0}
for height,occurence in data.items():
  if 50<float(height)<60:
    modedataforrange["50-60"]+=occurence 
  elif 60<float(height)<70:
    modedataforrange["60-70"]+=occurence 
  elif 70<float(height)<80:
    modedataforrange["70-80"]+=occurence 
moderange,modeoccurence = 0,0
for range,occurence in modedataforrange.items():
  if occurence>modeoccurence:
    moderange,modeoccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((moderange[0] + moderange[1])/2)
print("Mode is",mode)
