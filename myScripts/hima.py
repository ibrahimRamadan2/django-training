from datetime import datetime
# s => Albums.objects.all()  from my old sqlLite database 
s = """<Album: hima,2022-10-07 15:30:00+00:00,2022-10-07 16:30:00+00:00,123.99,amr diab,False>, <Album: lovely,2020-10-07 21:48:20+00:00,2020-10-09 21:48:20+00:00,1231.99,billie eilish,False>, <Album: ana ndman,2019-10-07 15:13:09+00:00,2019-11-07 15:13:10+00:00,20.5,tamer ashour,False>, <Album: salam ya sa7be,2010-10-06 15:13:49+00:00,2011-10-06 15:13:55+00:00,500.0,tamer hosny,False>, <Album: rage3lk tane,2001-10-06 15:14:32+00:00,2001-12-06 15:14:33+00:00,1000.0,ehab twfik,False>, <Album: fake album1,2022-10-09 08:34:20+00:00,2022-10-09 08:34:22+00:00,12313.0,tamer hosny,False>, <Album: ana hena wala henak,2022-10-09 08:36:06+00:00,2022-10-09 08:36:07+00:00,1231.0,tamer hosny,True>, <Album: bla bla,2022-10-09 12:14:35+00:00,2022-10-09 12:14:36+00:00,123123.0,billie eilish,True>, <Album: dqwe,2022-10-09 12:14:49+00:00,2022-10-09 12:14:50+00:00,41231.0,billie eilish,True>, <Album: New Album,2022-10-09 12:15:09+00:00,2022-10-09 12:15:10+00:00,61231.0,amr diab,True>, <Album: New Album 12,2022-10-09 12:15:29+00:00,2022-10-09 12:15:30+00:00,13251231.0,michael jackson,True>, <Album: the end,2022-10-09 12:16:32+00:00,2022-10-09 12:16:33+00:00,31111.0,amr diab,True>, <Album: the end 2,2022-10-09 12:16:46+00:00,2022-10-09 12:16:47+00:00,1313.0,amr diab,True>"""
def getDateTime(str2):
  lst= str2.split(" ")
  date = lst[0] 
  time = lst[1]
  l1 =date.split('-')
  l2= time.split(':')
  
  for i in range(len(l1)):
    l1[i] = str(int(l1[i]))
  for i in range(2):
    l2[i] = str(int(l2[i]))
  # creationDate=datetime.datetime(2022,10,7,15,30)
  return f"datetime.datetime({l1[0]},{l1[1]},{l1[2]},{l2[0]},{l2[1]})"


lst = s.split(", ")
cnt=0
x = str(123)
print("\n")
for i in lst :
    s2 =i[8:-1]
    lst2 =s2.split(",")
    # hima  ,2022-10-07 15:30:00+00:00  ,2022-10-07 16:30:00+00:00  ,123.99  ,amr diab,  False
    name= lst2[0]
    creationData= getDateTime(lst2[1]) 
    releaseData = getDateTime(lst2[2]) 
    cost = lst2[3]
    artistName = lst2[4] 
    artistquery = f"var_{cnt} = Artist.objects.get(stageName=\"{artistName}\")"
    isAccepted = lst2[5]
  #   amrDiab = Artist.objects.get(stageName = "amr diab")
  #   Album.objects.create(name = "koly gra7 part2"  , creationDate=datetime.datetime(2022,10,7,15,30),
 	#  releaseDate=datetime.datetime(2022,10,7,16,30) ,cost=123.99 , artist= amrDiab)
    
    result1= artistquery
    result2= f"Album.objects.create(name =\"{name}\", creationDate={creationData},releaseDate={releaseData} ,cost={cost} , artist= var_{cnt})"
    cnt+=1
    print(result1)
    print(result2)
    print("\n")