class organism(object):
    def __init__(self):
        self.breath=True
        self.language=False

class animal(organism):
    def __init__(self):
        super(animal,self).__init__()
        self.photosynthesis=False
        self.motion=True

class vertebrate(animal):
    def __init__(self):
        super(vertebrate,self).__init__()
        self.spine=True
            
class mammal(vertebrate):
    def __init__(self):
        super(mammal,self).__init__()
        self.egg=False
    def where(self):
        print "They are common in life."

class dog(mammal):
    def __init__(self,name,owner):
        super(dog,self).__init__()
        self.lifelong=False
        self.superlarge=False
        self.pet=True
        self.name=name
        self.owner=owner
    def eat(self):
        print "Cannot eat!"      
#input lines below into the python console
#>>rover=*.dog('Rover','Sherry')
#>>rover.name
#'Rover'
#>>rover.owner
#'Sherry'
    
#>>dick=*.dog('Dick','Richard')
#>>dick.name='Dick'
#'Dick'
#>>dick.owner='Richard'
#'Richard'
