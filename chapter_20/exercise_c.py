class MyString:
    def __init__(self,s=''):
        self.s=s

    def display(self):
        print(self.s)

    def tolower(self):
        self.s=self.s.lower()

    def toupper(self):
        self.s = self.s.upper()

    def __iadd__(self,other):
        self.s=self.s+other.s
        return MyString(self.s)


s1=MyString('heLlo')
s1.display()
s1.tolower()
s1.display()
s1.toupper()
s1.display()
s2=MyString('Good morning')
s1+=s2
s1.display()