class Fighter:
    def __init__(self, name, spec, hpMax, shotsMax, rocketsMax = 0, grenadesMax = 0, medkitsMax = 0, smokesMax = 0):
        self.name = name
        self.spec = spec
        
        # Reloadables
        self.hpMax = hpMax
        self.hp = hpMax
        self.shotsMax = shotsMax
        self.shots = shotsMax
        
        # Unreloadables
        self.rocketsMax = rocketsMax
        self.rockets = rocketsMax
        self.grenadesMax = grenadesMax
        self.grenades = grenadesMax
        self.medkitsMax = medkitsMax
        self.medkits = medkitsMax
        self.smokesMax = smokesMax
        self.smokes = smokesMax

    def restock(self):
        self.hp = self.hpMax
        self.shots = self.shotsMax
        self.grenades = self.grenadesMax
        self.rockets = self.rocketsMax
        self.medkits = self.medkitsMax
        self.smokes = self.smokesMax
        print(f'Restocked all items of {self.name}')
        self.info()
        return
        
    def reload(self):
        self.shots=self.shotsMax
        print(f'{self.name} reloaded back to {self.shots}/{self.shotsMax} shots.')
        self.info()
        return
    
    def heal(self, amount):
        self.hp += amount
        if self.hp > self.hpMax:
            self.hp = self.hpMax
        print(f'{self.name} healed {amount} to reach {self.hp}/{self.hpMax} hp.')
        self.info()
        return
    
    def damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f'{self.name} took {amount} damage to reach {self.hp}/{self.hpMax} hp.')
        if self.hp == 0:
            print(f'{self.name} has 0 hp and is downed.')
        self.info()
        return
    
    def fire(self, amount = 1):
        if amount > self.shots:
            print('Not enough ammunition!')
        else:
            self.shots -= amount
            print (f'{self.name} fired {amount} shot(s), leaving them with {self.shots}/{self.shotsMax} shots.')
        self.info()
        return
    
    def nade(self):
        if self.grenades == 0:
            print('No grenades available!')
        else:
            self.grenades -= 1
            print(f'{self.name} throws a grenade, leaving them with {self.grenades}')
        self.info()
        return
    
    def launch(self):
        if self.rockets == 0:
            print('No rockets available!')
        else:
            self.rockets -= 1
            print(f'{self.name} launches a rocket, leaving them with {self.rockets}')
        self.info()
        return

    def smoke(self):
        if self.smokes == 0:
            print('No smokes available!')
        else:
            self.smokes -= 1
            print(f'{self.name} throws a smoke, leaving them with {self.smokes}')
        self.info()
        return

    def aid(self):
        if self.medkits == 0:
            print('No medkits available!')
        else:
            self.medkits -= 1
            print(f'{self.name} uses a medkit, leaving them with {self.medkits}')
        self.info()
        return
    
    def use(self):
        print(f'\nWhat item is {self.name} using?\nPick from the following options:')
        print('Grenades: g\nRockets: r\nMedkits: m\nSmokes: s')
        item = input().upper()
        if item == 'G':
            self.nade()
        elif item == 'R':
            self.launch()
        elif item == 'M':
            self.aid()
        elif item == 'S':
            self.smoke()
        self.info()
        return

    
    def info(self):
        print (f'\n{self.name}\nClass: {self.spec}')
        data = [
            ['hp' , self.hp , self.hpMax],
            ['Shots' , self.shots , self.shotsMax],
            ['Grenades' , self.grenades , self.grenadesMax],
            ['Rockets' , self.rockets , self.rocketsMax],
            ['Medkits' , self.medkits , self.medkitsMax],
            ['Smokes' , self.smokes , self.smokesMax]
            ]
        for i in data:
            if i[2] != 0:
                #print(f'{i[0]}: {i[1]}/{i[2]}')
                print(f'{i[0]}:' + ' '*(8-len(i[0])) + '|'*i[1] + '.'*(i[2]-i[1]))
        print('\n')
        return

class Sniper(Fighter):
    def __init__(self, name):
        super().__init__(name, spec='Sniper', hpMax=6, shotsMax=4)


class Heavy(Fighter):
    def __init__(self, name):
        super().__init__(name, spec='Heavy',hpMax=6, shotsMax=3, grenadesMax = 2, rocketsMax = 1)


class Support(Fighter):
    def __init__(self, name):
        super().__init__(name, spec='Support', hpMax=6, shotsMax=4, smokesMax = 1)


class Assault(Fighter):
    def __init__(self, name, grenadesMax = 1):
        super().__init__(name, spec='Assault', hpMax=6, shotsMax=4, grenadesMax = 1)

def setup():
    global player_dict
    player_dict = {}
    while True:
        name = input('\nName: ')
        if name == '':
            break
        
        switcher={
            '1': Sniper(name),
            '2': Assault(name),
            '3': Support(name),
            '4': Heavy(name)
            }
    
        Spec = '0'
        options = ['','1','2','3','4']
        while True:
            print('\nClass:\n1: Sniper\n2: Assault\n3: Support\n4: Heavy')
            Spec = (input())
            if Spec in options:
                break
                    
            
        if Spec == '':
            continue
        else:
            
            globals()[name] = switcher.get(Spec)
            globals()[name].info()
            player_dict[str(len(player_dict)+1)] = name
    choosePlayer()
    return

def choosePlayer():

    while True:
        print('Who is doing stuff?')
        for i in range(1,len(player_dict)+1):
            print(f'{i}: {player_dict[str(i)]}')
        chosen = input()
        if chosen not in player_dict:
            setup()
            break
            
        elif chosen in player_dict:
            chooseAction(player_dict[chosen])
    return
    
def chooseAction(Player):
    print(f'{Player} is doing stuff')
    stuff = {
        '1':'fire'
        '2':'damage'
        '3':'heal'
        '4':'reload'
        '5':'use'
        '6':'restock
        }
    return





setup()

