import csv

lc =0
arr_abstrak=[]
with open('dataabstrakfff.csv','r') as abstrak_data:
    cread = csv.reader(abstrak_data)
    lot = list(cread)
    arr_abstrak = lot

newarr = []
for yy in arr_abstrak:
    if(len(yy)>0):
        temparr = []
        strr = ""
        for x in range(len(yy[0])):
            #print("cek")
            if (yy[0][x] == ';'):
                temparr.append(strr)
                strr = ""
            else:
                strr = strr + yy[0][x]

        newarr.append(temparr)


aa = 0
ab = len(newarr)
while aa<ab:
    if len(newarr[aa])==0:
        newarr.remove(newarr[aa])
        ab=ab-1
    aa=aa+1


for x in newarr:
    if(len(x)>=11):
        print(x)