Q1 = '''select id,fname from Director where NOT EXISTS 
(select name from movie inner join moviedirector on movie.id = moviedirector.mid
where Director.id=moviedirector.did AND year<2000) 
AND EXISTS (select name from movie inner join moviedirector on movie.id = moviedirector.mid
where Director.id = moviedirector.did AND year>2000) ORDER BY Director.id ASC;'''

Q2 = '''select fname,(select m.name from movie m inner join moviedirector md on
m.id=md.mid AND md.did = d.id order by m.rank DESC,m.name ASC limit 1)
from director d limit 100;'''

Q3 = '''select * from actor where not exists(select pid from cast inner join movie
on `movie`.id=`cast`.mid where `actor`.id = `cast`.pid AND `movie`.year BETWEEN 1990 AND 2000)
ORDER BY `actor`.id DESC limit 100;'''




