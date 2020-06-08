import string
print("Mr claculator for elements of the periodic table")
print("This calculator uses this periodic table for refrence")
print("https://classroom.google.com/c/ODIyMzE0MTg3NTNa/a/MTEyMDM3NTUxMzIz/details")
print("The calculator was Developed by Saifeldin Mohamed Farid")
print("==========================================================================")

class Element:
    def __init__(self, relative_atomic_mass):
        self.relative_atomic_mass = relative_atomic_mass
    def ar(self):
        return self.relative_atomic_mass
    def __mul__(self, int):
        return self.ar() * int

class Compound:
    def __init__(self, formula):
        elements = list()
        for i in formula:
            if i in string.ascii_uppercase:
                elements += i
            else:
                elements[-1] += i
        self.formula = formula
        self.elements = elements
    def mr(self):
        ar_values = [eval(x) for x in self.elements]
        for i in range( len(ar_values) ):
            if type( ar_values[i] ) == Element:
                ar_values[i] = ar_values[i].ar()
        self.mr = sum(ar_values)
        return self.mr
#Now on to defining each element in the periodic table into this calculator
#Group 1
H = Element(1.01)
Li = Element(6.94)
Na = Element(22.99)
K = Element(39.10)
Rb = Element(85.47)
Cs = Element(132.91)
Fr = Element(223)
#Group 2
Be = Element(9.01)
Mg = Element(24.31)
Ca = Element(40.08)
Sr = Element(87.62)
Ba = Element(137.33)
Ra = Element(226)
#Transition elements
Sc = Element(44.96)
Y = Element(88.91)
La = Element(138.91)
Ac = Element(227)
Ti = Element(47.87)
Zr = Element(91.22)
Hf = Element(178.49)
Rf = Element(267)
V = Element(50.94)
Nb = Element(92.91)
Ta = Element(180.95)
Db = Element(268)
Cr = Element(52.00)
Mo = Element(95.96)
W = Element(183.84)
Sg = Element(269)
Mn = Element(54.94)
Tc = Element(98)
Re = Element(186.21)
Bh = Element(270)
Fe = Element(55.85)
Ru = Element(101.07)
Os = Element(190.23)
Hs = Element(269)
Co = Element(58.93)
Rh = Element(102.91)
Ir = Element(192.22)
Mt = Element(278)
Ni = Element(58.69)
Pd = Element(106.42)
Pt = Element(195.08)
Ds = Element(281)
Cu = Element(63.55)
Ag = Element(107.87)
Au = Element(196.97)
Rg = Element(281)
Zn = Element(65.38)
Cd = Element(112.41)
Hg = Element(200.59)
Cn = Element(285)
#Group 3
B = Element(10.81)
Al = Element(26.98)
Ga = Element(69.72)
In = Element(114.82)
Ti = Element(204.38)
Uut = Element(286)
#Group 4
C = Element(12.01)
Si = Element(28.09)
Ge = Element(72.63)
Sn = Element(118.71)
Pb = Element(207.20)
Uuq = Element(289)
#Group 5
N = Element(14.01)
P = Element(30.97)
As = Element(74.92)
Sb = Element(121.76)
Bi = Element(208.98)
Uup = Element(288)
#Group 6
O = Element(16.00)
S = Element(32.07)
Se = Element(78.96)
Te = Element(127.60)
Po = Element(209)
Uuh = Element(293)
#Group 7
F = Element(19.00)
Cl = Element(35.45)
Br = Element(79.90)
I = Element(126.90)
At = Element(210)
Uus = Element(294)
#Group 0
He = Element(4.00)
Ne = Element(20.18)
Ar = Element(39.95)
Kr = Element(83.90)
Xe = Element(131.29)
Rn = Element(222)
Uuo = Element(294)
#Lanthanides
Ce = Element(140.12)
Pr = Element(140.91)
Nd = Element(144.24)
Pm = Element(145)
Sm = Element(150.36)
Eu = Element(151.96)
Gd = Element(157.25)
Tb = Element(158.93)
Dy = Element(162.50)
Ho = Element(164.93)
Er = Element(167.26)
Tm = Element(168.93)
Yb = Element(173.05)
Lu = Element(174.97)
#Actinides
Th = Element(232.04)
Pa = Element(231.04)
U = Element(238.03)
Np = Element(237)
Pu = Element(244)
Am = Element(243)
Cm = Element(247)
Bk = Element(247)
Cf = Element(251)
Es = Element(252)
Fm = Element(257)
Md = Element(258)
No = Element(259)
Lr = Element(262)

while True:
    try:
        compound = Compound( input("\nInput the name of the compound/element you want to find its Mr\n") )
        print( compound.mr() )
    except:
        print("ERROR!!! Either you inputted an invalid element or didn't input the compound in the right format")
