import math
import matplotlib.pyplot as plt

class Nucleus:
    def __init__(self, Z, A):
        self.A = A #число протонов
        self.Z = Z #массовое число
        self.N = A-Z #число нейтронов
    def z(self):
        return self.Z
        
    def energy(self): #формула для расчета энергии с формулой Вайзекера
        a_1 = 15.8  # объемный член
        a_2 = 17.2  # поверхностный член
        a_3 = 0.71  # кулоновский член
        a_4 = 23.7  # асимметричный член
        if self.A%2 != 0:
            a_5=0
        elif self.Z%2==0:
            a_5=34
        else:
            a_5=-34
        G = (a_1 * self.A) - (a_2 * (self.A ** (2/3))) - (a_3 * (self.Z ** 2) / (self.A ** (1/3))) - (a_4 * ((self.A - 2 * self.Z) ** 2) / self.A + a_5 * (self.A ** (-3/4)))
        return int(G)
        
    def udenergy(self): # Удельная энергия
        e = self.energy()/self.A
        return round(e, 1)
    
    def mass(self): #масса ядра
        mass_proton = 7.289
        mass_neutron = 8.071
        return round(self.Z * mass_proton + self.N * mass_neutron - self.energy() + self.A*931.5, 2)
    
    def radius(self): # Радиус ядра
        r = 1.35*(self.A ** (1/3))
        return round(r, 2)
    
    def beta(self): # Устойчивость изотопа к бета распаду
        zravn = int(self.A/(0.015*self.A+2))+1
        if zravn == self.Z:
            print('Изотоп устойчив к бета-распаду.')
        else:
            print('Изотоп неустойчив к бета-распаду.')
    
    def  can_split(self): # Возможно ли деление данного изотопа на 2 одинаковых четно-четных осколка.
        if self.A % 4 == 0 and self.Z % 4 == 0:
            print('Делится на два четно-четных осколка.')
        else:
            print('Не делится на два четно-четных осколка.')
            
if __name__ == "__main__":
    nuclei = [
    [Nucleus(92,238), # U-238
    Nucleus(94,239), # Pu-239 
    Nucleus(98,252), # Cf-252
    Nucleus(94,238), # Pu-238
    Nucleus(52,135), # Te-135
    Nucleus(28,60),  # Ni-60
    Nucleus(8,16),   # O-16
    Nucleus(7,15),   # N-15
    Nucleus(15,29),  # P-29
    Nucleus(14,29),  # Si-29
    Nucleus(24,52)], # Cr-52
    ['U-238',
     'Pu-239',
     'Cf-252',
     'Pu-238',
     'Te-135',
     'Ni-60',
     'O-16',
     'N-15',
     'P-29',
     'Si-29',
     'Cr-52']
    ]

    i = 0
    j = 0
    slov1 = {}
    slov2 = {}
    
    for nucleus in nuclei[0]:
        print(nuclei[1][i])
        print('--------------------------------')
        print(f'Удельная энергия связи: {nucleus.udenergy()} МэВ')
        print(f'Масса атома: {nucleus.mass()} МэВ')
        print(f'Радиус атома: {nucleus.radius()} Фм')
        slov1[nucleus.z()]=nucleus.radius()
        slov2[nucleus.z()]=nucleus.mass()
        nucleus.beta()
        nucleus.can_split()
        print('')
        i=i+1
slov1 = sorted(slov1.items())
slov2 = sorted(slov2.items())
slov1 = dict(slov1)
slov2 = dict(slov2)
z = list(slov1.keys())
r = list(slov1.values())
m = list(slov2.values())
plt.figure(figsize=[9,6])
plt.plot(z, r, linewidth=2, marker='o', markersize=5)
plt.xlabel('Заряд ядра')
plt.ylabel('Радиус атома, Фм')
plt.title('Зависимость радиуса атома от заряда ядра')
plt.show()
plt.figure(figsize=[9,6])
plt.plot(z, m, linewidth=2, marker='o', markersize=5)
plt.xlabel('Заряд ядра')
plt.ylabel('Масса атома, Мэв')
plt.title('Зависимость массы атома от заряда ядра')
plt.show()


    
