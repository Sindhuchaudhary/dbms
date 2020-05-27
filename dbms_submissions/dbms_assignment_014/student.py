class DoesNotExist(Exception):
    pass


class MultipleObjectsReturned(Exception):
    pass


class InvalidField(Exception):
    pass


class Student:
    def __init__(self, student_id = None ,name = None, age = None , score = None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score = score
        
    @staticmethod
    def aggregations(agg=None,field='',**kwargs):
        list = ["student_id","name","age","score",""]
        multiple_values = []
        
        if field not in list:
            raise InvalidField
        for k,v in kwargs.items():
            q = k.split('__')
            
            if q[0] not in list:
                raise InvalidField
            operation = {"lt":"<","lte":"<=","gt":">","gte":">=","eq":"=","neq":"<>"}
            if len(q) == 1:
                val = "{} {} '{}'".format(q[0],operation['eq'],v)
            elif q[1] == "in":
                v = tuple(v)
                val = "{} {} {}".format(q[0],'IN',v)
            elif q[1] == "contains":
                val = "{} {} '%{}%'".format(q[0],'LIKE',v) 
            else:
                val = "{} {} '{}'".format(q[0],operation[q[1]],v)
            multiple_values.append(val)
        x = ' AND '.join(multiple_values)
        
        
        if x == "":
            data = read_data("SELECT {}({}) FROM Student".format(agg,field))
        else:
            data = read_data("SELECT {}({}) FROM Student where {}".format(agg,field,x))
            
        return data[0][0] 
    
    @classmethod
    def avg(cls, field, **kwargs):
                
        ans = cls.aggregations('AVG', field, **kwargs)
        return ans
    
    @classmethod
    def min(cls, field, **kwargs):
                
        ans = cls.aggregations('MIN', field, **kwargs)
        return ans
        
    @classmethod
    def max(cls, field, **kwargs):
                
        ans = cls.aggregations('MAX', field, **kwargs)
        return ans
    
    @classmethod
    def sum(cls, field, **kwargs):
                
        ans = cls.aggregations('SUM', field, **kwargs)
        return ans
    @classmethod
    def count(cls, field="", **kwargs):
                
        ans = cls.aggregations('COUNT', field, **kwargs)
        return ans
        
def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    c = connection.cursor() 
    c.execute("PRAGMA foreign_keys=on;") 
    c.execute(sql_query) 
    connection.commit() 
    connection.close()

def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    c = connection.cursor() 
    c.execute(sql_query) 
    ans= c.fetchall()  
    connection.close()
    return ans
        