Q1 = '''select COUNT(id) from Movie WHERE year < 2000;'''

Q2 = '''select AVG(rank) from Movie WHERE year = 1991;'''

Q3 = '''select MIN(rank) from Movie WHERE year = 1991;'''

Q4 = '''select fname,lname from Actor inner join Cast on id = pid where mid = 27;''' 

Q5 = '''select COUNT(mid) from Cast inner join Actor on id=pid WHERE fname = "Jon" AND lname = "Dough";'''

Q6 = '''select name from Movie  WHERE (name LIKE "Young Latin Girls%") AND (year BETWEEN 2003 AND 2006);'''

Q7 = '''select distinct fname,lname from ((Director inner join MovieDirector on Director.id = MovieDirector.did) inner join Movie on MovieDirector.mid = Movie.id) where name LIKE "Star Trek%" GROUP BY Director.id HAVING COUNT(Movie.id>=1);'''


Q8 = '''select * from Movie  join (Director inner join Actor on Director.fname = "Jackie" AND Actor.fname = "Jackie") ORDER BY name ASC;''' 

Q9 = '''select fname,lname FROM Director INNER JOIN MovieDIRECTOR ON `Director`.`id`=did INNER JOIN Movie ON `Movie`.`id`=mid WHERE year = 2001 GROUP BY did HAVING COUNT(mid)>=4 ORDER BY fname ASC,lname DESC;'''

Q10 = '''select gender, COUNT(gender) from Actor GROUP BY gender ORDER BY gender ASC;'''

Q11 = '''select m1.name,m2.name,m1.rank,m1.year from Movie m1 CROSS JOIN Movie m2 where m1.year = m2.year AND m1.rank = m2.rank AND m1.name != m2.name  ORDER BY m1.name limit 100 ;'''  

Q12 = '''select a.fname,m.year,AVG(rank) from Movie m inner join Cast c on  c.mid=m.id inner join Actor a on a.id=c.pid GROUP BY m.year,a.id ORDER BY a.fname ASC,m.year DESC LIMIT 100;'''   

Q13 = '''select `Actor`.fname,`Director`.fname,AVG(rank) AS score  from Actor inner join Cast on `Actor`.id=`Cast`.pid inner join Movie on `Movie`.id=`Cast`.mid inner join MovieDirector on `Movie`.id=`MovieDirector`.mid inner join Director on `Director`.id=`MovieDirector`.did GROUP BY `Actor`.id,`Director`.id HAVING COUNT(`Cast`.mid)>=5 ORDER BY score DESC, `Director`.fname ASC,`Actor`.fname DESC LIMIT 100;'''                                         c