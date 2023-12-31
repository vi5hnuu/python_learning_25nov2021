from abc import ABC,abstractmethod
class character(ABC):
    @abstractmethod
    def patriotism(self):
        pass

class Actor:
    def style(self):
        print('>>Actor.style:')
class person(Actor,character):
    def do_acting(self):
        print('>>person.doActing')

    def style(self):
        print('>>person.style')

    def patriotism(self):
        print('>>person.patriotism')

p=person()
p.patriotism()
p.style()
p.do_acting()