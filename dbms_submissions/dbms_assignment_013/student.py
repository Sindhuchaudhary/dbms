class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass

def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_stu
	dents.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()


def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
	
	


class Student:  

    def __init__(self,name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)


    def delete(self):
        sql_query='delete from student where student_id={}'.format(self.student_id)
        write_data(sql_query)

    def save(self):
        if self.student_id is None:
            query="insert into student(name,age,score) values ('{}',{},{})".format(self.name,self.age,self.score)
            write_data(query)
            q1='select student_id from student where name="{}" and age={} and score={}'.format(self.name,self.age,self.score)
            a=read_data(q1)   
            self.student_id=a[0][0]
        else:
            sql_query="update student set  student_id={},name='{}',age={},score={} where student_id={}".format(self.student_id,self.name,self.age,self.score,self.b)
            write_data(sql_query)


            
        
    @classmethod
    def get(cls,**kwargs):
        for k,v in kwargs.items():
            cls.a=k
            cls.b=v
            if str(k) not in ('name','age','score','student_id'):
                raise InvalidField 
           
        query="select * from student where {} = '{}'".format(cls.a,cls.b)
        
        res=read_data(query)
        if len(res)>1:
            raise MultipleObjectsReturned
        elif len(res)==0:
            raise DoesNotExist
        elif len(res)==1:
            c=Student(res[0][1],res[0][2],res[0][3])
            c.student_id=res[0][0]
            return c      
    @classmethod
    def filter(cls,**kwar):
        oper_list = ['lt','lte','gt','gte','neq','in','contains','eq']
        for key,value in kwar.items():
            cls.x=key
            cls.y=value

            q=key.split('__')
            if q[0] not in ('student_id','name','age','score'):
                raise InvalidField

            elif key in ('student_id','name','age','score'):
                sql_query="select * from student where {}='{}'".format(cls.x,cls.y)
                r=read_data(sql_query)

            elif q[1]=='lt':
                sql_query="select * from student where {}<'{}'".format(q[0],cls.y)
                r=read_data(sql_query)

            elif q[1]=='lte':
                sql_query="select * from student where {}<='{}'".format(q[0],cls.y)
                r=read_data(sql_query)

            elif q[1]=='gt':
                sql_query="select * from student where {}>'{}'".format(q[0],cls.y)
                r=read_data(sql_query)

            elif q[1]=='gte':
                sql_query="select * from student where {}>='{}'".format(q[0],cls.y)
                r=read_data(sql_query)

            elif q[1]=='neq':
                sql_query="select * from student where {}<>'{}'".format(q[0],cls.y)
                r=read_data(sql_query)

            elif q[1]=='in':
                o=tuple(cls.y)
                sql_query="select * from student where {} in {}".format(q[0],o)
                r=read_data(sql_query)

            elif q[1]=='contains':
                sql_query="select * from student where {} like '%{}%'".format(q[0],cls.y)
                r=read_data(sql_query)
                
            elif q[1] in oper_list:
                sql_query = "select * from Student where {} like '{}'".format(q[0],cls.y)
                r = read_data(sql_query)
            result = []   
            
            if len(r) == 0:
                 return result
            else:
                for i in r:
                    b=Student(i[1],i[2],i[3])
                    b.student_id=i[0]
                    result.append(b)
        return result

