Q1 = '''select `actor`.id,`actor`.fname,`actor`.lname,`actor`.gender
from actor inner join cast on `actor`.id=`cast`.pid inner join movie on 
`cast`.mid=`movie`.id where `movie`.name like "Annie%";'''

Q2 = '''select `movie`.id,`movie`.name,`movie`.rank ,`movie`.year 
from movie inner join moviedirector on `moviedirector`.mid=`movie`.id 
inner join director on `director`.id=`moviedirector`.did where 
`director`.fname = "Biff" AND `director`.lname="Malibu" AND `movie`.year 
in (1999,1994,2003) order by `movie`.rank DESC,`movie`.year ASC;'''

Q3 = '''select m.year,count(m.id) as no_of_movies from movie m group by 
m.year having avg(rank)>(select avg(rank) from movie) order by m.year ASC;'''

  
Q4 = '''select id,name,year,rank from movie where year = 2001 AND 
rank<(select avg(rank) from movie) order by rank DESC limit 10;'''

Q6 = '''select distinct(`actor`.id) from actor inner join  
cast on `cast`.pid=`actor`.id  inner join movie on `cast`.mid=`movie`.id 
group by `actor`.id ,`movie`.id having count(distinct(`cast`.role))>1 limit 100;'''

Q7 = '''select fname,count(fname) from di	rector group by fname having count(fname)>1 ;'''

Q8 = '''select id,fname,lname from director where exists (select * from cast inner join 
moviedirector on `moviedirector`.mid =`cast`.mid  where  `director`.id=`moviedirector`.did 
group by `moviedirector`.did,`cast`.mid having count(distinct `cast`.pid)>=100) AND not exists
(select * from cast inner join moviedirector on `moviedirector`.mid=`cast`.mid where 
`director`.id=`moviedirector`.did group by `moviedirector`.did,`cast`.mid having 
count(distinct `cast`.pid)<100);'''












