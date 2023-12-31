class avgadj:
    def __init__(self,lst):
        self.__data=lst;
        self.__len=len(lst)
        self.__first=0;
        self.__sec=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.__sec==self.__len:
            raise StopIteration
        self.__avg=(self.__data[self.__first]+self.__data[self.__sec])/2
        self.__first+=1
        self.__sec+=1
        return self.__avg


lst=[10,20,30,40,50,60,70,80]
col=avgadj(lst)
for val in col:
    print(val)

    #check next programm generators

