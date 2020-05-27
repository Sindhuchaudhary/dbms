Q1 = '''select fname,lname from Actor inner join Cast on id = pid where mid = 12148;'''

Q2 = '''select COUNT(mid) from Cast inner join Actor on id=pid WHERE fname = "Harrison (I)" AND lname = "Ford";'''

Q3 = '''select distinct(pid) from Cast inner join Movie on id=mid WHERE name LIKE "Young Latin Girls%";'''

Q4 = '''select count(distinct(pid)) from Cast inner join Movie on  mid=id WHERE year BETWEEN 1990 AND 2000;'''


    