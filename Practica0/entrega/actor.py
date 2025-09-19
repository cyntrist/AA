class Actor:
    def __init__(self,name,faction,hp,dp,ap): # constructor
        self.name = name;
        self.faction = faction;
        self.hp = hp;
        self.dp = dp;
        self.ap = ap;
        
    def __repr__(self):
        return f"{self.name}(Faction={self.faction},HP={self.hp}, DP={self.dp}, AP={self.ap})"