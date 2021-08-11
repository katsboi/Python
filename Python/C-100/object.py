class Game(object):
    def __init__(self,name,genre,size,developer, playerfeedback = None):
        self.name= name
        self.genre= genre
        self.size= size
        self.developer= developer
        self.playerfeedback = playerfeedback or {}

    def setFeedback(self, review, feedback):
        self.playerfeedback[review] = feedback
    
    def getFeedback(self, review):
        return self.playerfeedback[review]
      
    def ratings(self):
          return self.playerfeedback


among_us= Game("Among Us","puzzle/mystery","indie","innersloth",{3, 6.5, 9.4, 8.7})
lastofus= Game("Last Of Us","thriller/action","AAA","naughtyDog",{9.2, 6, 8.2, 7.1})

print(among_us.ratings())
print(lastofus.ratings())