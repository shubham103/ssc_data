raw_data=open("/home/shubham/Desktop/ssc_practice_website/test_data.txt","r")
final_data=open("/home/shubham/Desktop/ssc_practice_website/final_data.txt","a")
count =0
string=""
while True:
    line=raw_data.readline()
    if not line:
        break
    if count==0:
        string=line[:-1]
        count+=1
        continue
    if line[0] == ',':
        string+=line[:-1]
    else:
        
        print(string)
        final_data.write(string+"\n")
        string=line[:-1]

raw_data.close()
final_data.close()
