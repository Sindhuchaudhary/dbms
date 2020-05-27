class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass

def write_data(sql_query):
	    import sqlite3
	    connection = sqlite3.connect('students.sqlite3')
	    crsr = connection.cursor() 
	    crsr.execute("PRAGMA foreign_keys=on;") 
	    crsr.execute(sql_query) 
	    connection.commit() 
	    connection.close()

def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect('students.sqlite3')
    crsr = connection.cursor() 
    crsr.execute(sql_query)
    ans= crsr.fetchall()
    connection.close()
    return ans

class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
        self.student_id=None
        
    @staticmethod    
    def get(student_id=0,name='',age=0,score=-1,**kwargs):
        if student_id != 0:
            record = read_data(f'select * from Student where student_id={student_id}')
        elif name != '':
            record = read_data(f'select * from Student where name = "{name}"')
        elif age != 0:
            record = read_data(f'select * from Student where age={age}')
        elif score != -1:
            record = read_data(f'select * from Student where score = {score}')
        else:
            raise InvalidField("InvalidField")
            
        if len(record)==0:
            raise DoesNotExist("DoesNotExist")
        elif len(record)>1:
            raise MultipleObjectsReturned("MultipleObjectsReturned")
        else:
            result = Student(record[0][1],record[0][2],record[0][3])
            result.student_id = record[0][0]
            return result 
    
    def delete(self):
        query = f'delete from Student where student_id={self.student_id}'
        write_data(query)
        
    def save(self):
        import sqlite3
        connection = sqlite3.connect('students.sqlite3')
        crsr = connection.cursor() 
        crsr.execute("PRAGMA foreign_keys=on;") 
	    
	    
        if self.student_id == None:
            query = f'insert into Student(name,age,score) values("{self.name}",{self.age},{self.score})'
            crsr.execute(query)
            self.student_id = crsr.lastrowid
        elif "select {} from Student where student_id not in (select student_id from Student)".format(self.student_id):
            query = "insert or replace into Student(student_id,name,age,score) values({},'{}',{},{})".format(self.student_id,self.name,self.age,self.score)
            crsr.execute(query)
            self.student_id=crsr.lastrowid
        else:
            query = f'update Student set name="{self.name}",age={self.age},score={self.score} where student_id={self.student_id}'
            crsr.execute(query)
        connection.commit()
        connection.close()
        
        