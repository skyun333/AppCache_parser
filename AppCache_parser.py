import json
import sqlite3
import os
import winsound as sd

conn=sqlite3.connect('database.db')
c=conn.cursor()
path=input("Appcache가 존재하는 폴더 경로를 입력하세요 : ")
#path="C:/Users/skyun/AppData/Local/Packages/Microsoft.Windows.Search_cw5n1h2txyewy/LocalState/DeviceSearchCache"
file_list = os.listdir(path)
parsing_file=[]
for i in range(len(file_list)):
     if(file_list[i][0:8]=="AppCache"):
        parsing_file.append(file_list[i])

ex=['System.FileExtension','System.Software.TimesUsed','System.DateAccessed','System.Tile.EncodedTargetPath','System.ItemNameDisplay']

for i in range(len(parsing_file)):
    file_open=path+"/"+parsing_file[i]    
    with open(file_open,"r",encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        print(len(json_data))
        for j in range(len(json_data)):
            print("---------------------------------------")
            
            sql='INSERT INTO AppCache (%s,%s,%s,%s,%s) VALUES ("%s","%s","%s","%s","%s");'%(str(ex[0].split(".")[-1]),str(ex[1].split(".")[-1]),str(ex[2].split(".")[-1]),str(ex[3].split(".")[-1]),str(ex[4].split(".")[-1]),str(json_data[j][ex[0]]['Value']),str(json_data[j][ex[1]]['Value']),str(json_data[j][ex[2]]['Value']),str(json_data[j][ex[3]]['Value']),str(json_data[j][ex[4]]['Value']))
            c.execute(sql)
conn.commit()
c.close()
conn.close()