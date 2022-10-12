---------------- extra -------------
i wrote a script to extract data from album qury set to help use 
do sql query to add it to your new empty sqlLite file

path : ../myScripts/hima.py

if you run the script , it will generate query to be add to the shell to create many albums 
** you should import models and datetime library . 
----------------------------------

# task 1 

## 1- create some artists
query:
Artist.objects.create(stageName = "amr diab" , SocialLink="https://www.instagram.com/amr-diab/")
Artist.objects.create(stageName = "ahmed samy" , SocialLink="https://www.instagram.com/ahmed-samy/")
Artist.objects.create(stageName = "ehab twfik" , SocialLink="https://www.instagram.com/ehab-twfik/")
Artist.objects.create(stageName = "tamer hosny" , SocialLink="https://www.instagram.com/tamer-hosny/")
Artist.objects.create(stageName = "mohamed moner" , SocialLink="https://www.instagram.com/mohamed-moner/")
Artist.objects.create(stageName = "hamo beka" , SocialLink="https://www.instagram.com/hamo-beka/")
Artist.objects.create(stageName = "mohamed hamaky" , SocialLink="https://www.instagram.com/hamky/")
Artist.objects.create(stageName = "tamer ashour" , SocialLink="https://www.instagram.com/tamer-ashour/")
Artist.objects.create(stageName = "michael jackson" , SocialLink="https://www.instagram.com/michael-jackson/")
Artist.objects.create(stageName = "billie eilish" , SocialLink="https://www.instagram.com/billie-eilish/")

result : 

## 2- list down all artists
query : 
    Artist.objects.all()
result : 
    <QuerySet [<Artist: amr diab>, <Artist: ahmed samy>, <Artist: ehab twfik>, <Artist: tamer hosny>, <Artist: mohamed moner>, <Artist: hamo beka>, <Artist: hamky>, <Artist: tamer ashour>, <Artist: michael jackson>, <Artist: billie eilish>]>

## 3- list down all artists sorted by name
query :
    Artist.objects.order_by("stageName")
result : 
    <QuerySet [<Artist: ahmed samy>, <Artist: amr diab>, <Artist: billie eilish>, <Artist: ehab twfik>, <Artist: hamky>, <Artist: hamo beka>, <Artist: michael jackson>, <Artist: mohamed moner>, <Artist: tamer ashour>, <Artist: tamer hosny>]>

## 4- list down all artists whose name starts with a
query :
    Artist.objects.filter(stageName__startswith="a")
result : 
    <QuerySet [<Artist: amr diab>, <Artist: ahmed samy>]>

## 5- in 2 different ways, create some albums and assign them to any artists
## query :
## way 1 :
    amrDiab = Artist.objects.get(stageName = "amr diab")
    album1 = Album(name = "koly gra7 part1"  , creationDate=datetime.datetime(2022,10,7,15,30),
 	 releaseDate=datetime.datetime(2022,10,7,16,30) ,cost=123.99 , artist= amrDiab)
	album1.save()
## way2 :
	amrDiab = Artist.objects.get(stageName = "amr diab")
    Album.objects.create(name = "koly gra7 part2"  , creationDate=datetime.datetime(2022,10,7,15,30),
 	releaseDate=datetime.datetime(2022,10,7,16,30) ,cost=123.99 , artist= amrDiab)
## result : 

## 6- get the latest released album
query :
    Album.objects.latest("releaseDate")
result : 
    <Album: koly gra7 part1 123.99  amr diab   2022-10-07 16:30:00+00:00>

## 7- get all albums released before today
query : 
    date = datetime.datetime.now() 
    year ,month , day = date.year , date.month, date.day 
    Album.objects.filter(releaseDate__lt =datetime.datetime(year , month ,day,23,59))
result :
    <QuerySet [<Album: koly gra7 part1 123.99  amr diab   2022-10-07 16:30:00+00:00>, <Album: lovely 1231.99  billie eilish   2020-10-09 21:48:20+00:00>, <Album: ana ndman 20.5  tamer ashour   2019-11-07 15:13:10+00:00>, <Album: salam ya sa7be 500.0  tamer hosny   2011-10-06 15:13:55+00:00>, <Album: rage3lk tane 1000.0  ehab twfik   2001-12-06 15:14:33+00:00>]>

## 8- get all albums released today or before but not after today
query :
    date = datetime.datetime.now(); 
    start_date = datetime.datetime(date.year, date.month ,date.day,0,0)
    end_date = datetime.datetime(date.year, date.month ,date.day,23,59)
    Album.objects.filter(releaseDate__range =(start_date ,end_date))
result :
    <QuerySet [<Album: koly gra7 part1 123.99  amr diab   2022-10-07 16:30:00+00:00>]>

## 9- count the total number of albums 
query:
    Album.objects.count()
result:
    5

## 10- in 2 different ways, for each artist, list down all of his/her albums 
 
## way 1 : 
query : 
    artists = Artist.objects.all() 
    for cur_artist in artists:
        albums = Album.objects.filter(artist=cur_artist)
        print(f"{cur_artist.stageName} : ")
        for album in albums:
            print(f"-- {album.name}")
result : 
    amr diab : 
    -- koly gra7 part1
    ahmed samy :
    ehab twfik :
    -- rage3lk tane
    tamer hosny :
    -- salam ya sa7be
    mohamed moner :
    hamo beka :
    hamky :
    tamer ashour :
    -- ana ndman
    michael jackson :
    billie eilish :
    -- lovely

## way 2 :
query : 
    artists = Artist.objects.all()
    for artist in artists : 
        print(artist.stageName)
        artist.album_set.all()   
result:
    amr diab
    <QuerySet [<Album: koly gra7 part1 123.99  amr diab   2022-10-07 16:30:00+00:00>]>
    ahmed samy
    <QuerySet []>
    ehab twfik
    <QuerySet [<Album: rage3lk tane 1000.0  ehab twfik   2001-12-06 15:14:33+00:00>]>
    tamer hosny
    <QuerySet [<Album: salam ya sa7be 500.0  tamer hosny   2011-10-06 15:13:55+00:00>]>
    mohamed moner
    <QuerySet []>
    hamo beka
    <QuerySet []>
    hamky
    <QuerySet []>
    tamer ashour
    <QuerySet [<Album: ana ndman 20.5  tamer ashour   2019-11-07 15:13:10+00:00>]>
    michael jackson
    <QuerySet []>
    billie eilish
    <QuerySet [<Album: lovely 1231.99  billie eilish   2020-10-09 21:48:20+00:00>]>


## 11-list down all albums ordered by cost then by name
query : 
    Album.objects.order_by("cost", "name")
result : 
    <QuerySet [<Album: ana ndman 20.5  tamer ashour   2019-11-07 15:13:10+00:00>, <Album: koly gra7 part1 123.99  amr diab   2022-10-07 16:30:00+00:00>, <Album: salam ya sa7be 500.0  tamer hosny   2011-10-06 15:13:55+00:00>, <Album: rage3lk tane 1000.0  ehab twfik   2001-12-06 15:14:33+00:00>, <Album: lovely 1231.99  billie eilish   2020-10-09 21:48:20+00:00>]>
