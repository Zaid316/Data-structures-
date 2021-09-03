class Footballer:
    def __init__ (self,name,position,age,club):
        self.name=name
        self.position=position
        self.age=age
        self.club=club

    def footballer_profile(self):
        print("NAME: ",self.name,)
        print("POSITION: ",self.position,)
        print("AGE: ",self.age,)
        print("CLUB: ",self.club,)

p1=Footballer('Messi','RW','33','FC Barcelona')
p2=Footballer('Werner','ST','24','Chelsea FC')
p3=Footballer('Van Dijk','CB','29','Liverpool FC')
p1.footballer_profile()
p2.footballer_profile()
p3.footballer_profile()

        