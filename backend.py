from pandas import *
import re

class Person:
    def __init__(self, userId, password):
        self.User_ID=userId
        self.Password=password
        self.classno=None
        self.FirstName=None
        self.LastName=None
        self.Department=None
        self.Age=None

    def User_Authentication(self):           #Check if given user id exists and database and check whether password matches
        dataframe=read_csv('data.csv')            #Decrease remaining tries for incorrect attempts
        ID_List=list(dataframe['UserID'])
        if self.User_ID in ID_List:            
            indx=ID_List.index(self.User_ID)
            if dataframe['Class'][indx]!=self.classno:
                return 1
            if dataframe['Tries'][indx]==0:
                return 2
            if dataframe['Password'][indx]==self.Password:
                dataframe.at[indx,'Tries']=3
                dataframe.to_csv('data.csv', index=False)
                return 0
            else:
                dataframe.at[indx,'Tries']-=1
                dataframe.to_csv('data.csv', index=False)
                return 1
        else: return 1

    def User_Registration(self):        #Check if given email and password match criteria and add to database, otherwise return error
        if not(re.match(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.User_ID)):
            return 1
        
        dataframe=read_csv('data.csv')
        ID_List=list(dataframe['UserID'])
        if self.User_ID in ID_List:
            return 2
        
        if len(self.Password)<8 | len(self.Password)>12:
            return 3
        
        special_char=re.compile("[a-z]")
        if special_char.search(self.Password)==None:
            return 4
        special_char=re.compile("[A-Z]")
        if special_char.search(self.Password)==None:
            return 4
        special_char=re.compile("[0-9]")
        if special_char.search(self.Password)==None:
            return 4
        
        special_char=re.compile("[!@#$%&*]")
        if special_char.search(self.Password)==None:
            return 5
        
        if ' ' in self.Password:
            return 6
        
        data={'UserID':[self.User_ID], 'Password':[self.Password], 'Class':[self.classno], 'Tries':[3]}
        dataframe=DataFrame(data)
        dataframe.to_csv('data.csv', mode='a', index=False, header=False)
        return 0
    
    def User_Deregistration(self):                        #delete account data from database
        dataframe=read_csv('data.csv')
        indx=list(dataframe['UserID']).index(self.User_ID)
        dataframe.drop([indx], inplace=True, errors='ignore')
        dataframe.to_csv('data.csv', index=False)


class Teacher(Person):
    def __init__(self, userId, password):
        super().__init__(userId, password)
        self.Designation=None
        self.YearOfJoining=None
        self.Office=None

    def Retrieve_Data(self):              #assign database values to object attributes
        dataframe=read_csv('data.csv')
        indx=list(dataframe['UserID']).index(self.User_ID)
        if notna(dataframe['Firstname'][indx]): self.FirstName=dataframe['Firstname'][indx]
        if notna(dataframe['Lastname'][indx]): self.LastName=dataframe['Lastname'][indx]
        if notna(dataframe['Department'][indx]): self.Department=dataframe['Department'][indx]
        if notna(dataframe['Age'][indx]): self.Age=dataframe['Age'][indx]
        if notna(dataframe['Designation'][indx]): self.Designation=dataframe['Designation'][indx]
        if notna(dataframe['YearOfJoining'][indx]): self.YearOfJoining=dataframe['YearOfJoining'][indx]
        if notna(dataframe['Office'][indx]): self.Office=dataframe['Office'][indx]

    def Save_Data(self):                  #store object attributes in database
        dataframe=read_csv('data.csv')
        indx=list(dataframe['UserID']).index(self.User_ID)
        dataframe.at[indx,'Firstname']=self.FirstName
        dataframe.at[indx,'Lastname']=self.LastName
        dataframe.at[indx,'Department']=self.Department
        dataframe.at[indx,'Age']=self.Age
        dataframe.at[indx,'Designation']=self.Designation
        dataframe.at[indx,'YearOfJoining']=self.YearOfJoining
        dataframe.at[indx,'Office']=self.Office
        dataframe.to_csv('data.csv', index=False)


class Student(Person):
    def __init__(self, userId, password):
        super().__init__(userId, password)
        self.RollNo=None
        self.BatchYear=None

    def Retrieve_Data(self):              #assign database values to object attributes
        dataframe=read_csv('data.csv')
        indx=list(dataframe['UserID']).index(self.User_ID)
        if notna(dataframe['Firstname'][indx]): self.FirstName=dataframe['Firstname'][indx]
        if notna(dataframe['Lastname'][indx]): self.LastName=dataframe['Lastname'][indx]
        if notna(dataframe['Department'][indx]): self.Department=dataframe['Department'][indx]
        if notna(dataframe['Age'][indx]): self.Age=dataframe['Age'][indx]
        if notna(dataframe['RollNo'][indx]): self.RollNo=dataframe['RollNo'][indx]
        if notna(dataframe['BatchYear'][indx]): self.BatchYear=dataframe['BatchYear'][indx]
        if notna(dataframe['Degree'][indx]): self.Degree=dataframe['Degree'][indx]

    def Save_Data(self):                  #store object attributes in database
        dataframe=read_csv('data.csv')
        indx=list(dataframe['UserID']).index(self.User_ID)
        dataframe.at[indx,'Firstname']=self.FirstName
        dataframe.at[indx,'Lastname']=self.LastName
        dataframe.at[indx,'Department']=self.Department
        dataframe.at[indx,'Age']=self.Age
        dataframe.at[indx,'RollNo']=self.RollNo
        dataframe.at[indx,'BatchYear']=self.BatchYear
        dataframe.at[indx,'Degree']=self.Degree
        dataframe.to_csv('data.csv', index=False)


class UG_Student(Student):
    def __init__(self, userId, password):
        super().__init__(userId, password)
        self.Degree=None


class PG_Student(Student):
    def __init__(self, userId, password):
        super().__init__(userId, password)
        self.Degree=None